import eel, os
from tkinter import filedialog
from tkinter import *

@eel.expose
def dir_select_tk():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost',1)
    folder_selected = filedialog.askdirectory()

    # print(folder_selected)
    return folder_selected

@eel.expose
def parent_dir(folder):
    if os.path.isdir(folder):
        os.chdir(folder)
        os.chdir('..')
        return os.getcwd()
    else:
        return 'Not valid folder'

@eel.expose
def enter_dir_and_list_contents(folder):
    if os.path.isdir(folder):
        os.chdir(folder)
        return os.listdir(folder)
    else:
        return 'Not valid folder'

@eel.expose
def list_contents_are_directories(folder):
    if os.path.isdir(folder):
        os.chdir(folder)
        types_list = list(map(os.path.isdir, os.listdir(folder)))
        return types_list
    else:
        return 'Not valid folder'


@eel.expose
def get_cwd():
    return os.getcwd()