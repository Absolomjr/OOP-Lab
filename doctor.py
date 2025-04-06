class Doctor:
    def __init__(self, name, specialization, years_of_experience):
        self.name = name
        self.specialization = specialization
        self.years_of_experience = years_of_experience
        self.appointments = []

    def display_appointments(self):
        print(f"\nAppointments for Dr. {self.name} ({self.specialization}):")
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            for appt in self.appointments:
                print(f"Patient: {appt.patient_name}, Date: {appt.date}, Status: {appt.status}")


class Appointment:
    def __init__(self, patient_name, date):
        self.patient_name = patient_name
        self.date = date
        self.status = "Scheduled"

    def schedule_appointment(self):
        self.status = "Scheduled"
        print(f"Appointment scheduled for {self.patient_name} on {self.date}.")

    def cancel_appointment(self):
        if self.status == "Scheduled":
            self.status = "Canceled"
            print(f"Appointment for {self.patient_name} on {self.date} has been canceled.")
        else:
            print(f"Cannot cancel appointment for {self.patient_name} on {self.date}. It is not currently scheduled.")


# === Example Usage ===

# Create a doctor
doctor = Doctor("John Smith", "Cardiology", 15)

# Create and schedule two appointments
appointment1 = Appointment("Alice", "2025-04-08")
appointment2 = Appointment("Bob", "2025-04-09")

appointment1.schedule_appointment()
appointment2.schedule_appointment()

# Add appointments to the doctor's list
doctor.appointments.append(appointment1)
doctor.appointments.append(appointment2)

# Cancel one appointment
appointment1.cancel_appointment()

# Try canceling again to test error handling
appointment1.cancel_appointment()

# Display all appointments
doctor.display_appointments()
