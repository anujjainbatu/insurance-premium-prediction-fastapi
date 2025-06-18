from pydantic import BaseModel, Field
from typing import Optional, List

# pydantic model for prediction response
class PredictionResponse(BaseModel):
    premium_category: str = Field(..., description="Predicted health insurance premium category", example="medium")
    confidence: float = Field(..., description="Confidence level of the prediction", example=0.85)
    class_probabilities: Optional[List[float]] = Field(None, description="Probabilities for each class label", example={"Low": 0.1, "Medium": 0.2, "High": 0.7})
    
    class Config:
        schema_extra = {
            "example": {
                "premium_category": "medium",
                "confidence": 0.85,
                "class_probabilities": {
                    "Low": 0.1,
                    "Medium": 0.2,
                    "High": 0.7
                }
            }
        }