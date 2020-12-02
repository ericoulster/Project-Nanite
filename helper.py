#######################################
########### Helper Functions ##########
#######################################

from flask           import request

from sample_data     import dummy_projects

def get_current_project_id():
    currentproject = request.cookies.get('currentproject')

    if not currentproject:
        currentproject = 0

    return currentproject


def load_projects_options(): # for all projects
    # Function [[receives JSON from API OR receives variables??]] and outputs as a dict
    
    #### IF USING JSON
    #response = get(url=f"{API_URL}/xxx") # this provides JSON
    #projects = loads(response.content) # this converts it to a dict, ready for output
    ####

    #### Reading from CSV using wordcounter_funcs below

    projects = dummy_projects() # keeping the dummy for testing purposes

    return projects

def get_projects():
   projects = load_projects_options()
   projects = projects.values()

   return list(projects) # return an iterable list of projecs (and their options)

def get_project(p_id):
    projects = get_projects()
    return projects[p_id] # returns a single project and its options
