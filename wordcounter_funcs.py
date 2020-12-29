import os
import glob
import string
import re
import fileinput
import csv
from datetime import date, datetime
from math import ceil

import numpy as np
import pandas as pd

from striprtf.striprtf import rtf_to_text
import docx2txt

r = re.compile(r'\w+')

punctuation_strip = str.maketrans('', '', string.punctuation)

# creates wordcount meta if none exists
def wordcount_meta_check_create():
    if os.path.exists('wordcount_meta.csv') == False:
        
        try:
            colnames = [str('Project Name'), 
                        str('Daily Target'), 
                        str('Project Path'), 
                        str('Filetype'),
                        str('Start Date'),
                        str('Deadline'),
                        str('Wordcount Goal')]
            with open('wordcount_meta.csv', 'w', encoding='cp1252') as file:
                    filewriter = csv.writer(file)
                    filewriter.writerow(colnames)
                    filewriter.close()
        except:
            print("error, wordcount_meta was not found, and nanite could not create it.")
    else:
        pass

# input is words, returns a wordcount
def wordcount(content):
    filetoken = content.translate(punctuation_strip).split(' ')
    wordcount = list(filter(r.match, filetoken))
    return len(wordcount)


# input is project's path, the filetype, and whether it is one file or multiple
def filepull(project_path, filetype='txt', isDirectory=False):
    
    if isDirectory is False:
        
        if filetype == 'txt':
            try:
                filepath = os.path.join(project_path)
                with open(filepath, "r", encoding='utf8') as file:
                    return file.read()
            except:
                print("txt file failed to be read")
            
        elif filetype == 'rtf':
            try:
                filepath = os.path.join(project_path)
                with open(filepath, "r", encoding='utf8') as file:
                    rtf_file = file.read()
                    clean_file = rtf_to_text(rtf_file)
                    return clean_file
            except:
                print("rtf file failed to be read")
                
        elif filetype == 'docx':
            try:
                filepath = os.path.join(project_path)
                file = docx2txt.process(filepath)
                return file
            except:
                print("docx file failed to be read")
        else:
            print("error: filepull only accepts 'txt', 'rtf', & 'docx' filetypes")
        
    if isDirectory is True:
        if filetype == 'txt':
            try:
                file_list = []
                for filepath in glob.glob(os.path.join(project_path, '*.' + str(filetype))):
                    with open(filepath, "r", encoding='utf8') as file:
                        read_in = file.read()
                        file_list.append(read_in)
                merged_files = (" ").join(file_list)
                return merged_files
            except:
                print("error, txt files didn't read correctly")
        
        elif filetype == 'rtf':
            try:
                file_list = []
                for filepath in glob.glob(os.path.join(project_path, '*.' + str(filetype))):
                    with open(filepath, "r", encoding='utf8') as file:
                        rtf_file = file.read()
                        clean_file = rtf_to_text(rtf_file)
                        file_list.append(clean_file)
                merged_files = (" ").join(file_list)
                return merged_files
            except:
                print("error, rtf files didn't read correctly")
        
        elif filetype == 'docx':
            try:
                file_list = []
                for filepath in glob.glob(os.path.join(project_path, '*.' + str(filetype))):
                    file_list = docx2txt.process(filepath)
                merged_files = (" ").join(file_list)
                return file_list
            except:
                print("error, docx files didn't read correctly")
        else:
            print("error: filepull only accepts 'txt', 'rtf', & 'docx' filetypes")
# Input is from front-end (name, target, path, filetype, and now deadline

