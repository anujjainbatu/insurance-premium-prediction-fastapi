from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, Model_VERSION

app = FastAPI()

#human readable message        
@app.get("/")
def home():
    return JSONResponse(status_code=200, content={"message": "Welcome to the Health Insurance Premium Prediction API!"})

#machine readable message
@app.get("/health")
def health_check():
    return JSONResponse(status_code=200, content={"status": "healthy", "model_loaded": model is not None , "message": "API is running smoothly!", "version": Model_VERSION})
        
@app.post("/predict", response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'lifestyle_risk': data.lifestyle_risk,
        'age_group': data.age_group,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    try:
        output = predict_output(user_input)
        return JSONResponse(status_code=200, content={"response": output})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e), "message": "An error occurred while processing the request."})