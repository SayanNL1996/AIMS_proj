from database_connection import DatabaseConnection
from validation import Validation
from query import Queries

conn = DatabaseConnection.dbconnection()
cursor = conn.cursor()


class Supervisor:

    def __init__(self, id):
        """
        Initializing and to get the team no of a supervisor.
        :param id:
        """
        self.id = id
        get_tid = "select Team_Number from Supervisors where id = ?"
        res = cursor.execute(get_tid, (self.id,))
        for i in res:
            Supervisor.team_id = i[0]
        Supervisor.supervisor_tasks(self)

    def supervisor_tasks(self):
        """
        Supervisor selects a task.
        :return:
        """
        try:
            option = {
                "1": ("Show Complaint", Supervisor.show_complaint),
                "2": ("Create Reports", Supervisor.create_report),
                "3": ("Show Reports", Supervisor.show_reports)
            }
            ans = input("Choose:\n"
                        "1.Show Complaint.\n"
                        "2.Create Reports.\n"
                        "3.Show Reports.\n")

            option.get(ans)[1](conn)
        except Exception as e:
            print("Invalid Choice. Please select again!")
            Supervisor.supervisor_tasks(self)

    def show_complaint(self):
        """
        Shows list of all the complaints assigned to their team by admin.
        :return:
        """
        try:

            sql = "select c.id,c.accident_name,c.comments from Complaints c where assigned_team = ?"
            result = cursor.execute(sql, (Supervisor.team_id,))
            for i in result:
                print("Complaint_id : {}".format(i[0]))
                print("Accident Name : {}".format(i[1]))
                print("Comments : {}".format(i[2]))
                # print("Complaint Status : {}".format(i[3]))
                print("----------------------------")


        except Exception as e:
            print("Error in reading data")

    def create_report(self):
        """
        Creating a report for a complaint assigned to them.
        :return:
        """

        Supervisor.show_complaint(self)
        result = Supervisor.input_create_report_data(self)
        Queries.create(self, 'Report',
                       (int(result[0]), Supervisor.team_id, result[1], result[2], int(result[3]), int(result[4]))
                       )
        Supervisor.supervisor_tasks(self)

    def input_create_report_data(self):
        """
        Validating the inputs for creating a report.
        :return:
        """

        complaint_no = Validation.input_int_for_create(self, "Enter Complaint id: ")
        root_cause = Validation.input_str_for_create(self, "Enter root cause: ")
        details = Validation.input_str_for_create(self, "Enter details: ")
        no_of_people_effected = Validation.input_int_for_create(self, "Enter total no of people effected: ")
        death_rate = Validation.input_int_for_create(self, "Enter number of deaths: ")

        return complaint_no, root_cause, details, no_of_people_effected,death_rate

    def show_reports(self):
        """
        Shows the list of all the reports assigned to them.
        :return:
        """
        try:
            sql = "select * from Report where team_no = ?"
            result = cursor.execute(sql, (Supervisor.team_id,))
            for i in result:
                print("Report Id : {}".format(i[0]))
                print("Root Cause : {}".format(i[3]))
                print("Details : {}".format(i[4]))
                print("Status : {}".format(i[5]))
                print("Death Rate : {}".format(i[6]))
                print("----------------------------")

        except Exception as e:
            print("Error in reading data")
        finally:
            Supervisor.supervisor_tasks(self)
