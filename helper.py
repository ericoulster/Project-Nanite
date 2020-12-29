#######################################
########### Helper Functions ##########
#######################################

from flask             import request

from wordcounter_funcs import wordmeta_pull, wordmeta_pull_all
from sample_data       import dummy_projects

def get_current_project_id():
    currentproject = request.cookies.get('currentproject')

    if not currentproject:
        currentproject = False

    return currentproject


def get_projects_dict(): # for all projects
    # TODO: defunct function??
    # Function [[receives JSON from API OR receives variables??]] and outputs as a dict
    
    #### IF USING JSON
    #response = get(url=f"{API_URL}/xxx") # this provides JSON
    #projects = loads(response.content) # this converts it to a dict, ready for output
    ####

    #### Reading from CSV using wordcounter_funcs below

    projects = dummy_projects() # keeping the dummy for testing purposes

    # out = wordmeta_pull('Alice in Project Land')
    # print(out)
    # RETURNS: {'Filetype': {'Alice in Project Land': 'txt'}, 'Latest Target': {'Alice in Project Land': 2000}, 'Project Path': {'Alice in Project Land': 'C:/Dummy/File/Path.txt'}, 'Deadline': {'Alice in Project Land': 210331}}
    # TODO: ?????

    return projects

def get_projects_list():
    # Return list of projects using wordmeta_pull_all() (each project in the output list is a dict)

    ## Defunct? ##
    #projects = get_projects_dict()
    #projects = projects.values()
    ## ##

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

def get_project(**kwargs):
    #Takes in either p_id (project id) or p_name (project name)
    project_notfound = {"name":"No Project: Create one now!","todaystargetwordcount":0}

    if 'p_id' in kwargs:
        p_id = kwargs['p_id']
        if p_id is False: # i.e. there is no project id
            return project_notfound
        else: # If there is a current_project_id
            p_id = int(p_id)
            projects = get_projects_list()
            try:    
                project = projects[p_id] # returns a single project and its options
                return project
            except:
                return project_notfound
    elif 'p_name' in kwargs:
        # TODO: add finding project by name
        p_name = kwargs['p_name']
        projects = get_projects_list()
        
        # check if project name is present in list of saved projects
        p_name_present = False
        for project in projects:
            if project['name'] == p_name:
                p_name_present = True
                break

        if not p_name_present: # i.e. no matching project name
            return project_notfound
        else: # If there is a matching project name
            return project # returns a single project and its options
    else:
        return project_notfound

def check_and_extract(parameter, formdata):
    if parameter in formdata:
        return formdata[parameter] 
    else:
        return None
