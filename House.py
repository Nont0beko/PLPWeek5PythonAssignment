class House:
    def __init__(self, address, num_rooms, area, price):
        self.address = address
        self.num_rooms = num_rooms
        self.area = area  # in square meters
        self.__price = price  # private attribute

    def show_details(self):
        print(f"Address: {self.address}")
        print(f"Rooms: {self.num_rooms}")
        print(f"Area: {self.area} sqm")
        print(f"Price: ${self.__price}")

    def renovate(self, added_rooms):
        self.num_rooms += added_rooms
        print(f"House renovated! Total rooms now: {self.num_rooms}")

    def get_price(self):  # getter for private attribute
        return self.__price

    def set_price(self, new_price):  # setter with validation
        if new_price > 0:
            self.__price = new_price
            print(f"Price updated to ${self.__price}")
        else:
            print("Invalid price. Update failed.")


class SmartHouse(House):
    def __init__(self, address, num_rooms, area, price, automation_level):
        super().__init__(address, num_rooms, area, price)
        self.automation_level = automation_level  # e.g., "Basic", "Advanced"

    # Polymorphism - override show_details
    def show_details(self):
        super().show_details()
        print(f"Automation Level: {self.automation_level}")

    def activate_voice_control(self):
        print(" Voice control activated! You can now control your house with your voice.")


        