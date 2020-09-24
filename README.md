Naticusdroid_test has 2 major files right now

index.html - This is the first file of the we app where the user can upload the apk file and upload it to the server to check whether it is malicious or benign.


backend.py - This file is the server file that sets up a localhost(127.0.0.1:12345) webserver. Once the webserver is up and running, then any apk uploaded on index.html will be uploaded on the server. The permissions are extracted from the apk using 'Androguard', which are passed to the model in the form of a permission vector. The model then yields a decision and passes the result as a JSON file which is displayed as a web page.  In the background, some details of the apps are being stored in a MySQL database, along with their malware classification. 
