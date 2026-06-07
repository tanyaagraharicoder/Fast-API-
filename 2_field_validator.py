
from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50)]
    age: Annotated[int, Field(gt=0, lt=120)]
    weight: Annotated[float, Field(gt=0)]

    married: bool

    allergies: Optional[List[str]] = None

    contact_details: Optional[Dict[str, str]] = None

    email: str

    @field_validator('email')
    @classmethod
   
    def validate_bank_email(cls, value):

        allowed_domains = ['sbi.com', 'icici.com']

        domain = value.split('@')[-1]

        if domain not in allowed_domains:
            raise ValueError(
                'Email must belong to SBI or ICICI bank employee'
            )

        return value


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.email)

    print("Inserted Successfully")


patient_info = {
    'name': 'Nitish',
    'age': 25,
    'weight': 70.5,
    'married': False,
    'allergies': ['dust', 'pollen'],

    'contact_details': {
        'phone': '1234567890'
    },

    'email': 'nitish@sbi.com'
}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)