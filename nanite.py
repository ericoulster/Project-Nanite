import eel
import nanite_eel_api
import sqlite_funcs as sf
from chrome_finder import has_chrome, has_chromium
import os
import webbrowser


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

# Checks user's os via platform and then sees if chrome is installed in the default location
# Will probably flag if the user installed in a wonked out location but...
if has_chrome() or has_chromium():
    # Start Eel
    print("Found chrome")
    eel.start('templates/home.html', size=(700, 700), jinja_templates='templates')
else:
    print("Couldn't find chrome")
    # Chrome not found; redirects user to a page asking them to install chrome
    # (Opens using user's default browser instead of via eel to avoid taking up the websocket)
    webbrowser.open_new_tab(f"file:///{os.getcwd()}/front_end/templates/error_download_chrome.html")