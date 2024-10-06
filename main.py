import joblib
from fastapi import FastAPI
from pydantic import BaseModel

class Request(BaseModel):
    petal_length: float
    petal_width: float
    sepal_length: float
    sepal_width: float

app = FastAPI()

@app.get("/")
def read_root():
    return  {"Hello": "Ziya"}

@app.post("/predict")
def predict(req:Request):
    filename = "model.sav"

    # load the model from disk
    loaded_model = joblib.load(filename)

    res = loaded_model.predict([[req.sepal_length, req.sepal_width, req.petal_length, req.petal_width]])
    mapping_label = {0:"Setosa", 1:"Versicolor", 2:"Virginica"}
    label = mapping_label[res[0]]

    return {"prediction": label}

