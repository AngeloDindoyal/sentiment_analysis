from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from utils.Clean import clean
from utils.Predict import predict_sentiment


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(data: TextInput):
    #Clean data
    data = clean(data.text)

    #Preprocess and Predict Pipeline
    result = predict_sentiment(data)

    return {"prediction": result}

if __name__ == "__main__": 
    uvicorn.run("app:app")