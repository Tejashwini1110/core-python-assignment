class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def __repr__(self):
        return self.name

# Function to search for patients by disease
def search_patients_by_disease(patients, disease):
#Function to find and return a list of patients with the given disease.
    return [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]

# Function to create patient records
def create_patient_records():
#Function to create and return a list of patient records.
    return [
        {"Name": "Alice", "Age": 30, "Disease": "Flu"},
        {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
        {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
    ]
# Input Example
patients = create_patient_records()
# Disease to search for
search_disease = "Flu"
# Searching for patients with the disease
patients_with_disease = search_patients_by_disease(patients, search_disease)
# Output the result
print(f"Patients with {search_disease}: {patients_with_disease}")
