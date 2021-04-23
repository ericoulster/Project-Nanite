import string
from datetime import date, datetime
from math import ceil
import re
import shutil
from pathlib import Path

from striprtf.striprtf import rtf_to_text
import docx2txt



# Note for etl: .stat().st_mtime in pathlib gives the time of last modification of a file



### Funcs ###


## Wordcount Funcs ##

r = re.compile(r'\w+')

punctuation_strip = str.maketrans('', '', string.punctuation)


# input is words, returns a wordcount
def wordcount(content: str) -> int:
    """
    The mechanism to count words.
    A component of file_pipe
    """
    filetoken = content.translate(punctuation_strip).split(' ')
    wordcount = list(filter(r.match, filetoken))
    return len(wordcount)


def path_parser(path: str) -> str:
    """
    Takes in path, returns filetype.
    A component of file_pipe
    """
    path_raw = r"{}".format(path)
    txt = '.txt'
    rtf = '.rtf'
    docx = '.docx'
    txt = path_raw.rfind(txt)
    rtf = path_raw.rfind(rtf)
    docx = path_raw.rfind(docx)
    if txt != -1:
        return '.txt'
    elif rtf != -1:
        return '.rtf'  
    elif docx != -1:
        return '.docx'   
    else:
        return None



def filepull(path: Path()) -> str:  
    """
    Takes in directory, returns all words from it.
    A component of file_pipe
    """
    ftype = path_parser(path)

    if ftype == '.txt':
        try:
            with open(path, "r", encoding='utf8') as txtfile:
                words = txtfile.read()
                txtfile.close()
                return words
        except:
            raise Exception("Error with reading .txt file")

    elif ftype == '.rtf':
        try:
            with open(path, "r", encoding='utf8') as rtffile:
                rtf_file = rtffile.read()
                clean_file = rtf_to_text(rtf_file)
                words = clean_file     
                rtffile.close()
                return words         
        except:
            raise Exception("Error with reading .rtf file")

    elif ftype == '.docx':
        try:
            docxfile = docx2txt.process(path)
            words = docxfile
            return words
        except:
            raise Exception("Error reading .docx file")

    else:
        print(f'{path} is an unrecognized filetype')


def file_pipe(path: str) -> str:
    """
    The function called to take a filepath, and return wordcounts.
    For use in sqlite_funcs.
    """
    orig = Path(f'{path}'.format(r''))
    local = r"./temp_filestore/"
    Path(local).mkdir(exist_ok=True)
    copy = Path(local)
    
    ## File Move ##
    
    if orig.is_dir() is True:
        try:
            shutil.copytree(orig, copy)
        except:
            raise Exception("Error: shutil copy failed")
    else:
        try:
            shutil.copy2(orig, copy)
        except:
            raise Exception("Error: shutil copy failed")
    
    ## Filepull ##

    # Single File #
    if orig.is_dir() is False:
        words = filepull(copy.joinpath(orig.name))
    ## Multi-file ##
    else:
        list_words = [filepull(i) for i in copy.iterdir()]
        words = (" ").join(list_words)
    wc = wordcount(words)
    shutil.rmtree(copy)
    return wc


def wp_page_convert(words, wp_page):
    """
    Simple conversion from words to pages
    """
    pages = floor(words/wp_page)
    return pages


## Time Intelligence Funcs ##

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


def change_goal(goal_start_date, goal_end_date, word_goal=None, daily_target=None):
    """
    Takes daily_words_calculate and word_goal_calculate and combines them as one function
    """
    if (word_goal is not None) and (daily_target is None):
        goal = daily_words_calculate(word_goal, goal_start_date, goal_end_date)
        return goal
    elif (daily_target is not None) and (word_goal is None):
        goal = word_goal_calculate(daily_target, goal_start_date, goal_end_date)
        return goal
    elif (word_goal is not None) and (daily_target is not None):
        pass
    else:   
        raise Exception("Error: provide word_goal or daily_target, but not both.")


## Time Func ##

def streak_length(df_col):
    d_list = []
    for i in df_col:
            if i == 0:
                d = 0
            else:
                d += 1
            d_list.append(d)
    return d_list

def is_streak(i, count_col, target_col):
    
    if i == 0:
        return 0
    else: 
        pass
    if i == 0:
        pass
    elif (count_col.iloc[i] - count_col.iloc[i-1]) >= (target_col.iloc[i]): 
        return 1
    else:
        return 0