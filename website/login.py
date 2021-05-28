import os
import pickle

login_file = os.path.join("website", "login.pkl")

with open(login_file, "wb") as login:
    pickle.dump("logged-out", login)


class LoginManager():

    def __init__(self):
        self.login_user = None
        self.logout_user = None

        self.logged_in = "logged-in"
        self.logged_out = "logged-out"

    def login(self, user):
        self.login_user = user
        with open(login_file, "wb") as file:
            pickle.dump(self.logged_in, file)

    def logout(self, user):
        self.logout_user = user
        with open(login_file, "wb") as file:
            pickle.dump(self.logged_out, file)

    def get_info(self):
        with open(login_file, "rb") as e:
            self.current_situation = pickle.load(e)
        return self.current_situation
