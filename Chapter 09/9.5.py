class User():
    """A class to model a user"""

    def __init__(self, first_name, last_name, email_address, register_date):
        """Initialize first, last name, email and register date attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.register_date = register_date
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increment the number of users trying to log in"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of users trying to log in"""
        self.login_attempts = 0


user = User('Max', 'Auramenka', 'titan@tut.by', '19.12.2021')

user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)
