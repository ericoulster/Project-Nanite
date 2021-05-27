import eel
import nanite_eel_api
import sqlite_funcs as sf

sqlite3_path = sf.sqlite3_path

eel.init('front_end')
sf.db_init() # create database if needed

# import or write exposed functions here
# 
# EXAMPLE:
# @eel.expose
# def py_random():
#     return random.random()

import file_access

# Start Eel
eel.start('templates/home.html', size=(700, 700), jinja_templates='templates')