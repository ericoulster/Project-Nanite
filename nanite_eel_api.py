import eel
from sqlite_funcs import *
from jinja2 import Template

@eel.expose
def eel_return_wordcounts(project_id):
    p = ProjectActions()
    p = p.set_project(project_id)
    return p.return_wordcounts('D')

@eel.expose
def get_author_id(authorname):
    a = AuthorActions()
    a.id_by_name(authorname)
    authorinfo = a.return_info()

    if 'author_id' in authorinfo:
        return authorinfo['author_id']
    else:
        return None

@eel.expose
def list_projects_html(username):
    # Jinja template with for loop (for x amount of projects, which also can be input)
    # This passes the complete html into the javascript as a string for rendering (with DOMParser), for quick prototyping

    author_id = get_author_id(username)
    projects = return_project_screen(author_id)
    # Sample returned: [{'project_name': "Johnny's Manifesto", 'project_id': 1.0, 'daily_words': 700.0, 'today_goal': 1000.0, 'total_progress': 23700.0, 'current_streak': 0}, {'project_name': "Johnny's Other Manifesto", 'project_id': 2, 'daily_words': 0, 'today_goal': 0, 'total_progress': 0, 'current_streak': 0}]

    # Debugging
    # print(projects)

    #convert floats to ints
    for p in projects:
        for k,v in p.items():
            if type(v)==float:
                p[k]=int(v)

    project_ids = [int(p['project_id']) for p in projects] # list project ids
    projects_zip = zip(project_ids, projects) # zip for looping

    t = Template("""{% for idx, project in projects %}
    <article id="project-{{idx}}" class="projects-item" data-pid="{{ project.project_id }}">
      <div id="project-{{idx}}-summary" class="project-summary panels">
        <div class="header panel">
            <h2>{{ project.project_name }}</h2>
            <div class="project-header-buttons">
                <div class="proj-nav-icon">
                    <a class="edit-project icon" href="#" onclick="showEditProjectModal({{idx}})"><img src="../static/imgs/icons/pencil.svg"></a>
                    <span class="optionExplanation">Edit Project</span>
                </div>
                <div class="proj-nav-icon">
                    <a class="download-project icon" href="#" onclick="showCSVExportModal({{idx}})"><img src="../static/imgs/icons/download.svg"></a>
                    <span class="optionExplanation">Export to CSV</span>
                </div>
                <div class="proj-nav-icon">
                    <a class="del-project icon" href="#" onclick="delete_project(get_username(),'{{ project.project_name }}')"><img src="../static/imgs/icons/trash.svg"></a>
                    <span class="optionExplanation">Delete Project</span>
                </div>
            </div>
        </div>
        <div class="progress panel"><label for="project-progress">Today's Progress:</label>
            <div class="progress-{{idx}}" data-pid="{{ project.project_id }}" data-todaywords="{{ project.daily_words }}" data-todaygoal="{{ project.today_goal }}"></div>
        </div>
        <div class="quickstats panel">
          <p>Total Progress: {{ project.total_progress }}</p>
          <p>Current Streak: {{ project.current_streak }}</p>
        </div>
        <div class="actions panel">
          <a onclick="showStatsModal({{project.project_id}})" class="btn">Project Stats</a>
          <a onclick="refresh_wordcounts({{project.project_id}})" class="btn">Refresh Project</a>
        </div>
      </div>
    </article>
  {% endfor %}""")


## PREVIOUS TEMPLATE - for dev

    # SAMPLE DATA EXPECTED BY THE TEMPLATE
    #projects2 = [{'name':'Sample Name', 'wordcountgoal':4000,'targetstartdate':'2021-01-01','targetenddate':'2021-07-01','filepath':'C:/Dummy/File/Path','filetype':'txt'},{'name':'Second P Name', 'wordcountgoal':7000,'targetstartdate':'2021-01-07','targetenddate':'2021-07-07','filepath':'D:/Dummy/File/Path','filetype':'docx'}]  
    #WCtotal = [3000,5000]
    
