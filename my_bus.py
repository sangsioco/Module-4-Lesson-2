
class Bus:
    # Class variables
    city_name = ['Metropolis', 'Starling City', 'Central City', 'Gotham City', 'Smallville']
    bus_fare = ['$2.50', '$3.50', '$5.00', '$3.00', '$4.50']

    def __init__(self, route_number, passenger_capacity, city_index):
        # Instance variables
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity
        self.city_index = city_index  # Index to select city and fare

    def display_info(self):
        print(f"City: {Bus.city_name[self.city_index]}")
        print(f"Base Fare: {Bus.bus_fare[self.city_index]}")
        print(f"Route Number: {self.route_number}")
        print(f"Passenger Capacity: {self.passenger_capacity}")