def wordmeta_set(name, target, path, filetype, start_date, deadline, goal):
    
    # creates wordcount meta if none exists.
    wordcount_meta_check_create()
    
    # try to read wordcount meta csv
    try:    
        df = pd.read_csv('wordcount_meta.csv', index_col='Project Name')
        
    except:
        print("error: nanite can't read records file")
    # Consolidate these options later on.
    
    # Condition 1: if records are empty, insert the first record.
    
    if df.empty is True:
        try:
            new_row = pd.DataFrame.from_records({
                'Project Name':name, 'Daily Target':target, 'Project Path':path, 'Filetype':filetype, 'Start Date':start_date, 'Deadline':deadline,
            'Wordcount Goal':goal}, index=[0]).set_index('Project Name')
            df = df.append(new_row)
            df.to_csv('wordcount_meta.csv', index=True)
        except:
            print("error, nanite cannot insert row of data into empty record-list.")
    
    
    # Condition 2: If the record exists, update it.
    
    elif df.index.str.match('^' + str(name) +'$').any() == True:
        try:
            new_row = pd.DataFrame.from_records({
                'Project Name':name, 'Daily Target':target, 'Project Path':path, 'Start Date':start_date, 'Filetype':filetype, 'Deadline':deadline,
             'Wordcount Goal':goal}, index=[0]).set_index('Project Name')
            df.update(new_row)
            df.to_csv('wordcount_meta.csv', index=True)
        except:
            print("error, nanite can't read row of data in records")
    
    # Condition 3: If no record exists, but other records exist, insert the record.
    
    else:
        try:
            new_row = pd.DataFrame.from_records({
                'Project Name':name, 'Daily Target':target, 'Project Path':path, 'Start Date':start_date, 'Filetype':filetype, 'Deadline':deadline,
             'Wordcount Goal':goal}, index=[0]).set_index('Project Name')
            df = df.append(new_row)
            df.to_csv('wordcount_meta.csv', index=True)
        except:
            print("error: nanite can't read data in records")


# Input is from front-end (takes name, returns wordcounts as a dict)

def wordmeta_pull_all():
    # BP NOTE: added this function 

    # creates wordcount meta if none exists.
    wordcount_meta_check_create()

    df = pd.read_csv('wordcount_meta.csv', index_col='Project Name')
    return df.to_dict(orient='index')

def wordmeta_pull(name):

    # creates wordcount meta if none exists.
    wordcount_meta_check_create()

    df = pd.read_csv('wordcount_meta.csv', index_col='Project Name')
    
    if df.index.str.match('^' + str(name) +'$').any() == True:
        val_row = df[df.index == str(name)]
        return val_row.reset_index().to_dict(orient='records')
        
    else:
        #needed: error handling
        print("name not in system")
        


# Input is project name and daily wordcount, writes an update to the wordcount file

def wordcount_update(name, wordcount):
    try:
        #This produces a csv file with date, overall target and actual wordcount, and wants to update the actual wordcount (dailywords -> actual word count). Actual word count is collected by the back end and only displayed in the front.
        timestamp = datetime.now().strftime("%d/%m/%Y - %X")
        
        if os.path.exists(str(name) + '_wordcount.csv') == False:
            colnames = [str('Date'), str('Total Wordcount'), str('Session Wordcount'), str('Daily Target') ]
            with open(str(name) + '_wordcount.csv', 'w', encoding='cp1252') as file:
                filewriter = csv.writer(file)
                filewriter.writerow(colnames)
                filewriter.close()
        else:
            pass
        # Used to grab regularly occuring daily target
        meta_df = pd.read_csv('wordcount_meta.csv', index_col='Project Name')    
        
        df = pd.read_csv(str(name) + '_wordcount.csv')
        
        # session wordcount is this session subtracted by last session 
        if df.empty is True:
            session_wordcount = wordcount
        else:
            session_wordcount = wordcount - df.iloc[-1]['Total Wordcount']
        
        df = df.append({'Date': timestamp, 'Total Wordcount':wordcount, 'Session Wordcount': session_wordcount, 'Daily Target':meta_df.loc[name]['Daily Target']}, ignore_index=True)
        df.to_csv(str(name) + '_wordcount.csv', index=False)
    except:
        print("wordcount failed to update")

# Input is the old name (from system) and new name (input field). Changes name in back-end.

def wordmeta_rename(name, new_name):
    try:
        df = pd.read_csv('wordcount_meta.csv')
        if df.empty is True:
            pass
        
        elif df['Project Name'].str.match('^' + str(name) +'$').any() == True:
            df['Project Name'] = np.where(df[['Project Name']] == str(name), str(new_name), df[['Project Name']])
            df.to_csv('wordcount_meta.csv', index=False)
            
        else:
            pass
    except:
        print("project failed to be renamed")

