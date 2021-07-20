### Dependendies ###
from datetime import datetime
from collections import namedtuple
import time
import os

import numpy as np
import pandas as pd

import sqlite3

from file_funcs import file_pipe, is_streak, streak_length, change_goal, daily_words_calculate, word_goal_calculate
### Variables ###

sqlite3_path = './database/nanite_storage.sqlite3'

# Using namedtuple to define dict-like structure for retrieved data (using ._asdict() method on them)

AuthorVals = namedtuple('Author', 'author_id username password acct_created_on')
ProjectVals = namedtuple('Project', 'project_id author_id project_name project_created_on project_start_date deadline wordcount_goal current_daily_target wp_page project_path')
WordVals = namedtuple('Wordcounts', 'record_id project_id author_id Wdate Wcount Wtarget')

## DDL init Queries ##

create_author_sql = """
CREATE TABLE IF NOT EXISTS authors (
    author_id integer PRIMARY KEY,
    username text NOT NULL,
    password text,
    acct_created_on text NOT NULL
)
"""

create_project_sql = """
CREATE TABLE IF NOT EXISTS projects (
    project_id integer PRIMARY KEY,
    author_id integer,
    project_name text NOT NULL,
    project_created_on text NOT NULL,
    project_start_date text,
    deadline text,
    wordcount_goal int,
    current_daily_target int,
    wp_page int,
    project_path text,
    FOREIGN KEY (author_id) REFERENCES authors (author_id)
)
"""

create_words_sql = """
CREATE TABLE IF NOT EXISTS words (
    record_id integer PRIMARY_KEY,
    project_id integer,
    author_id integer,
    Wdate text NOT NULL,
    Wcount int NOT NULL,
    Wtarget int,
    FOREIGN KEY (project_id) REFERENCES projects (project_id),
    FOREIGN KEY (author_id) REFERENCES authors (author_id)
)
"""


### Functions ###

def timestamp(): 
    return str(datetime.now())

def datestamp():
    return str(datetime.now().date())

def samedate(date: str) -> bool(): # For some reason date is actually a date? Not sure why???
    if date == None:
        return False
    else:
        day = str(date.date())
        today = datestamp()

        if day == today:
            return True
        else:
            return False


def db_init():
    """
    Creates databases if they don't exist.
    Uses DDL init Queries.
    Should be Run on start-up.
    """
    if os.path.exists(sqlite3_path) == False:
        conn = sqlite3.connect(sqlite3_path)
        conn.execute("PRAGMA foreign_keys = 1")
        conn.execute(create_author_sql)
        conn.execute(create_project_sql)
        conn.execute(create_words_sql)
        conn.close()
    else:
        print("db already exists")



def return_project_screen(author_id:int) -> list(dict()):
    """
    Returns all the values needed for the Projects page, each 'div' as an individual dict.
    Needs to be tested on entries without a table.
    """
    a = AuthorActions(author_id)
    projects = a.return_projects()
    project_ids = [i[0] for i in projects]
    projects_list = []
    for i in project_ids:
        p = ProjectActions(i)
        p.set_project()

        try:
            row = p.return_wordcounts()[-1]
        except:
            # Maybe I should just raise an exception?
            row = {'Wcount': 0, 'Wdate': None, 'Wtarget': 0, 'project_id': p.project_id, 'record_id': None, 'Wtarget_sum': 0, 'daily_words': 0.0, 'streak': 0}
        if samedate(row['Wdate']) is False:
            p_dict = {
            'project_name': p.project_name, 'project_id': row['project_id'], 'daily_words': 0, 
            'today_goal': row['Wtarget'], 'total_progress': row['Wcount'], 'current_streak':0
            }   
        else:   
            p_dict = {
            'project_name': p.project_name, 'project_id': row['project_id'], 'daily_words': row['daily_words'], 
            'today_goal': row['Wtarget'], 'total_progress': row['Wcount'], 'current_streak':row['streak']
            }            
        projects_list.append(p_dict)
        
    return projects_list


