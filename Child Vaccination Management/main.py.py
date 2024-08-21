import datetime

class Child:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.vaccination_records = []

    def add_vaccination_record(self, vaccine, date_given):
        self.vaccination_records.append({'vaccine': vaccine, 'date_given': date_given})
    
    def view_vaccination_records(self):
        return self.vaccination_records


class VaccinationSystem:
    def __init__(self):
        self.children = {}
        self.vaccination_schedule = {
            'BCG': 'Birth',
            'Polio': '6 weeks',
            'DPT': '6 weeks',
            'MMR': '9 months'
        }

    def add_child(self, name, dob):
        if name not in self.children:
            self.children[name] = Child(name, dob)
        else:
            print(f"Child named {name} already exists.")

    def view_vaccination_schedule(self):
        return self.vaccination_schedule

    def book_appointment(self, child_name, vaccine):
        if child_name in self.children:
            child = self.children[child_name]
            due_date = self.calculate_due_date(child.dob, vaccine)
            print(f"Appointment booked for {child_name} on {due_date} for {vaccine} vaccine.")
            return due_date
        else:
            print(f"No child found with the name {child_name}.")
            return None
    
    def send_reminder(self, child_name, vaccine):
        due_date = self.book_appointment(child_name, vaccine)
        if due_date:
            print(f"Reminder: {vaccine} vaccination for {child_name} is due on {due_date}.")

    def calculate_due_date(self, dob, vaccine):
        # Assuming 'dob' is a datetime.date object
        if vaccine in self.vaccination_schedule:
            schedule = self.vaccination_schedule[vaccine]
            if schedule == 'Birth':
                return dob
            weeks = int(schedule.split()[0])
            due_date = dob + datetime.timedelta(weeks=weeks)
            return due_date
        else:
            print(f"No schedule found for {vaccine}.")
            return None

    def view_updates(self, child_name):
        if child_name in self.children:
            child = self.children[child_name]
            records = child.view_vaccination_records()
            print(f"Vaccination records for {child_name}:")
            for record in records:
                print(f"Vaccine: {record['vaccine']}, Date Given: {record['date_given']}")
        else:
            print(f"No updates found for {child_name}.")


# Example Usage
system = VaccinationSystem()
system.add_child("AKHIL", datetime.date(2023, 1, 1))
system.view_vaccination_schedule()
system.book_appointment("AKHIL", "Polio")
system.send_reminder("AKHIL", "DPT")
system.view_updates("AKHIL")

