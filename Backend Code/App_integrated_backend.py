# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:15:20 2020

@author: aksha
"""

from flask import Flask, request, jsonify, render_template
import joblib
#import traceback, os
import pandas as pd
#import jinja2
import mysql.connector
from androguard.core.bytecodes.apk import APK
from time import time

'''Initializing FLASK and index.html'''
app = Flask(__name__)

'''Connecting to the MySQL server containing the database named naticus'''
mydb = mysql.connector.connect(
  host="localhost",
  user="akshay",
  password="Cstar_2033",
  database="naticus"
)


model = joblib.load("Naticus.pkl") # Load "model.pkl"
print ('Model loaded')
model_columns = joblib.load("Naticus_columns.pkl") # Load "model_columns.pkl"
print ('Model columns loaded')
PERMISSIONS = model_columns
v = len(PERMISSIONS)



@app.route("/naticus", methods = ["POST"])
def parse_request_list():
    recieved_string = request.form['perm_list']
    #Now check if permission list is actually a 'list' or some other object.
    #Once checked, pass the permission list to a function which creates the permission vector. 
    #The permission vector is passed to the model and classified 
    permission_list = list(recieved_string.split(","))
    permission_list.pop()
    #print(permission_list)
    permission_vector = create_perm_vector(permission_list)
    #print(permission_vector)
    result = classify(permission_vector)
    return result;



@app.route("/perm_info", methods = ["POST"])
def parse_request_perm():
    permission = request.args['perm']
    #Now check if permission list is actually a 'list' or some other object.
    #Once checked, pass the permission list to a function which creates the permission vector. 
    #The permission vector is passed to the model and classified 
    return permission


def create_perm_vector(permission_list):
    perm_vector = [] * v
    for permission in PERMISSIONS:
        hit = 1 if permission in permission_list else 0
        perm_vector.append(hit)
    
    return list(perm_vector)

def classify(query):
    if model:
        query = [query]
        query = pd.DataFrame(query, columns = model_columns)
            
        classification = model.predict(query)
        if classification == 0:
            category = 'Benign'
        else:
            category = 'Malware'
        
        return category
        
    else:
        return ('No model here to use')


'''
The main function initializes the ports for the server, loads the model and variables, and runs the server.
'''
if __name__ == '__main__':    
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 5000 # If you don't provide any port the port will be set to 12345

#    app.run(host='172.31.203.233',port=port)    
    app.run(port=port)    





































