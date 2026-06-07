from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()


def load_data():
    # Simulate loading data from a database or file
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {"message": "Patient management system API is running!"}


@app.get("/about")
def about():
    return {"message": "A fully functional patient management system record."}


@app.get('/view')
def view():
    data = load_data()
    return {"patients": data}


@app.get('/patient/{patient_id}')
def view_patient(
    patient_id: str = Path(..., description="The ID of the patient to retrieve")
):
    data = load_data()

    if patient_id in data:
        return {"patient": data[patient_id]}
    else:
        raise HTTPException(status_code=404, detail="Patient not found")


@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"),
    order: str = Query(
        'asc',
        description="Sort order: 'asc' for ascending, 'desc' for descending"
    )
):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}"
        )

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort order. Valid orders are: 'asc' or 'desc'"
        )

    data = load_data()

    reverse_order = True if order == 'desc' else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=reverse_order
    )

    return {"sorted_patients": sorted_data}