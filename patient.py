# patient.py

class Patient:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.doctor_id = None

    def assign_doctor(self, doctor_id):
        self.doctor_id = doctor_id

    def get_info(self):
        return f"Patient: {self.name}, Gender: {self.gender}, Age: {self.age}, Doctor ID: {self.doctor_id}"
