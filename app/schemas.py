from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(UserCreate):
    id: int

# ML Schemas
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisPrediction(BaseModel):
    features: IrisFeatures
    prediction: str
    probability: List[float]
    flower_types: List[str] = ["Setosa", "Versicolor", "Virginica"]
