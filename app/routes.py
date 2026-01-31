from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserResponse, IrisFeatures, IrisPrediction
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Routers
users_router = APIRouter(prefix="/users", tags=["Users"])
ml_router = APIRouter(prefix="/ml", tags=["Machine Learning"])

# Fake database
users_db = []

# ML Model - Load and train Iris classifier
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)
ml_model = RandomForestClassifier(n_estimators=10, random_state=42)
ml_model.fit(X_train, y_train)
flower_names = iris.target_names.tolist()

# Users endpoints
@users_router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    new_user = {"id": user_id, **user.dict()}
    users_db.append(new_user)
    return new_user

@users_router.get("/", response_model=list[UserResponse])
def get_users():
    return users_db

@users_router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# ML Endpoints
@ml_router.post("/iris/predict", response_model=IrisPrediction)
def predict_iris(features: IrisFeatures):
    """
    Predict Iris flower type based on sepal and petal measurements.
    
    Example:
    - sepal_length: 5.1
    - sepal_width: 3.5
    - petal_length: 1.4
    - petal_width: 0.2
    """
    input_features = np.array([[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]])
    
    prediction = ml_model.predict(input_features)[0]
    probabilities = ml_model.predict_proba(input_features)[0]
    
    return IrisPrediction(
        features=features,
        prediction=flower_names[prediction],
        probability=probabilities.tolist(),
        flower_types=flower_names
    )

@ml_router.get("/iris/info")
def iris_info():
    """
    Get information about the Iris dataset and model accuracy.
    """
    accuracy = ml_model.score(X_test, y_test)
    return {
        "dataset": "Iris Flower Classification",
        "model": "Random Forest Classifier",
        "num_trees": 10,
        "test_accuracy": round(accuracy, 4),
        "flower_types": flower_names,
        "features": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
        "description": "Predicts iris flower type based on petal and sepal measurements"
    }

@ml_router.post("/iris/batch")
def batch_predict(features_list: list[IrisFeatures]):
    """
    Predict multiple iris flowers at once.
    """
    results = []
    for features in features_list:
        result = predict_iris(features)
        results.append(result)
    return {"predictions": results, "count": len(results)}

# Export routers
router = APIRouter()
router.include_router(users_router)
router.include_router(ml_router)
