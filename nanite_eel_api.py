import eel
from sqlite_funcs import *

# Exposing Class Sqlite Funcs to Eel ##

@eel.expose
def new_author(authorname):
    create_author(authorname)

@eel.expose
def new_project(authorname, projectname, targetstartdate , targetenddate, wordcountgoal, current_daily_target, wp_page, projectpath):
    #print(authorname, projectname, targetstartdate , targetenddate, wordcountgoal, current_daily_target, wp_page, projectpath)
    
    a = AuthorActions()
    a.id_by_name(authorname)
    a.create_project(projectname, targetstartdate , targetenddate, wordcountgoal, current_daily_target, wp_page, projectpath)

    # Samples
    # a.id_by_name('Johnny')
    # a.create_project("Johnny's Other Manifesto", '2020-04-24', '2020-06-20', '15000', '400', '400', r'D:\Documents\Datasets\001. ML Projects\Wordcount v2\Git Project\Johnnys Manifesto.txt')


# Exposing 'Top Level' Sqlite Funcs to Eel ##

@eel.expose
def eel_return_author_list():
    """
    Prints all authors as a list of dicts
    """
    return return_author_list()

    
@eel.expose
def eel_create_author(author_name, password=''):    
    """ 
    Inserts an Author into database if they don't exist.
    If they do, this task does not go through. 
    """
    return create_author(author_name, password)

@eel.expose
def eel_return_project_screen(author_id:int) -> list(dict()):
    """
    Returns all the values needed for the Projects page, each 'div' as an individual dict.
    Needs to be tested on entries without a table.
    """
    return return_project_screen(author_id)

@eel.expose
def eel_return_projects_by_name(author_name:str) -> list(dict()):
    a = AuthorActions()
    a.id_by_name(author_name)
    return a.return_projects()