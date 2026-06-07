from pydantic import BaseModel, model_validator
from typing import List, Dict


class Patient(BaseModel):

    name: str
    age: int
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):

        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError(
                'Patients older than 60 must have an emergency contact'
            )

        return model


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)

    print("Updated Successfully")


patient_info = {

    'name': 'Nitish',

    'age': 65,

    'married': False,

    'allergies': ['dust', 'pollen'],

    'contact_details': {
        'phone': '1234567890',
        'emergency': '9876543210'
    }
}


patient1 = Patient(**patient_info)

update_patient_data(patient1)