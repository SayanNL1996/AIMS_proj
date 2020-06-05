from database_connection import DatabaseConnection
from validation import Validation
from query import Queries

conn = DatabaseConnection.dbconnection()
cursor = conn.cursor()


class Worker:
    def __init__(self, id):
        """

        :param id:
        """
        self.id = id
        Worker.worker_tasks(self)

    def worker_tasks(self):
        """
        List of all the Employee tasks.
        :return:
        """
        try:
            print("\nSelect the task!\n"
                  "1: Create Complaint\n"
                  "2: Show Complaint History\n"
                  "3: Show Active Complaints\n"
                  "4: Show Profile\n")
            worker_tasks_id = int(input("Select task: "))

            if worker_tasks_id == 1:
                Worker.create_complaint(self)
            elif worker_tasks_id == 2:
                Worker.show_complaint_history(self)
            elif worker_tasks_id == 3:
                Worker.show_active_complaints(self)
            elif worker_tasks_id == 4:
                Worker.show_worker_profile(self)
            else:
                raise Exception
        except Exception as e:
            print("Invalid Choice. Please select again!")
            Worker.worker_tasks(self)

    def create_complaint(self):
        """
        Creating a complaint to admin.
        :return:
        """

        result = Worker.input_create_complaint_data(self)
        Queries.create(self, 'Complaints',
                       (result[0], result[1], self.id)
                       )

        Worker.worker_tasks(self)

    def input_create_complaint_data(self):
        """
        Validating the inputs for creating a complaint.
        :return:
        """

        accident_name = Validation.input_str_for_create(self, "Enter details: ")
        comments = Validation.input_str_for_create(self, "Enter comments: ")

        return accident_name, comments

    def show_complaint_history(self):
        """
        Shows the list of all the complaints registered by them.
        :return:
        """
        try:
            sql = "select * from Complaints where worker_id = ?"
            result = cursor.execute(sql, (self.id,))

            for i in result:
                print("id : {}".format(i[0]))
                print("Accident_name : {}".format(i[1]))
                print("Comments : {}".format(i[2]))
                print("Status : {}".format(i[4]))
                print("----------------------------")


        except Exception as e:
            print("Error in reading data")
        finally:
            Worker.worker_tasks(self)

    def show_active_complaints(self):
        """
        Shows the complaints that are work in progress.
        :return:
        """
        try:
            sql = "select * from Complaints where worker_id = ? and status = 'WIP'"
            result = cursor.execute(sql, (self.id,))
            for i in result:
                print("Complaint_id : {}".format(i[0]))
                print("Accident_name : {}".format(i[1]))
                print("Comments : {}".format(i[2]))
                print("Status : {}".format(i[4]))
                print("----------------------------")

        except Exception as e:
            print("Error in reading data")
        finally:
            Worker.worker_tasks(self)

    def show_worker_profile(self):
        """
        Shows the details of an employee profile.
        :return:
        """
        try:
            sql = "select * from Employees where id = ?"
            result = cursor.execute(sql, (self.id,))
            for i in result:
                print("Employee_id : {}".format(i[0]))
                print("Name : {}".format(i[1]))
                print("Email : {}".format(i[2]))
                print("Role : {}".format(i[4]))
                print("----------------------------")
        except Exception as e:
            print("Error in reading data")
        finally:
            Worker.worker_tasks(self)
