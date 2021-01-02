# -*- coding: utf-8 -*-
# Start Flask with default web server
 
#from front_end import app
from front_end import ui


HOST='127.0.0.1'
PORT='5000'

if __name__ == '__main__':
    # app.run(host=HOST, port=PORT,)
    #app.run(host=HOST, port=PORT, debug=True) # This
    ui.run()
