#######################################
########### Helper Functions ##########
#######################################

from api import load_projects_options

def get_projects():
   projects = load_projects_options()
   projects = projects.values()

   return list(projects) # return an iterable list of projecs (and their options)

def get_project(p_id):
    projects = get_projects()
    return projects[p_id] # returns a single project and its options

