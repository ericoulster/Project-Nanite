from flask        import render_template
from flask        import request, redirect, url_for, make_response, Markup
from math         import ceil
from datetime     import datetime

from wordcounter_funcs import wordmeta_set, wordcount, filepull, wordcount_update, project_delete, wordmeta_rename, wordmeta_pull, wordmeta_pull_all, daily_words_calculate, word_goal_calculate, wordcount_pull, get_sidepane_info, wordstreak, wordcount_last_day
from helper            import get_projects_list, get_projects_list, get_project, get_current_project_id, check_and_extract
from front_end         import app

#### CONTEXT PROCESSORS ####
@app.context_processor
def inject_menu_info():
    username = request.cookies.get('currentuser')
    p_id = get_current_project_id()
    current_project_name = get_project(p_id = p_id)["name"]

    if p_id == False:
        info = {'words written':0, "day longest streak":0, "You write most on":'---'}
    else:
        try: #TODO: fix this! had to do this to make the app usable when get_sidepane_info returns the indexing error
            info = get_sidepane_info(current_project_name)
        except:
            info = {'words written':0, "day longest streak":0, "You write most on":'---'}

    if (username is None) or (username == ''):
        username = 'Writer'
    return dict(menuprojects=enumerate(get_projects_list()) \
        , projectname = current_project_name \
            , username = username \
                , overall_total_words_written = info['words written'] \
                    , streak_length = info['day longest streak'] \
                        , weekday_most_writing = info['You write most on']) #TODO get this information across projects?

#### ROUTES ####

#@app.route('/test')
#def test():
    #return render_template('modaltest.html', pagetitle='Test' )
    #return ""

@app.route('/')
def index():
    return render_template('home.html', pagetitle='Home')

@app.route('/projects', methods=['GET','POST'])
def pg_projects():
    if request.method == 'GET':
        projectslist = get_projects_list() # This is still needed, as context processor is 'used up' on menu
        projects = enumerate(get_projects_list())
        
        hasprojects = True if projectslist else False # check if this has projects and pass on
        
        # NOTE: one of the below may be useful for the project end dates
        # datetime.strptime(project.targetenddate,'%y%m%d').strftime("%d-%b-%Y")
        # datetime.strptime(project.targetenddate,'%y%m%d').strftime("%d-%b-%Y")

        WCtoday = []
        WCprojtotal = []

        # TODO: test this script below
        for project in projectslist:
            try:
                isDirectory = not project['filepath'].split(".")[-1]==project['filetype']    
                # isDirectory = not project['filepath'][-3:]==project['filetype'] #TODO: refine? This is detecting if this is a directory (or a file) by comparing the end of the file path to the filetype
                wc = wordcount(filepull(project['filepath'], project['filetype'], isDirectory)) #  #TODO pick up directory (or not) from project
                wc_pull = wordcount_pull(project['name'])
                WCprojtotal.append(wc)
            except:
                pass # TODO error handle this

            try:
                wclastsession = wc_pull[-1]['Session Wordcount'] #TODO: This is the wordcount from last session. Should be today?
            except:
                wclastsession = 0
            
            WCtoday.append(wclastsession)

        return render_template('projects.html', pagetitle='Projects', hasprojects=hasprojects, projects=projects, WCtoday=WCtoday, WCtotal=WCprojtotal)

    elif request.method == 'POST': 
    # Add a new project
        #pr_id = datetime.now().strftime("%y%m%d%H%M%S%f")
        projectname = request.form['name']
        filepath = request.form['filepath']
        filetype = request.form['filetype']
        targetstartdate = request.form['targetstartdate']
        targetenddate = request.form['targetenddate']
        wordcountreg = request.form['wordcountreg']

        if wordcountreg == 'daily': 
            dailytarget = request.form['wordcountgoal']
            wordcountgoal = word_goal_calculate(dailytarget, targetstartdate, targetenddate)
        elif wordcountreg == 'total':
            wordcountgoal = request.form['wordcountgoal']
            dailytarget = daily_words_calculate(wordcountgoal, targetstartdate, targetenddate)
        else:
            pass # ERROR #TODO handle this

        # SEND THESE TO BACK END
        isDirectory = not filepath.split(".")[-1]==filetype #TODO: refine? This is detecting if this is a directory (or a file) by comparing the end of the file path to the filetype
        wc = wordcount(filepull(filepath, filetype, isDirectory))
        #TODO: 1. Check if there is a file first?  2. pick up if directory (or not) from project filepath directly
        
        wordmeta_set(projectname, dailytarget, filepath, filetype, targetstartdate, targetenddate, wordcountgoal)  
        wordcount_update(name = projectname, wordcount = wc)
        return redirect(url_for('pg_projects'))

