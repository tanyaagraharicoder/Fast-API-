from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict


class Patient(BaseModel):

    name: str
    age: int
    height: float
    weight: float
    email: EmailStr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:

        height_in_meters = self.height / 100

        bmi = self.weight / (height_in_meters ** 2)

        return round(bmi, 2)


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.height)
    print(patient.weight)
    print(patient.email)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

    print(f"BMI: {patient.calculate_bmi}")

    print("Updated Successfully")


patient_info = {

    'name': 'Nitish',

    'age': 25,

    'height': 175.0,

    'weight': 70.5,

    'email': 'nitish@example.com',

    'married': True,

    'allergies': ['peanuts', 'shellfish'],

    'contact_details': {
        'phone': '123-456-7890',
        'address': '123 Main St, City, State'
    }
}


patient = Patient(**patient_info)

update_patient_data(patient)