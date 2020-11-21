from flask import Flask, render_template, request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def getprojects(): # getprojects = function that produces an iterable list of projects (dictionaries? objects?) that user can view/edit settings for
    project = {
        "name": "Dummy Project Name",
        "filepath": "C:/Dummy/File/Path.txt",
        "targetwordcount": 20000,
        "targetenddate": 210331 #31st March 2021 
    }
    projects = [project]
    return projects


@app.route('/')
def index():
    return render_template('home.html', pagetitle='Home')

@app.route('/options')
def pg_options():
    projects = getprojects() 
    return render_template('options.html', pagetitle='Project Options', projects=projects)

@app.route('/stats')
def pg_stats():
    return render_template('stats.html', pagetitle='Stats')

@app.route('/charts')
def pg_charts():
    return render_template('charts.html', pagetitle='Charts')


@app.route('/update-options', methods=['POST'])
def update_options():
    # CODE HERE
    return redirect('/')

@app.route('/new-project', methods=['POST'])
def new_project():
    projectname = request.form['projectname']
    filepath = request.form['filepath']
    targetwordcount = request.form['targetwordcount']
    targetenddate = request.form['targetenddate']

    # BACK END CODE HERE
    # return redirect('/')
    return f"Submitted values: {projectname} | {filepath} | {targetwordcount} | {targetenddate}"   

if __name__ == '__main__':
    app.run()
