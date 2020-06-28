# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:30:06 2020

@author: PKALYAN
"""

import sqlite3

# creates data.db inside our folder

connection = sqlite3.connect('data.db')
# it starts things, where to start from and executing queries also stores results
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)

user = (1,'kalyan','abcd')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)

users = [(1,'kalyan1','abcd'),
         (2,'kalyan6','abcd'),
         (3,'kalyan2','abcd'),
         (4,'kalyan3','abcd'),
         (5,'kalyan4','abcd'),
         (6,'kalyan5','abcd')
         ]
cursor.executemany(insert_query,users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()