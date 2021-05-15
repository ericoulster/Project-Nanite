import eel
import nanite_eel_api
from sqlite_funcs import db_init

eel.init('front_end')
db_init() # create database if needed

# import or write exposed functions here
# 
# EXAMPLE:
# @eel.expose
# def py_random():
#     return random.random()

import file_access

# Start Eel
eel.start('templates/home.html', size=(700, 700), jinja_templates='templates')