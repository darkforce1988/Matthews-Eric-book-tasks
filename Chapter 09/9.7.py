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


class Admin(User):
    """A class to model an admin"""
    def __init__(self, first_name, last_name, email_address, register_date):
        super().__init__(first_name, last_name, email_address, register_date)
        privileges = [
                      'allowed message edition',
                      'allowed user banning',
                      'allowed user deletion',
                      ]
        self.privileges = privileges

    def show_privileges(self):
        """Show admin privileges"""
        print("Do not write spam messages! Admin have the following rights:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")


admin_account = Admin('Max', 'Auramenka', 'titan@tut.by', '19.12.2021')
admin_account.show_privileges()
