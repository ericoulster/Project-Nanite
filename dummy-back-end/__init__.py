from flask_sqlalchemy import SQLAlchemy
from nanite import app

# TODO: SET UP DATABASE - rough code below

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectname = db.Column(db.Text)
    projectfilepath = db.Column(db.Text)
    targetwordcount = db.Column(db.Integer)
    todaystargetwordcount = db.Column(db.Integer)
    targetenddate = db.Column(db.Integer)

    completed = db.Column(db.Boolean, default=False)

    def __init__(self, projectname, projectfilepath, targetwordcount, todaystargetwordcount, targetenddate, completed):
        self.projectname = projectname
        self.projectfilepath = projectfilepath
        self.targetwordcount = targetwordcount
        self.todaystargetwordcount = todaystargetwordcount
        self.targetenddate = targetenddate
        self.completed = False

    def __repr__(self):
        status = "Completed" if self.completed else "Incomplete"
        return '<Project: %s, Target: %i words to complete by %i. Status: %s>' % (self.projectname, self.targetwordcount, self.targetenddate, status)

db.create_all()