def return_stats_screen(p_id:int) -> dict():
    """
    Returns a dict of the following:
    -current wordcount
    -wordcount goal

    -average daily wordcount
    -highest daily wordcount
    -current streak
    -max streak

    -wordcount freq, daily, weekly, monthly
    -day-of-week averages
    -current deadline
    """
    p = ProjectActions()
    p.set_project(project_id=p_id)
    
    wgad = p.return_wordgoal_and_deadline()
    weekBar = p.return_weekly_avg()
    
    daily = p.return_wordcounts('D')
    weekly = p.return_wordcounts('W')
    monthly = p.return_wordcounts('M')
    
    #  ===========================================/
    #  Refactor Later - Changed max_streak and current_streak to string since js 
    #     has trouble reading numpy.int64.
    # ==========================================/
    day_df = pd.DataFrame(daily)
    max_streak = int(day_df['streak'].max())
    current_streak = int(day_df['streak'].iloc[-1])

    max_wc = day_df['daily_words'].max()
    mean_wc = day_df['daily_words'].mean()
    
    current_wc = int(day_df['Wcount'].iloc[-1])

    # ====================================================!!
    # Refactor later -- JS has trouble retrieving Python Timestamp for some reason
    #    need to figure out why.
    # ====================================================!!

    for obj in daily:
        obj["Wdate"] = obj["Wdate"].strftime("%m/%d/%y")
    for obj in weekly:
        obj["Wdate"] = obj["Wdate"].strftime("%m/%d/%y")
    for obj in monthly:
        obj["Wdate"] = obj["Wdate"].strftime("%m/%d/%y")

    stats_screen = {'word_goal_and_deadline': wgad, 'barData': {'daily':daily, 'weekly':weekly, 'monthly':monthly}, 'weekBar': weekBar, 'max_streak':max_streak, 'current_streak': current_streak, 'max_wc': max_wc, 'mean_wc':mean_wc, 'current_wc':current_wc}

    return stats_screen


## 'Top Level' Funcs ##

def create_author(author_name, password=''):    
    """ 
    Inserts an Author into database if they don't exist.
    If they do, this task does not go through. 
    """
    # add a check to make sure the author doesn't already exist
    now = timestamp()
    conn = sqlite3.connect(sqlite3_path)
    cur = conn.cursor()
    
    cur.execute("SELECT username FROM authors WHERE username=?", (author_name,))
    entry = cur.fetchone()
    if entry is None:

        query = '''INSERT INTO authors
                    values (?,?,?,?) '''
        
        params = (None, author_name, password, now)
        cur.execute(query, params)
        conn.commit()
        conn.close()
    else:
        conn.close()
        return print("This row already exists!")


