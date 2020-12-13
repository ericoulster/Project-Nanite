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


# input is words, returns a wordcount
def wordcount(content):
    filetoken = content.translate(punctuation_strip).split(' ')
    wordcount = list(filter(r.match, filetoken))
    return len(wordcount)


# input is project's path, the filetype, and whether it is one file or multiple
def filepull(project_path, filetype='txt', isDirectory=False):
    
    if isDirectory is False:
        if filetype == 'txt':
            filepath = os.path.join(project_path)
            with open(filepath, "r", encoding='utf8') as file:
                return file.read()
            
        elif filetype == 'rtf':
            filepath = os.path.join(project_path)
            with open(filepath, "r", encoding='utf8') as file:
                rtf_file = file.read()
                clean_file = rtf_to_text(rtf_file)
                return clean_file
                
        elif filetype == 'docx':
            filepath = os.path.join(project_path)
            file = docx2txt.process(filepath)
            return file

        else:
            print("error: filepull only accepts 'txt', 'rtf', & 'docx' as args")
        
    if isDirectory is True:
        if filetype == 'txt':
            file_list = []
            for filepath in glob.glob(os.path.join(project_path, '*.' + str(filetype))):
                with open(filepath, "r", encoding='utf8') as file:
                    read_in = file.read()
                    file_list.append(read_in)
            merged_files = (" ").join(file_list)
            return merged_files
        
        elif filetype == 'rtf':
            file_list = []
            for filepath in glob.glob(os.path.join(project_path, '*.' + str(filetype))):
                with open(filepath, "r", encoding='utf8') as file:
                    rtf_file = file.read()
                    clean_file = rtf_to_text(rtf_file)
                    file_list.append(clean_file)
            merged_files = (" ").join(file_list)
            return merged_files    
        
        elif filetype == 'docx':
            file_list = []
            for filepath in glob.glob(os.path.join(project_path, '*.' + str(filetype))):
                file_list = docx2txt.process(filepath)
            merged_files = (" ").join(file_list)
            return file_list

# Input is from front-end (name, target, path, filetype, and now deadline

def wordmeta_set(name, target, path, filetype, deadline, goal):
    
    df = pd.read_csv('wordcount_meta.csv', index_col='Project Name')
    # Consolidate these options later on.
    
    if df.empty is True:
        new_row = pd.DataFrame.from_records({
            'Project Name':name, 'Daily Target':target, 'Project Path':path, 'Filetype':filetype, 'Deadline':deadline, 'Wordcount Goal':goal
        }, index=[0]).set_index('Project Name')
        df = df.append(new_row)
        df.to_csv('wordcount_meta.csv', index=True)
    
    elif df.index.str.match('^' + str(name) +'$').any() == True:
        new_row = pd.DataFrame.from_records({
            'Project Name':name, 'Daily Target':target, 'Project Path':path, 'Filetype':filetype, 'Deadline':deadline, 'Wordcount Goal':goal
        }, index=[0]).set_index('Project Name')
        df.update(new_row)
        df.to_csv('wordcount_meta.csv', index=True)
        
    else:
        new_row = pd.DataFrame.from_records({
            'Project Name':name, 'Daily Target':target, 'Project Path':path, 'Filetype':filetype, 'Deadline':deadline, 'Wordcount Goal':goal
        }, index=[0]).set_index('Project Name')
        df = df.append(new_row)
        df.to_csv('wordcount_meta.csv', index=True)

# Input is from front-end (takes name, returns wordcounts as a dict)

def wordmeta_pull(name):
    #TODO: change output dict to match those in sample_data.py (i.e. make sure values are all strings and ints, not more dicts, and - preferably - the keys match)
    df = pd.read_csv('wordcount_meta.csv', index_col='Project Name')
    
    if df.index.str.match('^' + str(name) +'$').any() == True:
        val_row = df[df.index == str(name)]
        return val_row.to_dict()
        
    else:
        #needed: error handling
        print("name not in system")
        


# Input is project name and daily wordcount, writes an update to the wordcount file

def wordcount_update(name, wordcount):
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

# Input is the old name (from system) and new name (input field). Changes name in back-end.

def wordmeta_rename(name, new_name):
    df = pd.read_csv('wordcount_meta.csv')
    if df.empty is True:
        pass
    
    elif df['Project Name'].str.match('^' + str(name) +'$').any() == True:
        df['Project Name'] = np.where(df[['Project Name']] == str(name), str(new_name), df[['Project Name']])
        df.to_csv('wordcount_meta.csv', index=False)
        
    else:
        pass

# takes in name of project, deletes it.

def project_delete(name):
    df = pd.read_csv('wordcount_meta.csv', index_col='Project Name')
    if df.empty is True:
        pass
    
    elif df.index.str.match('^' + str(name) +'$').any() == True:
        df = df.drop(labels=str(name), axis=0)
        df.to_csv('wordcount_meta.csv', index=True)
        os.remove(str(name) + '_wordcount.csv')
    else:
        pass
        
        
def daily_words_calculate(word_goal, goal_start_date, goal_finish_date):
    # We currently assume you are starting at zero words, or are factoring your already existant words into your decision.
    # This assumption may be worth revisiting later
    days_left = abs((datetime.strptime(goal_finish_date,"%d/%m/%Y") - datetime.strptime(goal_start_date,"%d/%m/%Y")).days)
    daily_target = ceil(word_goal/days_left)
    return daily_target


def word_goal_calculate(daily_target, goal_start_date, goal_finish_date):
    # We currently assume you are starting at zero words, or are factoring your already existant words into your decision.
    # This assumption may be worth revisiting later
    days_left = abs((datetime.strptime(goal_finish_date,"%d/%m/%Y") - datetime.strptime(goal_start_date,"%d/%m/%Y")).days)
    word_goal = daily_target*days_left
    return word_goal


