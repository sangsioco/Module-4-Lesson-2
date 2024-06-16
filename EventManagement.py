from event_manager import Events
import os

events = {}  # Dictionary where the key is the name and value is the event object

def save_events_to_file():
    with open('event.txt', 'w') as file:
        for event in events.values():
            participants = ','.join(event.participants)
            file.write(f"{event.name},{event.date},{event.location},{participants}\n")

def load_events_from_file():
    if os.path.exists('event.txt'):
        with open('event.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                name = parts[0]
                date = parts[1]
                location = parts[2]
                participants = parts[3:]  # Handle multiple participants correctly
                event = Events(name, date, location)
                event.participants = participants
                events[name] = event

load_events_from_file()

while True:

    print("Event Planning Menu ")    
    print("\n1. Add event ")
    print("2. Register participant ")
    print("3. Display total participant count and name ")
    print("4. Save entry ")
    print("5. Exit application ")
    action = input("Enter your selection: ")
    if action == '5':
        print("Exiting Event Planning Application.")
        break
    try:
        if action == '1':
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            location = input("Enter event location: ")
            events[name] = Events(name, date, location)
            print("Event added.")
        elif action == '2':
            event_name = input("Enter event name: ")
            participant = input("Enter participant name: ")
            if event_name in events:
                events[event_name].register_participant(participant)
                print("Participant registered.")
            else:
                print("Event not found.")
        elif action == '3':
            for event in events.values():
                event.display_event()
        elif action == '4':
            save_events_to_file()
            print("Events saved to file.")
    except Exception as e:
        print(f"An error occurred: {e}")
