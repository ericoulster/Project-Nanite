import string
from datetime import date, datetime
from math import ceil
import re
from pathlib import Path

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




### TO EDIT ###:
# Switch to using Pathlib instead of os.path (will also replace glob functions)
def filepull(project_path: str, filetype='txt': str, is_folder=False: bool) -> str:
    # assigning to a raw string
    project_path = r'{}'.format(project_path)

    
    if is_folder is False:
        
        if filetype == '.txt':
            try:
                filepath = Path(project_path)
                with open(filepath, "r", encoding='utf8') as file:
                    return file.read()
            except:
                print("txt file failed to be read")
            
        elif filetype == '.rtf':
            try:
                filepath = Path(project_path)
                with open(filepath, "r", encoding='utf8') as file:
                    rtf_file = file.read()
                    clean_file = rtf_to_text(rtf_file)
                    return clean_file
            except:
                print("rtf file failed to be read")
                
        elif filetype == '.docx':
            try:
                filepath = Path(project_path)
                file = docx2txt.process(filepath)
                return file
            except:
                print("docx file failed to be read")
        else:
            print("error: filepull only accepts 'txt', 'rtf', & 'docx' filetypes")
        
    if is_folder is True:
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