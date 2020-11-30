#######################################
################# URLs ################
####################################### 

from flask import render_template
from flask import request, redirect
from math import ceil
import datetime

from helper import load_projects_options, get_projects, get_project, get_current_project_id

from front_end import app


@app.route('/')
def index():
    # Get Current project
    current_project_id = int(get_current_project_id())
    current_project = get_project(current_project_id)

    wctoday = 0 # TODO: get today's word count
    daysleft = datetime.datetime.strptime(str(current_project["targetenddate"]),'%y%m%d') - datetime.datetime.today()
    daysleft = int(daysleft.days)
    wordsleft = current_project["targetwordcount"] - wctoday
    wctoday_suggested_target =  ceil(wordsleft / daysleft)

    return render_template('home.html', \
        pagetitle='Home', \
        projectname=current_project["name"], \
        WCtoday=wctoday, \
        wctoday_target= current_project["todaystargetwordcount"], \
        wctoday_suggested_target=wctoday_suggested_target, \
        current_project_id = current_project_id)

@app.route('/options')
def pg_options():
    projects = enumerate(get_projects()) 
    # NOTE: one of the below may be useful for the project end dates
    # datetime.datetime.strptime(project.targetenddate,'%y%m%d').strftime("%d-%b-%Y")
    # datetime.datetime.strptime(project.targetenddate,'%y%m%d').strftime("%d-%b-%Y")
    return render_template('options.html', pagetitle='Project Options', projects=projects)

@app.route('/stats')
def pg_stats():
    return render_template('stats.html', pagetitle='Stats')

@app.route('/charts')
def pg_charts():
    return render_template('charts.html', pagetitle='Charts')