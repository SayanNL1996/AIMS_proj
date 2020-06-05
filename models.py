from database_connection import connect

conn = connect()
cursor = conn.cursor()

# print("database created successfully")

# cursor.execute('''CREATE TABLE IF NOT EXISTS Admin
#          (id  INT AUTO_INCREMENT PRIMARY KEY,
#          name            VARCHAR(30)    NOT NULL,
#          email           VARCHAR(20)    NOT NULL,
#          password        VARCHAR(10) NOT NULL,
#          created_at DATETIME DEFAULT CURRENT_TIMESTAMP);''')
#
# cursor.execute("INSERT INTO Admin VALUES (1,'sayan','sayan@gmail.com','sayan@1',datetime());")
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS Employees
#          (id  INTEGER PRIMARY KEY AUTOINCREMENT,
#          name           VARCHAR(30) NOT NULL,
#          email           VARCHAR(20)    NOT NULL UNIQUE,
#          password        VARCHAR(10) NOT NULL,
#          role               VARCHAR(10) DEFAULT "not assigned",
#          created_at DATETIME DEFAULT CURRENT_TIMESTAMP);''')
#
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS Supervisors
#          (id  INTEGER PRIMARY KEY AUTOINCREMENT,
#          name           VARCHAR(30) NOT NULL,
#          email           VARCHAR(20)    NOT NULL,
#          password        VARCHAR(10) NOT NULL,
#          assigned        VARCHAR(20)    DEFAULT "none",
#          Team_Number     INTEGER(10) NOT NULL,
#          created_at DATETIME DEFAULT CURRENT_TIMESTAMP);''')



# cursor.execute('''CREATE TABLE IF NOT EXISTS Complaints
#          (id  INTEGER PRIMARY KEY AUTOINCREMENT,
#          accident_name           VARCHAR(30) NOT NULL,
#          comments           VARCHAR(50)    NOT NULL,
#          worker_id        INTEGER(10) NOT NULL,
#          status             VARCHAR(10) DEFAULT "open",
#          assigned_team      INTEGER(10) DEFAULT "none",
#          created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#         FOREIGN KEY (worker_id) REFERENCES Employees(id),
#         FOREIGN KEY (assigned_team) REFERENCES Supervisors(Team_Number));''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS Report
#          (id  INTEGER PRIMARY KEY AUTOINCREMENT,
#          complaint_id           INTEGER(10) NOT NULL,
#          team_no           INTEGER(10)    NOT NULL,
#          root_cause        VARCHAR(50) NOT NULL,
#          details             VARCHAR(100) NOT NULL,
#          status             VARCHAR(10)  DEFAULT "none",
#          no_of_people_effected  INTEGER(100) NOT NULL,
#          death_rate         INTEGER(100)    DEFAULT "none",
#          created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#         FOREIGN KEY (complaint_id) REFERENCES Complaints(id),
#         FOREIGN KEY (team_no) REFERENCES Supervisors(Team_Number));''')


#
conn.commit()
conn.close()