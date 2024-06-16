class Events:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        self.participants = []
    
    def register_participant(self, participant_name):
        self.participants.append(participant_name)
    
    def get_participant_count(self):
        return len(self.participants)

    def display_event(self):
        print(f"Event: {self.name}, Date: {self.date}, Location: {self.location}, ")
        print(f"Total Participants: {self.get_participant_count()}")
        print("Participants:", ', '.join(self.participants))
    
   