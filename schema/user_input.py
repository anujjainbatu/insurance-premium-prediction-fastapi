from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities

# pydantic model for input data
class UserInput(BaseModel):

    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the user", example=30)]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user in kg", example=70.0)]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description="Height of the user in meters", example=1.75)]
    income_lpa: Annotated[float, Field(..., gt=0, description="Income of the user in lakhs per annum", example=10.0)]
    smoker: Annotated[bool, Field(..., description="Is the user a smoker?", example=False)]
    city: Annotated[str, Field(..., description="City of the user", example="New York")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the user", example="business_owner")]
    
    @field_validator('city')
    @classmethod
    def validate_city(cls, v) -> str:
        v = v.strip().title()
        return v
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 24.9:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 45:
            return "middle-aged"
        else:
            return "senior"
        
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3