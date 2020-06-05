from authentication import auth
from users.admin import Admin
from users.supervisors import Supervisor
from users.worker import Worker



class Login:
    def __init__(self):
        pass

    def login(self):
        """
        Takes the credentials,validates them and redirects to specific user tasks.
        :return:
        """
        try:
            print("WELCOME TO AIMS!!\n")
            print("Login as: \n"
                  "1: Admin \n"
                  "2: Supervisor \n"
                  "3: Member\n")
            num = int(input("Select user: "))
            if num in [1, 2, 3]:
                email = input("Enter Email: ")
                password = input("Enter password: ")
                data = auth(email, password, num)

                if data['isboolean'] == 'True':
                    if num == 1:
                        Admin.__init__(self, data['data'])
                    elif num == 2:
                        Supervisor.__init__(self, data['data'])
                    else:
                        Worker.__init__(self, data['data'])

                else:
                    raise Exception
            else:
                print("Invalid Choice. Please Enter again: ")
                self.login()

        except Exception as e:
            print("Error", e)
            self.login()


log = Login()
log.login()
