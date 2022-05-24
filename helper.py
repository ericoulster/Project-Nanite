#######################################
########### Helper Functions ##########
#######################################

from wordcounter_funcs import wordmeta_pull, wordmeta_pull_all

# Get the ID for the current project
def get_current_project_id():
    #TODO: THIS IS A DUMMY FUNCTION
    #currentproject = request.cookies.get('currentproject')
    currentproject = False

    if not currentproject:
        currentproject = False

    return currentproject

# DEFUNCT: Get a dict of all projects
#def get_projects_dict(): # for all projects
    # TODO: defunct function??
    # Function [[receives JSON from API OR receives variables??]] and outputs as a dict
    
    #### IF USING JSON
    #response = get(url=f"{API_URL}/xxx") # this provides JSON, needs: from requests import get
    #projects = loads(response.content) # this converts it to a dict, ready for output
    ####

#    return projects

# Get a list of all projects
def get_projects_list():
    # Return list of projects using wordmeta_pull_all() (each project in the output list is a dict)

    wmpull = wordmeta_pull_all()
    projects = []

    for proj in wmpull.items():
        project  = { 
                    "name": proj[0],
                    "filepath": proj[1]['Project Path'],
                    "filetype": proj[1]['Filetype'],
                    "wordcountgoal": proj[1]['Wordcount Goal'],
                    "todaystargetwordcount": proj[1]['Daily Target'],
                    "targetstartdate": proj[1]['Start Date'],
                    "targetenddate": proj[1]['Deadline']
                    }
        projects.append(project)
        
    return projects # return an iterable list of projects (and their options)

# Get details of a project by its p_id (project ID number) or by its name (p_name)
def get_project(**kwargs):
    #Takes in either p_id (project id) or p_name (project name)
    project_notfound = {"name":"No Project: Create one now!","todaystargetwordcount":0}

    if 'p_id' in kwargs:
        # Uses p_id preferentially; checks for p_name if there's no p_id
        p_id = kwargs['p_id']
        if p_id is False: 
            # i.e. there is no project id
            return project_notfound
        else: 
            # If there is a current_project_id
            p_id = int(p_id)
            projects = get_projects_list()
            try:    
                project = projects[p_id] # returns a single project and its options
                return project
            except:
                return project_notfound
    elif 'p_name' in kwargs:
        p_name = kwargs['p_name']
        projects = get_projects_list()
        
        # check if project name is present in list of saved projects
        for project in projects:
            if project['name'] == p_name:
                return project # If there is a matching project name, return a single project and its options

        # If function hasn't returned by this point, then there's no matching project name
        return project_notfound
    else:
        return project_notfound

# Check if a parameter is in the submitted form data and return it; handle absence of parameter gracefully (return None)
def check_and_extract(parameter, formdata):
    if parameter in formdata:
        return formdata[parameter] 
    else:
        return None
