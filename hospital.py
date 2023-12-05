# hospital.py

from patient import Patient
from doctor import Doctor

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = {}
        self.doctors = {}
        self.patient_counter = 1
        self.doctor_counter = 1

    def register_patient(self, name, gender, age):
        patient_id = self.patient_counter
        self.patients[patient_id] = Patient(name, gender, age)
        self.patient_counter += 1
        return patient_id

    def register_doctor(self, name, specialty):
        doctor_id = self.doctor_counter
        self.doctors[doctor_id] = Doctor(name, specialty)
        self.doctor_counter += 1
        return doctor_id

    def assign_doctor_to_patient(self, patient_id, doctor_id):
        patient = self.patients.get(patient_id)
        doctor = self.doctors.get(doctor_id)

        if patient and doctor:
            patient.assign_doctor(doctor_id)

    def display_patient_information(self, patient_id):
        patient = self.patients.get(patient_id)

        if patient:
            print(patient.get_info())