#     t = Template("""{% for idx, project in projects %}
#     <div id="project-{{idx}}" class="projects-item">
#       <div id="project-{{idx}}-summary" class="project-summary panels">
#         <div class="panel"><h2>{{ project.name }}</h2></div>
#         <div class="panel"><label for="project-progress">Writing Goal: {{project.wordcountgoal}} Total Words</label>
#           <progress id="project-progress" value="{{WCtotal[idx]}}" max="{{project.wordcountgoal}}"> {{WCtotal[idx] / project.wordcountgoal}} </progress><p> <span class="progress-to-goal">{{WCtotal[idx]}} / {{project.wordcountgoal}}</span> <span class="last-update hidden">Last Update: No Update Yet!</span> </p>
#         </div>
#         <div class="panel">
#           <p>Start Date: {{ project.targetstartdate }}</p>
#           <p>Finish Date: {{ project.targetenddate }}</p>
#           <button onclick="pm = document.querySelector('#project-{{idx}}-more').classList.toggle('hidden');">More...</button>
#         </div>
#       </div>
#       <div id="project-{{idx}}-more" class="project-summary-more panels hidden">
#        <form id="project-{{idx}}-form" action="/project-options/{{idx}}" method="POST" class="project-form existing-project">
#         <div class="formfields">
#           <fieldset> 
#               <legend>Setup</legend>
#                 <input type="text" name="projectid" value="{{idx}}" class="formfield" hidden required disabled>
#                 <input type="text" name="name" value="{{ project.name }}" class="formfield" hidden required disabled>
#                 <label>File/folder Path:</label><input type="text" name="filepath" value="{{ project.filepath }}" class="formfield" required disabled><br/>
#                 <label>Files of type:</label>
#                   <select name="filetype" class="formfield" required disabled>
#                     <option value="" selected hidden>{{ project.filetype }}</option>
#                     <option value="txt">txt</option>
#                     <option value="rtf">rtf</option>
#                     <option value="docx">docx</option>
#                   </select><br/>
#           </fieldset>
#           <fieldset> 
#             <legend>Goals</legend>
#                 <label>Word Count Goal:</label><input type="text" name="wordcountgoal" value="{{ project.wordcountgoal }}" class="formfield" required disabled> words
#                 <div class="regularity selection" style="display:inline-block;">
#                   <input type="radio" id="daily-{{idx}}" name="wordcountreg" value="daily" class="formfield" required disabled>
#                   <label for="daily-{{idx}}">Daily</label>
#                   <input type="radio" id="total-{{idx}}" name="wordcountreg" value="total" class="formfield" required checked disabled>
#                   <label for="total-{{idx}}">Total</label>
#                 </div>
#                 <br/>
#                 <label>Start Date:</label><input type="date" name="targetstartdate" value="{{ project.targetstartdate }}" class="formfield" required disabled><br/>
#                 <label>Goal End Date:</label><input type="date" name="targetenddate" value="{{ project.targetenddate }}" class="formfield" required disabled><br/>
#             </fieldset>
#         </div>
#             <input type="submit" value="Update Project" class="formfield hidden" disabled> 
#         </form>
#         <div class="modal modal-{{idx}} hidden">
#           <form action = "/project-options/{{idx}}/ren" method = "POST">
#             <input type="text" name="name" value="{{ project.name }}" class="formfield" required hidden>
#             <input type="text" name="newname" value="{{ project.name }}" class="formfield" required>
#             <input type="submit" value="Rename Project">
#           </form>
#         </div>
#         <div id="project-actions-{{idx}}" class="project-actions project-actions-{{idx}}">
#           <form class="" action = "/current-project" method = "POST">
#               <input type="hidden" name="currentproject" value="{{idx}}">
#               <input type="submit" value="Show Insights">
#           </form>
#             <button class="debug" onclick="alert(document.cookie);">Cookie Alert</button>
#             <button onclick="m = document.querySelector('.modal-{{idx}}'); m.classList.toggle('hidden');">Rename Project</button>
#             <button onclick="pr = document.querySelectorAll('div#project-{{idx}} form#project-{{idx}}-form .formfield'); pr.forEach(function(x){x.toggleAttribute('disabled');}); document.querySelector('#project-{{idx}}-form > input[type=\'submit\']').classList.toggle('hidden');">Edit Project</button>
#           <form action = "/project-options/{{idx}}/del" method = "POST">
#               <input type="text" name="name" value="{{ project.name }}" class="formfield" required hidden>
#               <input type="submit" value="Delete Project">
#           </form>
#           <form action = "/project-options/{{idx}}" method = "POST">
#             <input type="text" name="name" value="{{ project.name }}" class="formfield" required hidden>
#             <input type="submit" value="Refresh Word Count">
#           </form>
#         </div>
#       </div>
#     </div>
#   {% endfor %}""") 

    return t.render(projects=projects_zip)


