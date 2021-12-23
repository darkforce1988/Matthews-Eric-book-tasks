class Restaurant():
    """Model of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe a restaurant with it's name and cuisine type"""
        print(f"'{self.restaurant_name}' restaurant have the "
              f"{self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Display information about restaurant is being opened"""
        print(f"'{self.restaurant_name}' restaurant is opened now!")

    def set_number_served(self, served_clients):
        """Set the number of clients served"""
        self.number_served = served_clients

    def increment_number_served(self, served_clients):
        """Increment the number of clients served"""
        self.number_served += served_clients


class IceCreamStand(Restaurant):
    """docstring for IceCreamStand"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        flavors = ['lime', 'chocolate', 'strawberry']
        self.flavors = flavors
        flavor = ''
        self.flavor = flavor

    def show_flavors_list(self):
        """show the list of available flavors"""
        print("Available flavors for your ice cream are:")
        for self.flavor in self.flavors:
            print(f"\t- {self.flavor}")


my_ice_cream = IceCreamStand('Power', 'Russian')
my_ice_cream.show_flavors_list()
