import eel
import nanite_eel_api
import sqlite_funcs as sf

import webbrowser
import os

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

try:
    # Start Eel
    eel.start('templates/home.html', size=(700, 700), jinja_templates='templates')
except:
    # Chrome not found; redirects user to a page asking them to install chrome
    # (Opens using user's default browser instead of via eel to avoid taking up the websocket)
    webbrowser.open_new_tab(f"file:///{os.getcwd()}/front_end/templates/error_download_chrome.html")