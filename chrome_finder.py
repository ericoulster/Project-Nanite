import platform
import os


def has_chrome():
    expected_chrome_locations = {
        "Darwin":"/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome",
        "Windows":"C:\Program Files\Google\Chrome\Application\Chrome.exe",
        "Linux":"/usr/bin/google-chrome"
    }


    try:
        install_path = expected_chrome_locations[platform.system()]
    except:
        raise NotImplemented(f"Error: {platform.system()} not recognized os")
    
    return os.path.exists(install_path)

def has_chromium():
    expected_chrome_locations = {
        "Darwin":"./Chromium.app",
        "Windows":".\Chromium.exe",
        "Linux":"./Chromium"
    }

    try:
        install_path = expected_chrome_locations[platform.system()]
    except:
        raise NotImplemented(f"Error: {platform.system()} not recognized os")
    
    return os.path.exists(install_path)
