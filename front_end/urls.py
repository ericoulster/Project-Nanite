#######################################
################# URLs ################
####################################### 

from flask        import render_template
from flask        import request, redirect, url_for, make_response
from math         import ceil
from datetime     import datetime

from wordcounter_funcs import wordmeta_set, wordcount, filepull, wordcount_update, project_delete, wordmeta_rename, wordmeta_pull
from helper            import get_projects_list, get_projects_list, get_project, get_current_project_id, check_and_extract
from front_end         import app

#### CONTEXT PROCESSORS ####
@app.context_processor
def inject_menu_info():
    username = request.cookies.get('currentuser')
    if username is None:
        username = 'Writer'
    return dict(menuprojects=enumerate(get_projects_list()) \
        , username = username \
            , overall_total_words_written = 0 \
                , streak_length = 0 \
                    , weekday_most_writing = "---") #TODO get this information for the menu

#### ROUTES ####
@app.route('/')
def index():
    return render_template('home.html', pagetitle='Home')

@app.route('/options', methods=['GET','POST'])
def pg_options():
    if request.method == 'GET':
        projects = enumerate(get_projects_list()) # This is still needed, as context processor is 'used up' on menu
        # NOTE: one of the below may be useful for the project end dates
        # datetime.strptime(project.targetenddate,'%y%m%d').strftime("%d-%b-%Y")
        # datetime.strptime(project.targetenddate,'%y%m%d').strftime("%d-%b-%Y")

        WCtoday = 0 # TODO: get today's word count and overall total for a project (get a list of these to iterate over in the template)
        WCtotal = 0

        return render_template('options.html', pagetitle='Project Options', projects=projects, WCtoday=WCtoday, WCtotal=WCtotal)

    elif request.method == 'POST': 
    # Add a new project
    # NOTE: if using DB, use the Project class defined in api.__init__.py
        #pr_id = datetime.now().strftime("%y%m%d%H%M%S%f")
        projectname = request.form['name']
        filepath = request.form['filepath']
        filetype = request.form['filetype']
        targetwordcount = request.form['targetwordcount']
        targetenddate = request.form['targetenddate']

        # SEND THESE TO BACK END
        # wordmeta_set(pr_id, projectname, targetwordcount, filepath, filetype, targetenddate)
        wordmeta_set(projectname, targetwordcount, filepath, filetype, targetenddate)

        ## DEBUGGING ##
        # print(f"Function run: new_project: add a project. \n Submitted values: {pr_id} | {projectname} | {filepath} | {targetwordcount} | {targetenddate}")
        print(f"Function run: new_project: add a project. \n Submitted values: {projectname} | {filepath} | {targetwordcount} | {targetenddate}")
        ## ##
        return redirect(url_for('pg_options'))

@app.route('/welcome', methods=['GET','POST'])
def pg_welcome():
    if request.method == 'GET':
        return render_template('welcome.html', pagetitle='Welcome')
    if request.method == 'POST': # TODO: Collect and store username
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
    #NOTE: project_num is available for use here, if updating by project ID instead of name

    if request.method == 'POST':
        # First off: Update the word count
        projectname = check_and_extract('name', request.form)
        project = get_project(p_name = projectname) # search for project
        dailywords= wordcount(filepull(project['filepath'], filetype='txt', isDirectory=False))
        wordcount_update(projectname, dailywords)
        
        # Then, check if anything else needs changing (via the form submission)
        pr_id = check_and_extract('projectid', request.form)
        filepath = check_and_extract('filepath', request.form)
        filetype = check_and_extract('filetype', request.form)
        targetwordcount = check_and_extract('targetwordcount', request.form)
        targetenddate = check_and_extract('targetenddate', request.form)
        
        if (projectname is not None) and (filepath is not None): # AND the others?
            # SEND THESE TO BACK END
            # TODO: this function currently just adds a new row, rather than updating the existing one
            # wordmeta_set(pr_id, projectname, targetwordcount, filepath, filetype, targetenddate)
            wordmeta_set(projectname, targetwordcount, filepath, filetype, targetenddate)

        ## DEBUGGING ##
        print('Function run: change_project_options: change details for a single existing project\n')
        print(f'Submitted Values: {pr_id} | {projectname} | {filepath} | {filetype} | {targetwordcount} | {targetenddate}')
        ## ##
        return redirect(request.referrer)

@app.route('/project-options/<int:project_num>/del', methods=['POST'])
def delete_project_options(project_num): # Delete a single project 
    projectname = check_and_extract('name', request.form)
    project_delete(projectname)

    ## DEBUGGING ##
    print(f"Function run: delete_project_options: delete project: {str(project_num)} | {projectname}")
    ## ##
    return redirect(request.referrer)

@app.route('/project-options/<int:project_num>/ren', methods=['POST'])
def rename_project(project_num): # Rename a single project 
    projectname = check_and_extract('name', request.form)
    new_name = check_and_extract('newname', request.form)
    wordmeta_rename(projectname, new_name)

    ## DEBUGGING ##
    print(f"Function run: rename_project: rename project: {str(projectname)} | {new_name}")
    ## ##
    return redirect(request.referrer)

@app.route('/stats-single')
def pg_single_stats():
    # Get Current project
    current_project_id = get_current_project_id() #returns a full string, or False
    current_project = get_project(p_id = current_project_id) #if current_project_id is False, will return dummy text
    
    if current_project_id is False: # i.e. there is no current_project_id
        wctoday = 0
        wctoday_suggested_target = 0
    else: # If there is a current_project_id
        current_project_id = int(current_project_id)

        wctoday = 0 # TODO when it becomes possible to get meta: wordcount(filepull(current_project['filepath'], filetype='txt', isDirectory=False))
        daysleft = datetime.strptime(str(current_project["targetenddate"]),'%y%m%d') - datetime.today()
        daysleft = int(daysleft.days)
        wordsleft = current_project["targetwordcount"] - wctoday
        wctoday_suggested_target =  ceil(wordsleft / daysleft)

    return render_template('stats-single.html', \
        pagetitle=current_project["name"] + ' Stats', \
        projectname=current_project["name"], \
        WCtoday=wctoday, \
        wctoday_target= current_project["todaystargetwordcount"], \
        wctoday_suggested_target=wctoday_suggested_target, \
        current_project_id = current_project_id)

#### Cookie for Current Project ####

@app.route('/current-project', methods = ['POST'])
def current_project_cookie():
    current_project_id = request.form['currentproject']

    # resp = make_response(render_template('home.html'))
    resp = make_response(redirect(request.referrer))
    resp.set_cookie('currentproject', current_project_id)

    return resp

@app.route('/current-user', methods = ['POST'])
def current_user_cookie():
    current_username = request.form['username']

    # resp = make_response(render_template('home.html'))
    resp = make_response(redirect(request.referrer))
    resp.set_cookie('currentuser', current_username)

    return resp
