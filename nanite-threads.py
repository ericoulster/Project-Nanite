import eel
import naniteglobals
from tkinter import filedialog
from tkinter import *

eel.init('front_end')

##### ##### ##### ##### ##### 
# Thread to show the file dialog box
def filedialog_thread():
    #global naniteglobals.filedialog_show
    #global naniteglobals.folder_selected
    while True:
        print(naniteglobals.filedialog_show)
        # Tkinter Loop
        if naniteglobals.filedialog_show:
            root = Tk()
            root.withdraw()
            naniteglobals.folder_selected = filedialog.askdirectory()
            print(naniteglobals.folder_selected)

            #reset filedialog_show to False (don't show it again needlessly)
            naniteglobals.filedialog_show = False

        eel.sleep(2)

eel.spawn(filedialog_thread)
##### ##### ##### ##### ##### 

import file_access # needs to be after eel.init and before eel.start (?)

eel.start('templates/home.html', size=(500, 300), jinja_templates='templates', block=False)

while True:
    # Main Loop
    eel.sleep(2)     