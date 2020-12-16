# Dummy Projects for testing purposes

# returned from wordmeta_pull {'Filetype': {'Alice in Project Land': 'txt'}, 'Latest Target': {'Alice in Project Land': 2000}, 'Project Path': {'Alice in Project Land': 'C:/Dummy/File/Path.txt'}, 'Deadline': {'Alice in Project Land': 210331}}
# returned from wordmeta_pull [{'Daily Target': 0, 'Project Path': 'C:/Dummy/FilePath/dummyProjects/B2F.txt', 'Filetype': 'txt', 'Start Date': 201215, 'Deadline': 210323, 'Wordcount Goal': 12000}]
# returned from wordmeta_pull_all {'Back 2 DF': {'Daily Target': 0, 'Project Path': 'C:/Dummy/FilePath/dummyProjects/B2F.txt', 'Filetype': 'txt', 'Start Date': 201215, 'Deadline': 210323, 'Wordcount Goal': 12000}, 'Bacon': {'Daily Target': 0, 'Project Path': 'C:/Dummy/FilePath/dummyProjects/bacon.txt', 'Filetype': 'txt', 'Start Date': 201215, 'Deadline': 210321, 'Wordcount Goal': 784512}}

def dummy_projects():
    dummy_project = {
            "name": "Alice in Project Land",
            "filepath": "C:/Dummy/File/Path.txt",
            "filetype": 'txt',
            "wordcountgoal": 20000,
            "todaystargetwordcount": 1000,
            "targetstartdate": 201210, #10 Dec 2020
            "targetenddate": 210331 #31st March 2021 
        }

    dummy_project2 = {
            "name": "Writing for Dummies",
            "filepath": "C:/Dummy/File/Path2.txt",
            "filetype": 'txt',
            "wordcountgoal": 50000,
            "todaystargetwordcount": 1000,
            "targetstartdate": 201208, #08 Dec 2020
            "targetenddate": 210721 #21st Jul 2021 
        }

    projects = {"0": dummy_project, "1": dummy_project2}

    return projects