# takes in name of project, deletes it.

def project_delete(name):
    try:
        df = pd.read_csv('wordcount_meta.csv', index_col='Project Name')
        if df.empty is True:
            pass
        
        elif df.index.str.match('^' + str(name) +'$').any() == True:
            df = df.drop(labels=str(name), axis=0)
            df.to_csv('wordcount_meta.csv', index=True)
            os.remove(str(name) + '_wordcount.csv')
        else:
            pass
    except:
        print("project failed to delete")
        
        
def daily_words_calculate(word_goal, goal_start_date, goal_finish_date):
    # We currently assume you are starting at zero words, or are factoring your already existant words into your decision.
    # This assumption may be worth revisiting later
    #NOTE: changed incoming date format #days_left = abs((datetime.strptime(goal_finish_date,"%d/%m/%Y") - datetime.strptime(goal_start_date,"%d/%m/%Y")).days)
    days_left = abs((datetime.strptime(goal_finish_date,"%Y-%m-%d") - datetime.strptime(goal_start_date,"%Y-%m-%d")).days)
    daily_target = ceil(int(word_goal)/days_left)
    return daily_target


def word_goal_calculate(daily_target, goal_start_date, goal_finish_date):
    # We currently assume you are starting at zero words, or are factoring your already existant words into your decision.
    # This assumption may be worth revisiting later
    #NOTE: changed incoming date format #days_left = abs((datetime.strptime(goal_finish_date,"%d/%m/%Y") - datetime.strptime(goal_start_date,"%d/%m/%Y")).days)
    days_left = abs((datetime.strptime(goal_finish_date,"%Y-%m-%d") - datetime.strptime(goal_start_date,"%Y-%m-%d")).days)
    word_goal = int(daily_target)*days_left
    return word_goal

# returns data for the wordcount table
def wordcount_pull(name):
    
    if os.path.exists(str(name) + '_wordcount.csv') == False:
        return print("no wordcount record")
    else:
        df = pd.read_csv(str(name) + '_wordcount.csv')
        return df.to_dict(orient='records')

# takes project name, returns number of days wordstreak
def wordstreak(name):
    try:
        df = pd.read_csv(str(name) + '_wordcount.csv')
        
        if df.empty is True:
            return 0
        else:
            df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y - %X').dt.date

            # Max daily target, sum of Session Wordcount
            df_g = df.groupby(['Date']).agg({'Session Wordcount':'sum', 'Daily Target':'last'})
            # sort by df_g asc
            df_g = df_g.sort_values(ascending=False, by='Date')
            x = 0
            for i in range(len(df_g)):
                if df_g['Session Wordcount'][i] >= df_g['Daily Target'][i]:
                    x += 1
                else:
                    return(x)
                    break
    except:
        print("wordstreak failed to be calculated")


    
def write_most_on(name):
    # This is currently an average - but which metric to use introduces bias, worth discussing.
    df = pd.read_csv(str(name) + '_wordcount.csv')
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y - %X').dt.date
    df_g = df.groupby(['Date']).agg({'Session Wordcount':'sum', 'Daily Target':'last'}).reset_index()
    df_g['Day of week'] = pd.to_datetime(df_g['Date']).dt.day_name()
    df_g = df_g.groupby('Day of week')['Session Wordcount'].mean().sort_values(ascending=False)
    return list(df_g.head(1).to_dict().keys())

# Displays sidepane info easily
def get_sidepane_info(name):
    #TODO: this gets info for one project, but (I understood that) the sidebar is meant to sum/average across projects
    words = wordcount_pull(name)[-1]['Total Wordcount'] #TODO: this throws an error:  'NoneType' object is not subscriptable
    streak = wordstreak(name)
    day = write_most_on(name)
    info = {
        'words written':words, "day longest streak":streak, "You write most on":str(day)[2:-2]
    }
    return info
