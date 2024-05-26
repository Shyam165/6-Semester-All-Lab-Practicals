class User:

    def login(self):
        print("Login")

    def register(self):
        print("Register")

class Student(User):

    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")


std = Student()

std.enroll()
std.review()
std.login()
std.register()
