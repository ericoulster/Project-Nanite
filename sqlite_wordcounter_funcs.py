import os
import glob
import string
import re
import fileinput
import csv
import easygui
from datetime import date, datetime
from math import ceil

import numpy as np
import pandas as pd

import sqlite3

### DDL Queries ###

create_author_sql = """
CREATE TABLE IF NOT EXISTS authors (
    author_id integer PRIMARY KEY,
    username text NOT NULL,
    password text,
    acct_created_on text NOT NULL
)
"""

create_project_sql = """
CREATE TABLE IF NOT EXISTS projects (
    project_id integer PRIMARY KEY,
    author_id integer,
    project_name text NOT NULL,
    project_created_on text NOT NULL,
    deadline text,
    wordcount_goal int,
    current_daily_target int,
    filetype text NOT NULL,
    is_folder int NOT NULL,
    project_path text NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors (author_id)
)
"""

create_words_sql = """
CREATE TABLE IF NOT EXISTS words (
    record_id integer PRIMARY_KEY,
    project_id integer,
    author_id integer,
    Wdate text NOT NULL,
    Wcount int NOT NULL,
    Wtarget int,
    FOREIGN KEY (project_id) REFERENCES projects (project_id),
    FOREIGN KEY (author_id) REFERENCES authors (author_id)
)
"""

### 



sqlite3_path = './Project-Nanite/database/nanite_storage.sqlite3'
# SQLite just needs to connect to create db
def db_init():
    """creates database if they don't exist"""
    if os.path.exists(sqlite3_path) == False:
        conn = sqlite3.connect(sqlite3_path)
        conn.execute("PRAGMA foreign_keys = 1")
        conn.execute(create_author_sql)
        conn.execute(create_project_sql)
        conn.execute(create_words_sql)
        conn.close()
    else:
        pass