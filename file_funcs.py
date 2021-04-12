import string
from datetime import date, datetime
from math import ceil
import re

from striprtf.striprtf import rtf_to_text
import docx2txt

r = re.compile(r'\w+')

punctuation_strip = str.maketrans('', '', string.punctuation)

# input is words, returns a wordcount
def wordcount(content: str) -> int:
    filetoken = content.translate(punctuation_strip).split(' ')
    wordcount = list(filter(r.match, filetoken))
    return len(wordcount)

def path_parser(path: str) -> str:
    """
    Takes in path, returns filetype
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

