# def insert_patient_data(name: str, age: int):
#     if isinstance(name, str) and isinstance(age, int):
#         print(name)
#         print(age)
#     else:
#         raise ValueError("Invalid input")


# insert_patient_data("John Doe", 30)



#  now using pydantic

from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50)]
    age: Annotated[int, Field(gt=0, lt=120)]
    weight: Annotated[float, Field(gt=0)]
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Optional[Dict[str, str]] = None


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

    print("Inserted successfully")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)

    print("Updated successfully")


patient_info = {
    'name': 'nitish',
    'age': 25,
    'weight': 70.5,
    'married': False,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'email': 'nitish@example.com',
        'phone': '123-456-7890'
    }
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
insert_patient_data(patient1)