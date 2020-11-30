#######################################
#### API POSTS/PUTs/DELs/Cookies ######
#######################################

# Data is passed to the back end by the following functions

# NEEDED: API_URL

from front_end       import app
from flask           import jsonify, request, redirect, url_for, make_response
from requests        import get
from json            import loads


## Cookie for Current Project ##
@app.route('/current-project', methods = ['POST'])
def current_project_cookie():
    current_project_id = request.form['currentproject']

    # resp = make_response(render_template('home.html'))
    resp = make_response(redirect(request.referrer))
    resp.set_cookie('currentproject', current_project_id)

    return resp

## SINGLE PROJECTS ##

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

        #### DEBUGGING ####
        print('Function run: change_project_options: change details for a single existing project')
        #### ####
        return redirect(request.referrer)

@app.route('/project-options/<int:project_num>/del', methods=['POST'])
def delete_project_options(project_num): # for a single project 
    # TODO: delete a project

    #### DEBUGGING ####
    print(f"Function run: delete_project_options: delete project {str(project_num)}")
    #### ####
    return redirect(request.referrer)

## ALL PROJECTS ##
@app.route('/project-options', methods=['POST'])
def new_project(): # add a new project
    # NOTE: if using DB, use the Project class defined in api.__init__.py

    # pr_id = generate unique Project ID, either now or as part of saving process
    projectname = request.form['name']
    filepath = request.form['filepath']
    targetwordcount = request.form['targetwordcount']
    targetenddate = request.form['targetenddate']

    # TODO: SEND THESE TO BACK END

    #### DEBUGGING ####
    print(f"Function run: new_project: add a project. \n Submitted values: {projectname} | {filepath} | {targetwordcount} | {targetenddate}")
    #### ####
    return redirect(url_for('pg_options'))

