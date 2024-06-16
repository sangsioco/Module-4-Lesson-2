from my_bus import Bus

class Transportation:
    def __init__(self):
        self.buses = []
        self.available_routes = [101, 102, 103, 104, 105]  # Predefined bus routes
        self.available_cities = ['Metropolis', 'Starling City', 'Central City', 'Gotham City', 'Smallville']

    def add_bus(self, bus):
        self.buses.append(bus)

    def list_buses(self):
        if not self.buses:
            print("No buses available.")
        else:
            for bus in self.buses:
                bus.display_info()
                print()

    def find_bus_by_route(self, route_number):
        for bus in self.buses:
            if bus.route_number == route_number:
                return bus
        return None
    
    def find_bus_by_city(self, city_name):
        buses_in_city = []
        for bus in self.buses:
            if Bus.city_name[bus.city_index] == city_name:
                buses_in_city.append(bus)
        return buses_in_city

    def input_bus_details(self):
        print("Available Routes:", self.available_routes)
        print("Available Cities:")
        for index, city in enumerate(self.available_cities):
            print(f"{index}: {city}")

        try:
            route_number = int(input("Enter route number from the available routes: "))
            if route_number not in self.available_routes:
                print("Invalid route number. Please select a valid route.")
                return

            city_index = int(input("Select city from city list: "))
            if city_index < 0 or city_index >= len(self.available_cities):
                print("Invalid city index. Please select a valid index.")
                return

            passenger_capacity = int(input("Enter passenger capacity: "))
            new_bus = Bus(route_number, passenger_capacity, city_index)
            self.add_bus(new_bus)
            print("Bus added successfully!")
        except ValueError:
            print("Invalid input. Please enter numeric values for route number, city index, and passenger capacity.")

    def manage_routes(self):
        while True:
            print("\n--- Transportation Management System ---")
            print("1. Add Bus")
            print("2. List Buses")
            print("3. Find Bus by Route Number")
            print("4. Find Bus by city")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.input_bus_details()
            elif choice == '2':
                self.list_buses()
            elif choice == '3':
                try:
                    route_number = int(input("Enter route number to find: "))
                    bus = self.find_bus_by_route(route_number)
                    if bus:
                        bus.display_info()
                    else:
                        print(f"No bus found with route number {route_number}")
                except ValueError:
                    print("Invalid input. Please enter a numeric value for route number.")
            elif choice == '4':
                try:
                    city_name = input("Enter the name of the city to find route: ")
                    buses = self.find_bus_by_city(city_name)
                    if buses:
                        for bus in buses:
                            bus.display_info()
                    else:
                        print(f"No buses found in {city_name}")
                except ValueError:
                    print("Invalid input. City not available.")
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    transport_system = Transportation()
    transport_system.manage_routes()
