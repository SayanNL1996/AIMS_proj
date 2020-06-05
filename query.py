from database_connection import DatabaseConnection

conn = DatabaseConnection.dbconnection()
cursor = conn.cursor()


class Queries:
    report_fields = '(complaint_id,team_no,root_cause,details,no_of_people_effected,death_rate)'
    complaint_fields = '(accident_name, comments, worker_id)'
    worker_fields = '(name,email,password)'
    supervisor_fields = '(name,email,password,Team_Number)'

    def __init__(self):
        pass

    def create(self, table_name, data):
        """
        Perform Write operation in DB
        :param table_name: table name
        :param data: values to be inserted
        :return: return to main statement
        """
        fields = None

        if table_name is 'Report':
            fields = Queries.report_fields
        elif table_name is 'Complaints':
            fields = Queries.complaint_fields
        elif table_name is 'Employees':
            fields = Queries.worker_fields
        elif table_name is 'Supervisors':
            fields = Queries.supervisor_fields

        try:
            query = 'INSERT INTO {table_name} {fields} VALUES {values}'.format(
                table_name=table_name, fields=fields, values=data
            )

            print(query)
            cursor.execute(query)
            conn.commit()
            print("Successfully created!")
            return

        except Exception as e:
            print("error occured", e)

    def update(self, table_name, data, field, value):
        """
        Update Operation in DB
        :param table_name: table name
        :param data: Values to be updated
        :param field: query field
        :param value: query value
        :return:
        """

        try:
            query = 'UPDATE {table_name} SET {data}WHERE {field} = "{value}"'.format(
                table_name=table_name, data=data, field=field, value=value
            )

            self.cursor.execute(query)
            self.conn.commit()

            print('Successfully Updated !\n')

        except Exception:
            print("Error Updating to DB !\n")

    def delete(self, table_name, field, value):
        """
        Delete Operation in DB
        :param table_name: table name
        :param field: column in which delete operation is performed
        :param value: value o be deleted
        :return:
        """

        try:
            query = 'DELETE FROM {table_name} WHERE {field} = "{value}"'.format(
                table_name=table_name, field=field, value=value
            )
            print(query)

            cursor.execute(query)
            conn.commit()

            print('Successfully Deleted !\n')
            return

        except Exception:
            print("Error Deleting from DB !\n")
