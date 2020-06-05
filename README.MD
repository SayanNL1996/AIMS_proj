AIMS(Accident & Incident Management System)

Introduction
----
Accident & Incident Management application (AIMS) is designed to help you manage accidents, incidents and near misses. The system provides for a structured investigation of accidents and incidents, from which preventative actions can then be generated and tracked. "Lessons learned" and best practice can be identified and shared across the organisation.
### Configuration parameters
**Email and Password** are the configuration parameter required to make the login for each user.
The parameters are entered in the console to enter the system.
### Authentication
A call is made to the SQLITE database with the login credentials, the credentials are validated for existence and henceforth the login is made; else "Invalid Credentials" message is displayed.
### database_connection.py
This file is used to create a database connection to the SQLite database. The database file thus created is - "mgnrega_database.sqlite".
### login.py
This file is used to start the project.It takes the credentials and calls authentication.py file.
### authentication.py
This file is used to validate the credentials for a particular user and return boolean value along with the userid if return value id True.
### models.py
This file contains all the schema that are executed when a particular operation is called.
### query.py
This file contains create, update and delete query which are called from different files to perform an operation.
### validation.py
This file contains all the function that are used to validate the inputs.

Some valid credentials to access the system as different users are:
```
**Admin**
  Email: sayan@gmail.com
  Password: sayan@1
**Supervisor**
  Email: rohit@gmail.com
  Password: rohit@1
**Member**
  Email: anant@gmail.com
  Password: Anant@1

```
### admin.py
This file is used to carry out all the Admin related functions.
### supervisor.py
This file is used to carry out all the Supervisor related functions.
### worker.py
This file is used to carry out all the Employee related functions.
### DIRECTORY STRUCTURE
```
+-- AIMS_project
|  +--login.py
|  +--authentication.py
|  +--database_connection.py
|  +--models.py
|  +--query.py
|  +--validation.py
|  +--user
   |+--admin.py
   |+--supervisors.py
   |+--worker.py

```
###FLOW
1. Run database_connection.py
2. Run the models.py
3. Run the login.py file.Choose the user to be logged in as.
4. Enter valid credentials for the user.
4. Carry out user related tasks.
