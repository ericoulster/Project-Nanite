# Dummy Projects for testing purposes

def dummy_projects():
    dummy_project = {
            "name": "Dummy Project Name",
            "filepath": "C:/Dummy/File/Path.txt",
            "filetype": 'txt',
            "targetwordcount": 20000,
            "todaystargetwordcount": 1000,
            "targetenddate": 210331 #31st March 2021 
        }

    dummy_project2 = {
            "name": "Writing for Dummies",
            "filepath": "C:/Dummy/File/Path2.txt",
            "filetype": 'txt',
            "targetwordcount": 50000,
            "todaystargetwordcount": 1000,
            "targetenddate": 210721 #21st Jul 2021 
        }

    projects = {"0": dummy_project, "1": dummy_project2}

    return projects