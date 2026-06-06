from fastapi import FastAPI
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

