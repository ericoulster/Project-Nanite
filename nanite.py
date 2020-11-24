from flask import Flask, render_template, request, redirect
from helper import load_projects_options, get_projects
from views import current_project_id, current_project
from math import ceil

app = Flask(__name__)

#######################################
############ API ENDPOINTS ############
#######################################
import datetime
from flask import jsonify, request

## TEST API ENDPOINT (JSON) ##
@app.route('/info', methods=['GET'])
def get_info():
  info = \
    {
      'name'        : 'project-nanite-api'
      , 'version'   : '1.0.0.'
      , 'date_time' : datetime.datetime.now()
    }
 
  return jsonify(info)
## END TEST ##

## SINGLE PROJECTS ##

@app.route('/project-options/<int:project_num>', methods=['GET'])
def load_project_options(project_num): # for a single project: !! not needed if using GET on all project-options !!
    # TODO
    return ('Not implemented yet')

@app.route('/project-options/<int:project_num>', methods=['PUT'])
def change_project_options(project_num): # for a single project

    wc_target_today = request.form['wctoday_target_new'] # these variables might or might not have values depending on which form is filled to update a record (home page or options page)

    # TODO
    return ('Not implemented yet')

@app.route('/project-options/<int:project_num>', methods=['DELETE'])
def delete_project_options(project_num): # for a single project 
    # TODO
    return ('Not implemented yet')

## ALL PROJECTS ##

@app.route('/project-options', methods=['GET'])
def load_projects_options_api(json_out=True): # for all projects
    # TODO: function outputs a JSON object that will become an iterable list of projects (currently outputs a dict)

    projects = load_projects_options()

    return projects

    # TODO if JSON is implemented, use:
    # if json_out:
    #     return jsonify(projects)
    # else:
    #     return projects

@app.route('/project-options', methods=['POST'])
def new_project(): # add a new project
    # NOTE: if using DB, use the Project class defined in api.__init__.py

    pr_id = len(load_projects_options(json_out=False))
    projectname = request.form['name']
    filepath = request.form['filepath']
    targetwordcount = request.form['targetwordcount']
    targetenddate = request.form['targetenddate']

    # TODO: SEND THESE TO BACK END
    # return redirect('/')
    return f"Submitted values: {pr_id} | {projectname} | {filepath} | {targetwordcount} | {targetenddate}"

#######################################
################# URLs ################
####################################### 

@app.route('/')
def index():
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

if __name__ == '__main__':
    # app.run()
    app.run(host='127.0.0.1', port=5000, debug=True)