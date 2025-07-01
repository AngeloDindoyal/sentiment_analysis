import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), "text_pipeline.joblib")
model = joblib.load(model_path)

def predict_sentiment(data):
    
    result = model.predict([data])

    if result == 0: 
        return "positive"
    else:
        return "negative"

    return resul