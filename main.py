# main.py

from hospital import Hospital

def main():
    hospital = Hospital("General Hospital")

    # Example usage
    patient_id = hospital.register_patient("John Doe", "Male", 30)
    doctor_id = hospital.register_doctor("Dr. Smith", "Cardiologist")

    hospital.assign_doctor_to_patient(patient_id, doctor_id)
    hospital.display_patient_information(patient_id)

if __name__ == "__main__":
    main()
