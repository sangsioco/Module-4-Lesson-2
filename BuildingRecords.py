import os

class Building:
    shared_facilities = ['Gym', 'Swimming Pool', 'Parking Lot']

    def __init__(self, name, number_floors):
        self.name= name
        self.number_of_floors = number_floors
        self.occupied_floors = 0

    def update_occupancy(self, change):
        if 0 <= self.occupied_floors + change <+ self.number_of_floors:
            self.occupied_floors += change
            return True
        return False
    
    def available_floors(self):
        return self.number_of_floors - self.occupied_floors

    def occupancy_rate(self):
        return (self.occupied_floors / self.number_of_floors) * 100
    

buildings = []

def save_building_to_file():
    with open('building_list.txt', 'w') as file:
        for building in buildings:
            file.write(f"{building.name},{building.number_of_floors}\n")

def load_building_from_file():
    buildings.clear()  # Clear existing buildings before loading
    if os.path.exists('building_list.txt'):
        with open('building_list.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                name = parts[0]
                number_of_floors = int(parts[1])
                buildings.append(Building(name, number_of_floors))
    else:
        print("Building list file not found.")

load_building_from_file()

while True:
    print("Building Management Application ")
    print("1. Add building ")
    print("2. Update building information ")
    print("3. Display list ")
    print("4. Save building list to a txt file")
    print("5. Upload building list from a txt file")
    print("6. Exit Application ")
    action = input("Enter your selection: ")
    if action == '6':
        print("Exiting Building Management Application.")
        break
    
    try:
        if action == '1':
            name = input("Enter building name: ")
            floors = int(input("Enter number of floors: "))
            buildings.append(Building(name, floors))
            print(f"Building '{name}' added with {floors} floors.")
        
        elif action == '2':
            name = input("Enter building name to update floor count: ")
            change = int(input("Enter change in number of floors: "))
            for building in buildings:
                if building.name == name:
                    if building.update_occupancy(change):
                        print(f"Updated occupancy for '{name}'.")
                    else:
                        print("Invalid occupancy change.")
                    break
            else:
                print("Building not found.")
        elif action == '3':
            for building in buildings:
                print(f"{building.name}: {building.available_floors()} available floors,"
                      f"Occupancy rate: {building.occupancy_rate():.2f}%")
        elif action == '4':
            save_building_to_file()
            print("Building list saved to file.")
        
        elif action == '5':
            load_building_from_file()
            print("Building list loaded from file.")
        
    except ValueError:
        print("Invalid input, please enter numberic values for units.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Apartment managemene system closed.")


