from database_connection import connect

conn = connect()
cursor = conn.cursor()


def auth(email, password, num):
    """
    authentication of user is done.
    :param email: email of the user
    :param password: password of the user
    :param num: the task id
    :return: returns boolean value along with the user id.
    """
    try:

        if num == 1:
            find_user = "select * from Admin where email = ? and password = ?"
        elif num == 2:
            find_user = "select * from Supervisors where email = ? and password = ?"
        else:
            find_user = "select * from Employees where email = ? and password = ?"

        cursor.execute(find_user, [email, password])
        results = cursor.fetchall()

        if results:
            return {'isboolean': 'True', 'data': results[0][0]}
        else:
            raise Exception


    except Exception as e:
        print('Wrong Credentials. Please Enter again!')
        return Exception
