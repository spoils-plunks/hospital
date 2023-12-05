# doctor.py

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def get_info(self):
        return f"Doctor: {self.name}, Specialty: {self.specialty}"
