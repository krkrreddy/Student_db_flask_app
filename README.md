# Student_db_flask_app
Students App based on using Flask and SQL server:

This app stores students name and roll number in sql data base. 
Retrieves and delete records for authorized user requests.

This project has 5 modules:

1.Student_app is main module from which all other sub modules are called. 

2.Db_user module allows to create new user and retrieve user name and password based on id or user name as input.

3.Security module has authenticate and identity functions.

4.Student module performs registeration of new student details,updation,deletion and retrieval of students details.

5.Create table module allows to create two base tables 
   
   --user for storing user id,name and password.  
   
   --student for storing student name and roll number.
