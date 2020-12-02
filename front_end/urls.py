#######################################
################# URLs ################
####################################### 

from flask        import render_template
from flask        import request, redirect, url_for, make_response
from math         import ceil
from datetime     import datetime

from wordcounter_funcs import wordmeta_set, wordcount, filepull
from helper            import load_projects_options, get_projects, get_project, get_current_project_id
from front_end         import app


@app.route('/')
def index():
    # Get Current project
    current_project_id = int(get_current_project_id())
    current_project = get_project(current_project_id)

    wctoday = 0 # TODO when it becomes possible to get meta: wordcount(filepull(current_project['filepath'], filetype='txt', isDirectory=False))
    daysleft = datetime.strptime(str(current_project["targetenddate"]),'%y%m%d') - datetime.today()
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

@app.route('/options', methods=['GET','POST'])
def pg_options():
    if request.method == 'GET':
        projects = enumerate(get_projects()) 
        # NOTE: one of the below may be useful for the project end dates
        # datetime.strptime(project.targetenddate,'%y%m%d').strftime("%d-%b-%Y")
        # datetime.strptime(project.targetenddate,'%y%m%d').strftime("%d-%b-%Y")
        return render_template('options.html', pagetitle='Project Options', projects=projects)

    elif request.method == 'POST': 
    # Add a new project
    # NOTE: if using DB, use the Project class defined in api.__init__.py
        pr_id = datetime.now().strftime("%y%m%d%H%M%S%f")
        projectname = request.form['name']
        filepath = request.form['filepath']
        filetype = request.form['filetype']
        targetwordcount = request.form['targetwordcount']
        targetenddate = request.form['targetenddate']

        # SEND THESE TO BACK END
        wordmeta_set(pr_id, projectname, targetwordcount, filepath, filetype, targetenddate)

        ## DEBUGGING ##
        print(f"Function run: new_project: add a project. \n Submitted values: {pr_id} | {projectname} | {filepath} | {targetwordcount} | {targetenddate}")
        ## ##
        return redirect(url_for('pg_options'))

@app.route('/stats')
def pg_stats():
    return render_template('stats.html', pagetitle='Stats')

@app.route('/charts')
def pg_charts():
    return render_template('charts.html', pagetitle='Charts')


#### CHANGES TO INDIVIDUAL PROJECTS ####

@app.route('/project-options/<int:project_num>', methods=['POST'])
def change_project_options(project_num): # for a single project
    if request.method == 'POST':
        
        # These variable might or might not have values depending on which form is filled to update a record (home page or options page)
        # TODO: HANDLE THIS

        wc_target_today = request.form['wctoday_target_new'] 
        projectname = request.form['name']
        filepath = request.form['filepath']
        targetwordcount = request.form['targetwordcount']
        targetenddate = request.form['targetenddate']

        # TODO: change details for a single existing project

        ## DEBUGGING ##
        print('Function run: change_project_options: change details for a single existing project')
        ## ##
        return redirect(request.referrer)

@app.route('/project-options/<int:project_num>/del', methods=['POST'])
def delete_project_options(project_num): # for a single project 
    # TODO: delete a project

    ## DEBUGGING ##
    print(f"Function run: delete_project_options: delete project {str(project_num)}")
    ## ##
    return redirect(request.referrer)

#### Cookie for Current Project ####
@app.route('/current-project', methods = ['POST'])
def current_project_cookie():
    current_project_id = request.form['currentproject']

    # resp = make_response(render_template('home.html'))
    resp = make_response(redirect(request.referrer))
    resp.set_cookie('currentproject', current_project_id)

    return resp
