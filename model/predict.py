import pickle
import pandas as pd

# import ml model
with open("model/model.pkl", "rb") as file:
    model = pickle.load(file)

#MLFLOW
Model_VERSION = "1.0.0"

# get class labels from the model
class_labels = model.classes_.tolist()

def predict_output(user_input: dict) -> str:
    """
    Predict the health insurance premium category based on user input.
    
    Args:
        user_input (dict): Dictionary containing user input data.
        
    Returns:
        str: Predicted health insurance premium category.
    """
    
    # Convert user input to DataFrame
    input_df = pd.DataFrame([user_input])
    
    # Make prediction
    predicted_class = model.predict(input_df)[0]

    # Get probabilities for all classes
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    # Create mapping of class labels to probabilities
    class_probs = dict(zip(class_labels, map(lambda x: round(x, 4), probabilities)))
    
    return {
        "premium_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }
