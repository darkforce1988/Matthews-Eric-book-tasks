class Restaurant():
    """Model of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe a restaurant with it's name and cuisine type"""
        print(f"'{self.restaurant_name}' restaurant have the "
              f"{self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Display information about restaurant is being opened"""
        print(f"'{self.restaurant_name}' restaurant is opened now!")


restaurant_1 = Restaurant('Foods', 'French')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('Dranik Style', 'Belorussian')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Narrow Eyes', 'Chinese')
restaurant_3.describe_restaurant()