@app.route('/welcome', methods=['GET'])
def pg_welcome():
    if request.method == 'GET':
        return render_template('welcome.html', pagetitle='Welcome')

@app.route('/how-nanite-works', methods=['GET'])
def pg_instructions():
    if request.method == 'GET':
        return render_template('how-nanite-works.html', pagetitle='How Nanite Works')

@app.route('/projects/<int:project_num>', methods=['GET'])
def pg_stats(project_num):
    if request.method == 'GET':
        project = get_project(p_id=project_num)
        streak = wordstreak(project['name'])
        lastwc = wordcount_last_day(project['name'])
        try:
            isDirectory = not project['filepath'].split(".")[-1]==project['filetype'] #TODO: refine? This is detecting if this is a directory (or a file) by comparing the end of the file path to the filetype
            wc = wordcount(filepull(project['filepath'], project['filetype'], isDirectory)) #  #TODO pick up directory (or not) from project filepath
        except:
            wc = 0
            pass # TODO error handle this
        print(project)
        return render_template('stats.html', pagetitle='Stats', project = project, WCtotal = wc, streak = streak, lastWordCount = lastwc)

@app.route('/charts')
def pg_charts():
    return render_template('charts.html', pagetitle='Charts')


## INDIVIDUAL PROJECTS: get details/make changes ##

@app.route('/project-options/<int:project_num>', methods=['POST'])
def change_project_options(project_num): # for a single project
    #NOTE: project_num is available for use here, if updating by project ID instead of name
    projectname = dailytarget = filepath = filetype = targetstartdate = targetenddate = wordcountgoal = None

    if request.method == 'POST':

        # First off: Try to update the word count
        projectname = check_and_extract('name', request.form)
        project = get_project(p_name = projectname) # search for project
        isDirectory = not project['filepath'].split(".")[-1]==project['filetype'] #TODO: refine? This is detecting if this is a directory (or a file) by comparing the end of the file path to the filetype
        try:
            dailywords= wordcount(filepull(project['filepath'], project['filetype'], isDirectory)) 
            wordcount_update(projectname, dailywords)
        except:
            pass # ERROR #TODO handle this
        
        # Then, check if anything else needs changing (via the form submission)
        pr_id = check_and_extract('projectid', request.form)
        filepath = check_and_extract('filepath', request.form)
        filetype = check_and_extract('filetype', request.form)
        targetstartdate = check_and_extract('targetstartdate', request.form)
        targetenddate = check_and_extract('targetenddate', request.form)
        wordcountreg = check_and_extract('wordcountreg', request.form)

        if wordcountreg == 'daily': 
            dailytarget = request.form['wordcountgoal']
            wordcountgoal = word_goal_calculate(dailytarget, targetstartdate, targetenddate)
        elif wordcountreg == 'total':
            wordcountgoal = request.form['wordcountgoal']
            dailytarget = daily_words_calculate(wordcountgoal, targetstartdate, targetenddate)
        else:
            pass # ERROR #TODO handle this

        if all(v is not None for v in [projectname, dailytarget, filepath, filetype, targetstartdate, targetenddate, wordcountgoal]):
            # Send to back end
            wordmeta_set(projectname, dailytarget, filepath, filetype, targetstartdate, targetenddate, wordcountgoal)

        return redirect(request.referrer)

@app.route('/project-options/<int:project_num>/del', methods=['POST'])
def delete_project_options(project_num): # Delete a single project 
    projectname = check_and_extract('name', request.form)
    project_delete(projectname)
    return redirect(request.referrer)

@app.route('/project-options/<int:project_num>/ren', methods=['POST'])
def rename_project(project_num): # Rename a single project 
    projectname = check_and_extract('name', request.form)
    new_name = check_and_extract('newname', request.form)
    wordmeta_rename(projectname, new_name)
    return redirect(request.referrer)

@app.route('/stats-single', methods=['GET'])
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
        wordsleft = current_project["wordcountgoal"] - wctoday
        wctoday_suggested_target =  ceil(wordsleft / daysleft)

    return render_template('stats-single.html', \
        pagetitle=current_project["name"] + ' Stats', \
        projectname=current_project["name"], \
        WCtoday=wctoday, \
        wctoday_target= current_project["dailytarget"], \
        wctoday_suggested_target=wctoday_suggested_target, \
        current_project_id = current_project_id)

#### Cookies for Current User and Current Project ####

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

    resp = make_response(redirect(url_for('pg_projects')))
    resp.set_cookie('currentuser', current_username)

    return resp
