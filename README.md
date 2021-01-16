# Blogging-Website  
A simple blogging app using Flask and SQLite implementing user role based authorization.  
two types of users - admin and author  
admin can create own blog, read all blogs, delete all blogs of any user. it can also delete users.      
author can create own blog, read all blogs of all users, delete his own blogs.  

Admin credentials  
email = admin@example.com  
password = admin  

Requirements  
-python3  
-pip  
-virtualenv  
-git  


To run the webapp  
-clone the repository  
-create a virual environment by command "virtualenv venv"  
-activate the virtual environment  
    for linux - source venv/bin/activate  
    for windows - venv\Scripts\activate  
-enter command "pip install -r requirements.txt" for installation of required libraries  
-enter command "flask run" to start the webapp  