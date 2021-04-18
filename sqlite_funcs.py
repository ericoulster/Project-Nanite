### Dependendies ###
from datetime import datetime
from collections import namedtuple

import numpy as np
import pandas as pd

import sqlite3


### Variables ###

sqlite3_path = './database/nanite_storage.sqlite3'

# Using namedtuple to define dict-like structure for retrieved data (using ._asdict() method on them)

AuthorVals = namedtuple('Author', 'author_id username password acct_created_on')
ProjectVals = namedtuple('Project', 'project_id author_id project_name project_created_on project_start_date deadline wordcount_goal current_daily_target filetype is_folder project_path')
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
    filetype text,
    is_folder int,
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
        filetype=None,
        is_folder=True,
        project_path=None):
        """
        Takes in a project info, then creates a new project for a given author.
        Eric note: Add 'page conversion' later in the future
        """
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
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            params = [None, self.author_id, project_name, now, project_start_date, deadline, 
            wordcount_goal, current_daily_target, filetype, is_folder, project_path]
            try:
                cur.execute(query, params)
                conn.commit()
            except:
                print("Query failed")
            finally:
                conn.close()
        else:
            print("project with this name already exists")
            conn.close()


    def delete_project(self, project_name):
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("DELETE FROM projects where project_name=? AND author_id=?", (project_name, self.author_id))
        conn.commit()
        conn.close()


    def return_projects(self):
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM projects where author_id=?", self.author_id)
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
        """Returns all wordcount records from all projects."""
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM words where author_id=?", self.author_id)
        row = cur.fetchall()
        data = [dict(WordVals(*row[i])._asdict()) for i in range(len(rows))]
        conn.close()
        return data


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
        self.filetype = None
        self.is_folder = None
        self.project_path = None

        self.author_set = False
        self.daily_target_set = False
        self.project_path = False

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
        cur.execute("SELECT * FROM projects where project_id=?", (project_id,))
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
        self.filetype = data[8]
        self.is_folder = data[9]
        self.project_path = data[10]
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
        cur.execute("SELECT * FROM projects where project_id=?", (project_id,))
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
            print("No name combination found.")
            conn.close()
        

    def get_wordcounts(self):
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM words where project_id=?", self.project_id)
        row = cur.fetchall()
        data = [dict(WordVals(*row[i])._asdict()) for i in range(len(rows))]
        conn.close()
        return data

    def set_wordcounts(self):
        """Input Daily Wordcounts (some functions not finished)"""
        if (self.current_daily_target == False):
            print("Wcount not pushed, Wordcount Target not set!")
        elif self.project_path is None:
            print("Project Path not set- Data cannot be pulled!")
        else:
            try:
                words = filepull(self.project_path, self.is_folder, self.filetype)
            except:
                print("filepull failed.")
            try:
                wc = wordcount(words)
            except:
                print("words cannot be counted")
                now = timestamp()
            query = '''INSERT INTO projects values (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            params = [None, self.project_id, self.author_id, now, wc, self.current_daily_target]
            try:
                cur.execute(query, params)
                conn.commit()
            except:
                print("Query insertion failed")
            finally:
                conn.close()

    def change_target(self):
        """Still needs doing"""
        pass

    def rename_project(self, new_name):
        """Renames a project based on new_name"""
        conn = sqlite3.connect(sqlite3_path)
        cur = conn.cursor()
        cur.execute("UPDATE projects SET project_name=? WHERE project_id=?", (new_name, self.project_id))
        conn.commit()
        conn.close()