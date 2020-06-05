import sqlite3


#
# def connect(self):
#     """
#     Connecting to Database
#     @return: connection object
#     """
#     conn = sqlite3.connect('/home/nineleaps/PycharmProjects/AIMS_project/aims_db.sqlite')
#
#     return conn
class DatabaseConnection:

    def dbconnection(self):
        conn = sqlite3.connect('/home/nineleaps/PycharmProjects/AIMS_project/aims_db.sqlite')
        return conn