def return_author_list():
    """
    Prints all authors as a list of dicts
    """
    conn = sqlite3.connect(sqlite3_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM authors")
    rows = cur.fetchall()
    data = [dict(AuthorVals(*rows[i])._asdict()) for i in range(len(rows))]
    conn.close()
    return data


## Author Level Class ##

class AuthorActions:

    def __init__(self, author_id=-1):
        self.author_id = author_id
    

    def return_info(self):
        """
        prints the row of information for the author
        """ 
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM authors WHERE author_id=?", (self.author_id,))
        row = cur.fetchall()
        data = AuthorVals(*row[0])
        conn.close()
        return dict(data._asdict())


    def id_by_name(self, author_name):
        """
        Sets AuthorActions to the right ID based on the author's name.
        """
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM authors WHERE username=?", (author_name,))
        data = cur.fetchone()
        if data is not None:
            self.author_id = int(data[0])
            conn.close()
        else:
            print("No name found.")
            conn.close()


    def create_project(
        self, 
        project_name, 
        project_start_date=None,
        deadline=None,
        wordcount_goal=None, 
        current_daily_target=None,
        wp_page=None,
        project_path=None):
        """
        Takes in a project info, then creates a new project for a given author.
        """
        
        # This just fills in other variables that are missing when creating a project

        if (wordcount_goal is None) & (current_daily_target is not None) & (project_start_date is not None) & (deadline is not None):
            wordcount_goal = word_goal_calculate(current_daily_target, project_start_date, deadline)
        elif (wordcount_goal is not None) & (current_daily_target is None) & (project_start_date is not None) & (deadline is not None):
            current_daily_target = daily_words_calculate(wordcount_goal, project_start_date, deadline)
        else:
            pass        

        now = timestamp()
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT project_id FROM projects WHERE project_name=? AND author_id=?", (project_name,self.author_id))
        entry = cur.fetchone()
        conn.close()
        if entry is None:
            # do insert
            conn = sqlite3.connect(sqlite3_path)
            cur = conn.cursor()
            query = '''INSERT INTO projects values (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            params = [None, self.author_id, project_name, now, project_start_date, deadline, 
            wordcount_goal, current_daily_target, wp_page, project_path]
            #try:
            cur.execute(query, params)
            conn.commit()
            #except:
                #print("Query failed")
            #finally:
            conn.close()
        else:
            print("project with this name already exists")
            conn.close()


    def delete_project(self, project_name):
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("DELETE FROM projects where project_name=? AND author_id=?", (project_name, self.author_id))
        ## TODO: also delete FROM words ??
        conn.commit()
        conn.close()


    def return_projects(self):
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM projects where author_id=?", (self.author_id, ))
        data = cur.fetchall()
        conn.close()
        return data


    def rename_author(self, new_name):
        """Renames an author based on new_name"""
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("UPDATE authors SET username=? WHERE author_id=?", (new_name, self.author_id))
        conn.commit()
        conn.close()

    def return_all_wordcounts(self):
        """Returns all wordcount records from all projects for a given author."""
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM words where author_id=?", (self.author_id, ))
        row = cur.fetchall()
        data = [dict(WordVals(*row[i])._asdict()) for i in range(len(rows))]
        conn.close()
        return data

    def return_freq_wordcounts(self, freq='D') -> dict:
        """
        Return frequency of wordcounts for a given author's projects
        freq maps to the granularity of the data, in line with pandas granularity values.
        """
        freq = freq
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM words where author_id=?", (self.author_id, ))
        row = cur.fetchall()
        data = [dict(WordVals(*row[i])._asdict()) for i in range(len(row))]
        conn.close()
        df = pd.DataFrame(data)
        df.index = pd.DatetimeIndex(df['Wdate'])

        earliest = df.index[0]
        latest = df.index[-1]

        new_index = pd.date_range(earliest, latest, freq='D')

        df = df.groupby(pd.Grouper(freq='D')).last()
        df = df.reindex(new_index, method='ffill')
        df = df.fillna(method='ffill')
        df['Wtarget_sum'] = df['Wtarget'].cumsum()
        df['Wdate'] = df['Wdate'].apply(lambda x: x[:10])
        df['streak'] = [is_streak(i, df['Wcount'], df['Wtarget']) for i in range(len(df))]
        d_list = streak_length(df['streak'])
        df['streak'] = pd.Series(d_list, index=new_index)

        df = df.groupby(pd.Grouper(freq=freq)).last()
        records = df.to_dict(orient='records')
        return records

## Project-level Class ##

class ProjectActions:
    
    def __init__(self, 
    project_id=-1, 
    author_id=-1
    ):
        self.project_id = project_id
        self.author_id = author_id

        self.project_name = None
        self.project_start_date = None
        self.deadline = None
        self.wordcount_goal = None
        self.current_daily_target = None
        self.wp_page = None
        self.project_path = None

        self.author_set = False
        self.daily_target_set = False

    def set_project(self, project_id=None):
        """
        Uses either the set id or an input id to assign project information to the ProjectActions Object.
        In turn, this also allows one to make changes to wordcounts.
        """
        # checkproject id in the database- reset 
        if (project_id is None) and (self.project_id == -1):
            raise Exception("Error: No value set for project_id")
        elif project_id is None:
            project_id = self.project_id 
        else:
            pass
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM projects where project_id=?", (project_id, ))
        row = cur.fetchall()
        data = row[0]
        self.project_id = project_id
        self.author_id = data[1]
        self.project_name = data[2]
        self.project_created_on = data[3]
        self.project_start_date = data[4]
        self.deadline = data[5]
        self.wordcount_goal = data[6]
        self.current_daily_target = data[7]
        self.wp_page = data[8]
        self.project_path = data[9]
        self.author_set = True
        self.daily_target_set = True
        conn.close()
        
    def get_project(self, project_id=None):
        if (project_id is None) and (self.project_id == -1):
            raise Exception("Error: No value set for project_id")
        elif project_id is None:
            project_id = self.project_id 
        else:
            pass
        # checkproject id in the database- reset 
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM projects where project_id=?", (project_id, ))
        row = cur.fetchall()
        data = [dict(ProjectVals(*row[i])._asdict()) for i in range(len(row))]
        conn.close()
        return data

    def id_by_names(self, author_name, project_name):
        """
        Sets ProjectActions to the right project & author based on the project & author's name.
        """
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        query="""
        SELECT authors.author_id, projects.project_id, authors.username, projects.project_name 
        FROM projects
        INNER JOIN authors ON projects.author_id = authors.author_id
        WHERE authors.username=? AND projects.project_name=? 
        """
        params = (author_name, project_name)
        cur.execute(query, params)
        data = cur.fetchone()
        if data is not None:
            self.project_id = int(data[1])
            self.author_id = int(data[0])
            conn.close()
            author_set = True
        else:
            raise Exception("No name combination found.")
            conn.close()
        

    def return_wordcounts_simple(self):
        """
        return all wordcounts for a given project
        """
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM words where project_id=?", (self.project_id, ))
        row = cur.fetchall()
        data = [dict(WordVals(*row[i])._asdict()) for i in range(len(row))]
        conn.close()
        return data


    def return_wordcounts(self, freq='D') -> dict:
        """
        Return frequency of wordcounts for a given project
        freq maps to the granularity of the data, in line with pandas timeseries granularity values.
        """
        freq = freq
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM words where project_id=?", (self.project_id, ))
        row = cur.fetchall()
        data = [dict(WordVals(*row[i])._asdict()) for i in range(len(row))]
        conn.close()
        df = pd.DataFrame(data)
        df.index = pd.DatetimeIndex(df['Wdate'])

        earliest = df.index[0]
        latest = df.index[-1]

        new_index = pd.date_range(earliest, latest, freq='D')

        df = df.groupby(pd.Grouper(freq='D')).last()
        df = df.reindex(new_index, method='ffill')
        df = df.fillna(method='ffill')
        df = df.drop(columns='Wdate')
        df['Wtarget_sum'] = df['Wtarget'].cumsum()
        # df['daily_words'] = [
        #     (df[['Wcount']].iloc[i] - df[['Wcount']].iloc[i-1]).clip(0) if i >= 1 
        #     else df[['Wcount']].iloc[i] for i in range(len(df))
        #     ]
        df['daily_words'] = [
            (df.iloc[i]['Wcount'] - df.iloc[i-1]['Wcount']).clip(0) if i >= 1 
            else df.iloc[i]['Wcount'] for i in range(len(df))
            ]
        df['streak'] = [is_streak(i, df['Wcount'], df['Wtarget']) for i in range(len(df))]
        d_list = streak_length(df['streak'])
        df['streak'] = pd.Series(d_list, index=new_index)
        
        df = df.groupby(pd.Grouper(freq=freq)).last()
        df = df.reset_index().rename(columns={'index':'Wdate'})
        records = df.to_dict(orient='records')
        return records


    def return_weekly_avg(self):
        """
        return days of writing
        YOU NEED TO CALCULATE DIFFERENCE BASED ON LAST ROW (THAT EXISTS ELSEWHERE)
        """
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM words where project_id=?", (self.project_id,))
        row = cur.fetchall()
        data = [dict(WordVals(*row[i])._asdict()) for i in range(len(row))]
        conn.close()
        df = pd.DataFrame(data)
        df['Wdate'] = pd.to_datetime(df['Wdate'], format='%Y-%m-%d').dt.date
        df['daily_words'] = [
            (df[['Wcount']].iloc[i] - df[['Wcount']].iloc[i-1]).clip(0) if i >= 1 
            else df[['Wcount']].iloc[i] for i in range(len(df))
            ]
        #I'm getting a glitch where extra meta-data comes with daily_words, the line below fixes it
        df['daily_words'] = [df['daily_words'][i][0] for i in range(len(df))]
        df_g = df.groupby(['Wdate']).agg({'daily_words':'mean', 'Wtarget':'last'}).reset_index()
        df_g['Day of week'] = pd.to_datetime(df_g['Wdate']).dt.day_name()
        df_g = pd.DataFrame(df_g.groupby('Day of week')['daily_words'].mean())
        df_g['IsMax'] = np.where(df_g >= np.max(df_g), 1, 0)
        df_g['Day'] = df_g.index.str[:3]
        df_g ['Wcount'] = df_g['daily_words']
        df_g = df_g.drop(columns='daily_words')
        weekmeans = df_g.to_dict(orient='records')
        maxday = df_g[df_g['IsMax'] == 1].index[0]
        barData = {'weekmeans': weekmeans, 'maxday': maxday}
        return barData


    def return_wordgoal_and_deadline(self):
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT deadline, wordcount_goal FROM projects where project_id=?", (self.project_id,))
        row = cur.fetchone()
        conn.close()
        wordgoal_and_deadline = dict({'wordgoal':row[1], 'deadline':row[0]})
        return wordgoal_and_deadline
        

    def enter_wordcount(self):
        """
        Input Daily Wordcounts
        """
        if (self.current_daily_target == False):
            raise Exception("Wcount not pushed, Wordcount Target not set!")
        elif self.project_path is None:
            raise Exception("Project Path not set- Data cannot be pulled!")
        else:
            try:
                wc = file_pipe(self.project_path)
            except:
                raise Exception("Error: wordcount pipeline (file_pipe) failed.")
            now = timestamp()
            query = '''INSERT INTO words values (
                ?, ?, ?, ?, ?, ?) '''
            params = [None, self.project_id, self.author_id, now, wc, self.current_daily_target]
            try:
                conn = sqlite3.connect(sqlite3_path)
                cur = conn.cursor()
                cur.execute(query, params)
                conn.commit()
            except:
                print("Query insertion failed")
            finally:
                conn.close()


    def change_daily_words(self, daily_words):
        """
        changes daily_words value.
        Re-calibrates word goal accordingly (based on deadline)
        Requires project_start_date, deadline, and project_id to work
        """
        if (self.project_start_date is not None) & (self.deadline is not None):
            word_goal = word_goal_calculate(daily_words, self.project_start_date, self.deadline)
            conn = sqlite3.connect(sqlite3_path)
            cur = conn.cursor()
            cur.execute("UPDATE projects SET wordcount_goal=?, current_daily_target=? WHERE project_id=?", (word_goal, daily_words, self.project_id))
            conn.commit()
            conn.close()
            self.current_daily_target = daily_words
            self.wordcount_goal = word_goal
        else:
            raise Exception("Error: Submission requires project_start_date & deadline")

    def change_word_goal(self, word_goal):
        """
        changes daily_words value.
        Also changes daily words to re-calibrate.
        Requires project_start_date, deadline, and project_id to work
        """
        if (self.project_start_date is not None) & (self.deadline is not None):
            daily_words = daily_words_calculate(word_goal, self.project_start_date, self.deadline)
            conn = sqlite3.connect(sqlite3_path)
            cur = conn.cursor()
            cur.execute("UPDATE projects SET wordcount_goal=?, current_daily_target=? WHERE project_id=?", (word_goal, daily_words, self.project_id))
            conn.commit()
            conn.close()
            self.current_daily_target = daily_words
            self.wordcount_goal = word_goal
        else:
            raise Exception("Error: Submission requires project_start_date & deadline")


    def change_deadline(self, new_deadline):
        """
        Changes deadline value.
        Re-calibrates daily_words accordingly
        Requires project_start_date, word_goal, and project_id to work
        """
        if (self.project_start_date is not None) & (self.wordcount_goal is not None):
            daily_words = daily_words_calculate(self.wordcount_goal, self.project_start_date, new_deadline)
            conn = sqlite3.connect(sqlite3_path)
            cur = conn.cursor()
            cur.execute("UPDATE projects SET current_daily_target=?, deadline=? WHERE project_id=?", (daily_words, new_deadline, self.project_id))
            conn.commit()
            conn.close()
            self.deadline = new_deadline
            self.current_daily_target = daily_words        
        else:
            raise Exception("Error: Submission requires project_start_date & wordcount_goal")

    def change_words_per_page(self, new_wp_page):
        "Changes wp_page value"
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("UPDATE projects SET wp_page WHERE project_id=?", (new_wp_page, self.project_id))
        conn.commit()
        conn.close()       
        self.wp_page = new_wp_page


    def rename_project(self, new_name):
        """Renames a project based on new_name"""
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("UPDATE projects SET project_name=? WHERE project_id=?", (new_name, self.project_id))
        conn.commit()
        conn.close()
        self.project_name = new_name



## Additional Project Actions ##

def get_max_streak(df: pd.DataFrame()) -> int():
    """
    Use on the output of get_wordcount to ge the max wordcount.
    """
    df = pd.DataFrame(records)
    return df['streak'].max()