# Exposing Class Sqlite Funcs to Eel ##

@eel.expose
def new_author(authorname):
    create_author(authorname)

@eel.expose
def new_project(authorname, projectname, targetstartdate , targetenddate, wordcountgoal, current_daily_target, wp_page, projectpath, is_weekly_word_count, weekly_words):
    #print(authorname, projectname, targetstartdate , targetenddate, wordcountgoal, current_daily_target, wp_page, projectpath)
    
    a = AuthorActions()
    a.id_by_name(authorname)
    a.create_project(projectname, targetstartdate , targetenddate, wordcountgoal, current_daily_target, wp_page, projectpath, is_weekly_word_count, weekly_words)

    # Samples
    # a.id_by_name('Johnny')
    # a.create_project("Johnny's Other Manifesto", '2020-04-24', '2020-06-20', '15000', '400', '400', r'D:\Documents\Datasets\001. ML Projects\Wordcount v2\Git Project\Johnnys Manifesto.txt')


# Exposing 'Top Level' Sqlite Funcs to Eel ##

@eel.expose
def eel_return_author_list():
    """
    Prints all authors as a list of dicts
    """
    return return_author_list()

    
@eel.expose
def eel_create_author(author_name, password=''):    
    """ 
    Inserts an Author into database if they don't exist.
    If they do, this task does not go through. 
    """
    return create_author(author_name, password)

@eel.expose
def eel_return_project_screen(author_id:int) -> list(dict()):
    """
    Returns all the values needed for the Projects page, each 'div' as an individual dict.
    Needs to be tested on entries without a table.
    """
    return return_project_screen(author_id)

@eel.expose
def return_projects_by_name(author_name:str) -> list(dict()):
    a = AuthorActions()
    a.id_by_name(author_name)
    return a.return_projects()

@eel.expose
def rename_project(project_id, new_name):
    pa = ProjectActions(project_id)
    pa.rename_project(new_name)
    return new_name

@eel.expose
def delete_project(authorname, project_name):
    a = AuthorActions()
    a.id_by_name(authorname)
    a.delete_project(project_name)
    return

@eel.expose
def eel_refresh_wordcounts(project_id):
    pa = ProjectActions()
    pa.set_project(project_id)
    pa.enter_wordcount()
    return 

@eel.expose
def eel_get_proj_info(project_id):
    """
    Given a project id, retrieves all information about it
    """
    pa = ProjectActions()
    return pa.get_project(project_id)[0]

@eel.expose
def eel_return_project_stats(project_id):
    """
    Given a project id, retrieves all information required for the stats modal
    """
    return return_stats_screen(project_id)

@eel.expose
def eel_update_project(authorname, project_id, proj_name, proj_path, proj_startdate,
 proj_enddate, proj_daily, proj_total, proj_isWeekly, proj_weekly):
    """
    Takes in all old and new information about project and edits it to match
    """
    pa = ProjectActions()
    pa.set_project(project_id)
    pa.rename_project(proj_name)
    
    if proj_isWeekly:
        pa.change_weekly_words(proj_weekly)
    
    pa.change_daily_words(proj_daily)
    pa.change_word_goal(proj_total)
    pa.change_deadline(proj_enddate)

@eel.expose
def eel_export_proj_to_csv(proj_id, csv_path):
    pa = ProjectActions()
    pa.set_project(proj_id)
    try:
        pa.render_wordcounts(csv_path)
        print("We should be good!")
        return 0
    except:
        print("WHOOPS THAT DIDN'T WORK")
        return 1

"""
Word count calculation end points
"""
@eel.expose
def wcCalc_dailyWordsCalc(word_goal, goal_start_date, goal_finish_date):
    return str(daily_words_calculate(word_goal, goal_start_date, goal_finish_date))

@eel.expose
def wcCalc_wordgoalCalc(daily_target, goal_start_date, goal_finish_date, is_weekly_wordcount):
    return str(word_goal_calculate(daily_target, goal_start_date, goal_finish_date, is_weekly_wordcount))

@eel.expose
def wcCalc_weeklyWordsCalc(weekly_words, goal_start_date, goal_finish_date):
    return str(weekly_words_calculate(weekly_words, goal_start_date, goal_finish_date))