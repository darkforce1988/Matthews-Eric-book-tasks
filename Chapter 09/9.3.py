class User():
    """A class to model a user"""
    def __init__(self, first_name, last_name, email_address, register_date):
        """Initialize first, last name, email and register date attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.register_date = register_date

    def describe_user(self):
        """Describe a user with his name, email and registration date"""
        print(f"Current user information:\n\t"
              f"- first name: {self.first_name},\n\t"
              f"- last name: {self.last_name},\n\t"
              f"- email address: {self.email_address},\n\t"
              f"- registration date: {self.register_date}.\n")

    def greet_user(self):
        """Greet a user"""
        name = self.first_name + ' ' + self.last_name
        print(f"Hello, {name}!\n")


user_1 = User('Max', 'Auramenka', 'titan@tut.by', '19.12.2021')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Jan', 'Paciypa', 'patsiypa@tut.by', '18.12.1993')
user_2.describe_user()
user_2.greet_user()

user_3 = User('Alexander', 'Vaitsekhovich', 'alex01@mail.ru', '01.01.2001')
user_3.describe_user()
user_3.greet_user()
