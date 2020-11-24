#######################################
########### Helper Functions ##########
#######################################

def load_projects_options(json_out=True): # for all projects
    # TODO: function outputs a JSON object that will become an iterable list of projects (currently outputs a dict)
    
    # Dummy below for testing
    dummy_project = {
        "name": "Dummy Project Name",
        "filepath": "C:/Dummy/File/Path.txt",
        "targetwordcount": 20000,
        "todaystargetwordcount": 1000,
        "targetenddate": 210331 #31st March 2021 
    }
    projects = {"0": dummy_project}

    return projects

def get_projects():
   projects = load_projects_options()
   projects = projects.values()

   return list(projects) # return an iterable list

def get_project(p_id):
    projects = get_projects()
    return projects[p_id]

