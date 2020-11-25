#######################################
########## API CALLS/POSTS ############
#######################################

# Calls to the API are made and requests received are converted for use by Flask by the following functions
# Data is passed to the back end by the following functions

# NEEDED: API_URL

from front_end       import app
from flask           import jsonify, request
from requests        import get
from json            import loads


from api.sample_data import dummy_projects

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
#@app.route('/project-options', methods=['GET'])
def load_projects_options(): # for all projects
    # Function receives JSON from API and outputs it as a dict
    
    #response = get(url=f"{API_URL}/project-options") # this provides JSON
    #projects = loads(response.content) # this converts it to a dict, ready for output

    projects = dummy_projects() # keeping the dummy for testing purposes

    return projects

@app.route('/project-options', methods=['POST'])
def new_project(): # add a new project
    # NOTE: if using DB, use the Project class defined in api.__init__.py

    # pr_id = generate unique Project ID, either now or as part of saving process
    projectname = request.form['name']
    filepath = request.form['filepath']
    targetwordcount = request.form['targetwordcount']
    targetenddate = request.form['targetenddate']

    # TODO: SEND THESE TO BACK END
    # return redirect('/')
    return f"Submitted values: {projectname} | {filepath} | {targetwordcount} | {targetenddate}"
