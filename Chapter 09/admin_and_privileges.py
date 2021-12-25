from user import User


class Privileges():
    """A class to model a privileges"""

    def __init__(self):
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


class Admin(User):
    """A class to model an admin"""

    def __init__(self, first_name, last_name, email_address, register_date):
        super().__init__(first_name, last_name, email_address, register_date)
        self.privileges_list = Privileges()
