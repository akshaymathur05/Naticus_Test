# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:25:44 2020

@author: aksha
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="akshay",
  password="Cstar_2033",
  database="naticus"
)

cursor = mydb.cursor()

#INSERT/UPDATE/CREATE/DELETE
cursor.execute("CREATE DATABASE naticus")
cursor.execute("DROP TABLE applications")
cursor.execute("CREATE TABLE applications (app_id INTEGER PRIMARY KEY AUTO_INCREMENT, app_name VARCHAR(255), app_about LONGTEXT, app_perms LONGTEXT, app_classification VARCHAR(10))")


#SELECT/SHOW
cursor.execute("SHOW TABLES")
cursor.execute("SHOW COLUMNS FROM applications")
cursor.execute("SELECT * from applications")


#PRINT RESULTS
result = cursor.fetchall()
for x in result:
    print(x)
    print("\n")