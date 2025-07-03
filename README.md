Product Review Sentiment Analysis API 

#Model 
- Trained on this public dataset: https://www.kaggle.com/datasets/manasabollavarapu/amazon-product-reviews

#Features 
- Predict sentiment of text (positive or negative)
- Vectorization and Normalization of text done internally
- FastAPI with built in Swagger Docs

#Access: 
- Prediction endpoint: https://sentiment-analysis-arsn.onrender.com/predict
- POST endpoint
- Expects a JSON body:
{'text' : 'this is a great API' }
- Result is a JSON:
{'prediction' : 'positive'}
