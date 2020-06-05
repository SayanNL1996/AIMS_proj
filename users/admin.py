from database_connection import DatabaseConnection
from validation import Validation
from query import Queries

conn = DatabaseConnection.dbconnection()
cursor = conn.cursor()


class Admin:
    def __init__(self, id):
        """
        :param id: Admin id
        """
        self.id = id
        Admin.admin_tasks(self)

    def admin_tasks(self):
        """
        To select a specific task of admin
        :return:
        """
        try:
            option = {
                "1": ("Worker Management", Admin.admin_worker_mgmnt),
                "2": ("Supervisor Management", Admin.admin_supervisor_mgmnt),
                "3": ("Show Complaints", Admin.show_complaints),
                "4": ("Report Management", Admin.admin_report_management)

            }
            ans = input("Choose:\n"
                        "1.Worker Management.\n"
                        "2.Supervisor Management.\n"
                        "3.Show Complaints.\n"
                        "4.Report Management\n")

            option.get(ans)[1](conn)
        except Exception as e:
            print("Invalid Choice. Please select again!")
            Admin.admin_tasks(self)

    def admin_worker_mgmnt(self):
        """
        Admins select a task for Employee Management.
        :return:
        """
        try:
            option = {
                "1": ("Create Worker Profile", Admin.create_worker),
                "2": ("Show All Workers", Admin.show_allworkers),
                # "3": ("Update Worker Profile", Supervisor.show_reports),
                "4": ("Delete Worker Profile", Admin.delete_worker),
                "5": ("Assign Job Role", Admin.assign_jobrole),
                "6": ("Go back", Admin.admin_tasks)

            }
            ans = input("Choose:\n"
                        "1.Create Worker Profile.\n"
                        "2.Show All Workers.\n"
                        "3.Update Worker Profile.\n"
                        "4.Delete Worker Profile.\n"
                        "5.Assign Job Role.\n"
                        "6.Go back.\n"
                        )

            option.get(ans)[1](conn)
        except Exception as e:
            print("Invalid Choice. Please select again!")
        finally:
            Admin.admin_worker_mgmnt(self)

    def create_worker(self):
        """
        Admin creates an Employee Profile.
        :return:
        """

        result = Admin.input_create_worker_data(self)
        Queries.create(self, 'Employees',
                       (result[0], result[1], result[2])
                       )

    def input_create_worker_data(self):
        """
        Taking all the employee input for validation.
        :return:
        """
        name = Validation.input_str_for_create(self, "Enter name: ")
        email = Validation.validate_email(self, "Enter Email: ")
        password = Validation.input_not_null_pass(self, "Enter Password: ")

        return name, email, password

    def update_worker(self):
        pass

    def delete_worker(self):
        """
        Deleting a worker profile from DB.
        :return:
        """
        Admin.show_allworkers(self)
        delete_worker_id = Validation.input_int_for_create(self, "Enter the Worker id: ")
        Queries.delete(self, 'Employees', 'id', delete_worker_id)
        Admin.admin_worker_mgmnt(self)

    def assign_jobrole(self):
        """
        To assign a job role to an unassigned employee.
        :return:
        """
        try:

            Admin.show_unassigned_workers(self)
            assign_jobrole_id = int(input("Enter the worker id: "))
            assign_role = input("Enter role: ")
            sql = 'UPDATE Employees SET role = ? WHERE id = ?'
            cursor.execute(sql, (assign_role, assign_jobrole_id))
            conn.commit()
            print("Job role assigned")

        except Exception as e:
            print('error', e)

        finally:
            Admin.admin_worker_mgmnt(self)

    def show_allworkers(self):
        """
        To get the details of all the Employees.
        :return:
        """
        try:
            sql = "select * from Employees"
            result = cursor.execute(sql)
            for i in result:
                print("Worker Id : {}".format(i[0]))
                print("Name : {}".format(i[1]))
                print("Email : {}".format(i[2]))
                print("Role : {}".format(i[4]))
                print("----------------------------")

        except Exception as e:
            print("Error in reading data")

    def show_unassigned_workers(self):
        """
        To show the details of unassigned Employees.
        :return:
        """
        try:
            sql = "Select * from Employees where role = 'not assigned' "
            result = cursor.execute(sql)
            for i in result:
                print("Worker Id : {}".format(i[0]))
                print("Name : {}".format(i[1]))
                print("Email : {}".format(i[2]))
                print("Role : {}".format(i[4]))
                print("----------------------------")

        except Exception as e:
            print("Error in reading data")

    # SUPERVISOR MANAGEMENT
    def admin_supervisor_mgmnt(self):
        """
        Select a task for supervisor management.
        :return:
        """
        try:
            option = {
                "1": ("Create Supervisor Team", Admin.create_supervisorTeam),
                # "2": ("Update Supervisor Profile", Supervisor.create_report),
                "3": ("Delete Supervisor Profile", Admin.delete_supervisor),
                "4": ("Delete Supervisor Team", Admin.delete_supervisor_team),
                "5": ("Assign", Admin.assign_supervisor),
                "6": ("Go back", Admin.admin_tasks)

            }
            ans = input("Choose:\n"
                        "1.Create Supervisor Team.\n"
                        "2.Update Supervisor Profile.\n"
                        "3.Delete Supervisor Profile.\n"
                        "4.Delete Supervisor Team.\n"
                        "5.Assign.\n"
                        "6.Go back.\n")

            option.get(ans)[1](conn)
        except Exception as e:
            print("Invalid Choice. Please select again!")
            Admin.admin_supervisor_mgmnt(self)

    def create_supervisorTeam(self):
        """
        Creating a Supervisor Team.
        :return:
        """
        num = int(input("Enter number of members: "))
        for i in range(num):
            result = Admin.input_create_supervisorTeam_data(self)
            Queries.create(self, 'Supervisors',
                           (result[0], result[1], result[2], int(result[3]))
                           )
        Admin.admin_supervisor_mgmnt(self)

    def input_create_supervisorTeam_data(self):
        """
        To validate the inputs.
        :return:
        """

        name = Validation.input_str_for_create(self, "Enter name: ")
        email = Validation.validate_email(self, "Enter Email: ")
        password = Validation.input_not_null_pass(self, "Enter Password: ")
        team_no = Validation.input_int_for_create(self, "Enter Team Number: ")

        return name, email, password, team_no

    def update_supervisor(self):
        pass

    def delete_supervisor(self):
        """
        To delete a particular supervisor's profile from DB.
        :return:
        """
        Admin.show_allsupervisors(self)
        delete_supervisor_id = Validation.input_int_for_create(self, "Enter supervisor id: ")
        Queries.delete(self, 'Supervisors', 'id', delete_supervisor_id)
        Admin.admin_supervisor_mgmnt(self)

    def delete_supervisor_team(self):
        """
        To delete a particular supervisor team.
        :return:
        """
        Admin.show_allsupervisors(self)
        delete_supervisor_teamnumber_id = Validation.input_int_for_create(self, "Enter Team Number: ")
        Queries.delete(self, 'Supervisors', 'Team_Number', delete_supervisor_teamnumber_id)
        Admin.admin_supervisor_mgmnt(self)

    def show_allsupervisors(self):
        """
        Shows the details of all the supervisors.
        :return:
        """
        try:
            sql = "select * from Supervisors order by Team_Number"
            result = cursor.execute(sql)

            for i in result:
                print("Supervisor id : {}".format(i[0]))
                print("Name : {}".format(i[1]))
                print("Email : {}".format(i[2]))
                print("Assigned : {}".format(i[4]))
                print("Team Number : {}".format(i[5]))
                print("----------------------------")

        except Exception as e:
            print("Error in reading data")

    def assign_supervisor(self):
        """
        To assign a supervisor team to a particular problem.
        :return:
        """
        try:
            Admin.show_complaints(self)
            c_id = int(input("Enter Complaint id: "))
            Admin.show_unassigned_supervisors(self)
            t_id = int(input("Enter Team Number: "))

            sql = 'UPDATE Supervisors Set assigned = "yes" WHERE Team_Number = ?'
            cursor.execute(sql, (t_id,))
            conn.commit()
            sql1 = 'UPDATE Complaints Set status = "WIP",assigned_team = ? WHERE id = ?'
            cursor.execute(sql1, (t_id, c_id,))
            conn.commit()
            print("Assigned Successfully!")

        except Exception as e:
            print('error', e)

        finally:
            Admin.admin_supervisor_mgmnt(self)

    def show_unassigned_supervisors(self):
        """
        Shows the list of all the unassigned supervisors.
        :return:
        """
        try:
            sql = "Select Team_Number from Supervisors where assigned = 'none' group by Team_Number"
            result = cursor.execute(sql)
            for i in result:
                # print("Supervisor id : {}".format(i[0]))
                # print("Name : {}".format(i[1]))
                # print("Email : {}".format(i[2]))
                # print("Assigned : {}".format(i[4]))
                print("Team Number : {}".format(i[0]))
                print("----------------------------")

        except Exception as e:
            print("Error in reading data")

    # SHOW COMPLAINTS
    def show_complaints(self):
        """
        Shows the details of all the complaints.
        :return:
        """
        try:
            sql = "Select * from Complaints where status = 'open' "
            result = cursor.execute(sql)

            for i in result:
                print("Complaint_id : {}".format(i[0]))
                print("Accident Name : {}".format(i[1]))
                print("Comments : {}".format(i[2]))
                print("----------------------------")



        except Exception as e:
            print("Error in reading data")

    # REPORT MANAGEMENT
    def admin_report_management(self):
        """
        Admin selects a task for Report Management.
        :return:
        """
        try:
            option = {
                "1": ("Show Report History", Admin.show_all_reports),
                "2": ("Show Approved Reports", Admin.show_approved_reports),
                "3": ("Show Rejected Reports", Admin.show_rejected_reports),
                "4": ("Show Pending Reports", Admin.show_pending_reports),
                "5": ("Go back", Admin.admin_tasks)

            }
            ans = input("Choose:\n"
                        "1.Show Report History.\n"
                        "2.Show Approved Reports.\n"
                        "3.Show Rejected Reports.\n"
                        "4.Show Pending Reports.\n"
                        "5.Go back.\n"
                        )

            option.get(ans)[1](conn)

        except Exception as e:
            print("Invalid Choice. Please select again!")
            Admin.admin_report_management(self)

    def show_all_reports(self):
        """
        Shows all the report history.
        :return:
        """
        try:
            sql = "Select r.id,r.complaint_id,r.team_no,r.root_cause,r.details,r.status,c.accident_name,c.comments from Report r join Complaints c on r.complaint_id = c.id"
            result = cursor.execute(sql)

            for i in result:
                print("Report Id : {}".format(i[0]))
                print("Complaint Id : {}".format(i[1]))
                print("Team Number : {}".format(i[2]))
                print("Root Cause : {}".format(i[3]))
                print("Details : {}".format(i[4]))
                print("Status : {}".format(i[5]))
                print("Accident Name : {}".format(i[6]))
                print("Comments : {}".format(i[7]))
                print("----------------------------")


        except Exception as e:
            print("Error in reading data")
        finally:
            Admin.admin_report_management(self)

    def show_approved_reports(self):
        """
        Shows the list of reports approved by Admin.
        :return:
        """
        try:
            sql = "Select r.id,r.complaint_id,r.team_no,r.root_cause,r.details,c.accident_name,c.comments from Report r join Complaints c on r.complaint_id = c.id where r.status = 'approved'"
            result = cursor.execute(sql)

            for i in result:
                print("Report Id : {}".format(i[0]))
                print("Complaint Id : {}".format(i[1]))
                print("Team Number : {}".format(i[2]))
                print("Root Cause : {}".format(i[3]))
                print("Details : {}".format(i[4]))
                print("Accident Name : {}".format(i[5]))
                print("Comments : {}".format(i[6]))
                print("----------------------------")


        except Exception as e:
            print("Error in reading data")
        finally:
            Admin.admin_report_management(self)

    def show_rejected_reports(self):
        """
        Shows the list of all the reports rejected by Admin.
        :return:
        """
        try:
            sql = "Select r.id,r.complaint_id,r.team_no,r.root_cause,r.details,c.accident_name,c.comments from Report r join Complaints c on r.complaint_id = c.id where r.status = 'rejected'"
            result = cursor.execute(sql)

            for i in result:
                print("Report Id : {}".format(i[0]))
                print("Complaint Id : {}".format(i[1]))
                print("Team Number : {}".format(i[2]))
                print("Root Cause : {}".format(i[3]))
                print("Details : {}".format(i[4]))
                print("Accident Name : {}".format(i[5]))
                print("Comments : {}".format(i[6]))
                print("----------------------------")


        except Exception as e:
            print("Error in reading data")
        finally:
            Admin.admin_report_management(self)

    def show_pending_reports(self):
        """
        Shows the list of reports that are pending and admin
        either accepts or rejects.
        :return:
        """
        try:
            sql = "Select r.id,r.complaint_id,r.team_no,r.root_cause,r.details,r.status,c.accident_name,c.comments from Report r join Complaints c on r.complaint_id = c.id where r.status = 'none'"
            result = cursor.execute(sql)

            for i in result:
                print("Report Id : {}".format(i[0]))
                print("Complaint Id : {}".format(i[1]))
                print("Team Number : {}".format(i[2]))
                print("Root Cause : {}".format(i[3]))
                print("Details : {}".format(i[4]))
                print("Accident Name : {}".format(i[5]))
                print("Comments : {}".format(i[6]))
                print("----------------------------")

            r_id = int(input("Enter Report Id: "))
            val = input("Enter 'a' to Approve or 'r' to Reject: ")
            if val is 'a':
                sql = 'update Report set status = "approved" where id = ?'
                cursor.execute(sql, (r_id,))
                conn.commit()
                print("Report approved successfully!")
                get_cid = 'select complaint_id from Report where id = ?'
                res = cursor.execute(get_cid, (r_id,))
                for i in res:
                    Admin.c_id = i[0]
                sql1 = 'update Complaints set status = "closed" where id = ?'
                cursor.execute(sql1, (Admin.c_id,))
                conn.commit()
            elif val is 'r':
                sql = 'update Report set status = "rejected" where id = ?'
                cursor.execute(sql, (r_id,))
                conn.commit()
                print("Report Rejected successfully!")

            else:
                print("Wrong Choice. Please Enter again!")
                Admin.show_pending_reports(self)

        except Exception as e:
            print("Error in reading data")
        finally:
            Admin.admin_report_management(self)
