import eel
from sqlite_funcs import *

@eel.expose
def new_author(authorname):
    create_author(authorname)

@eel.expose
def new_project(authorname, projectname, targetstartdate , targetenddate, wordcountgoal, current_daily_target, wp_page, projectpath):
    a = AuthorActions()
    a.id_by_name(authorname)
    a.create_project(projectname, targetstartdate , targetenddate, wordcountgoal, current_daily_target, wp_page, projectpath)

    # Samples
    # a.id_by_name('Johnny')
    # a.create_project("Johnny's Other Manifesto", '2020-04-24', '2020-06-20', '15000', '400', '400', r'D:\Documents\Datasets\001. ML Projects\Wordcount v2\Git Project\Johnnys Manifesto.txt')