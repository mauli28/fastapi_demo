# Machine Learning Demo - Iris Flower Classification

This FastAPI project includes a complete ML demo that demonstrates machine learning in action using the Iris flower dataset.

## 🌸 What's Included

### Machine Learning Features
- **Iris Flower Classification**: Uses Random Forest Classifier trained on the famous Iris dataset
- **Real-time Predictions**: Get instant predictions based on flower measurements
- **Confidence Scores**: See prediction confidence as probability bars
- **Batch Predictions**: Predict multiple flowers at once via API
- **Model Information**: View model accuracy and dataset details

### API Endpoints

#### Single Prediction
```
POST /ml/iris/predict
Content-Type: application/json

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Response:
```json
{
  "features": {...},
  "prediction": "Setosa",
  "probability": [0.98, 0.02, 0.0],
  "flower_types": ["Setosa", "Versicolor", "Virginica"]
}
```

#### Model Information
```
GET /ml/iris/info
```

#### Batch Predictions
```
POST /ml/iris/batch
Content-Type: application/json

[
  {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2},
  {"sepal_length": 5.9, "sepal_width": 3.0, "petal_length": 4.2, "petal_width": 1.5}
]
```

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
uvicorn app.main:app --reload
```

### 3. Access the Demo

- **Interactive ML Demo**: http://localhost:8000/ml-demo.html
- **API Documentation**: http://localhost:8000/docs
- **Home Page**: http://localhost:8000/

## 📊 Try the Examples

The ML demo includes pre-loaded example data for three iris types:

1. **Setosa** (Sepal: 5.1 x 3.5, Petal: 1.4 x 0.2)
2. **Versicolor** (Sepal: 5.9 x 3.0, Petal: 4.2 x 1.5)
3. **Virginica** (Sepal: 6.3 x 3.3, Petal: 6.0 x 2.5)

## 🤖 Model Details

- **Model Type**: Random Forest Classifier
- **Number of Trees**: 10
- **Training Data**: 80% of Iris dataset
- **Test Data**: 20% of Iris dataset
- **Features**:
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)

## 📁 Project Structure

```
fastapi_demo/
├── app/
│   ├── main.py           # FastAPI application setup
│   ├── routes.py         # API routes (users + ML endpoints)
│   ├── schemas.py        # Pydantic models (data validation)
│   ├── models.py         # Database models
│   └── static/
│       ├── index.html    # Home page
│       └── ml-demo.html  # Interactive ML demo UI
├── requirements.txt      # Project dependencies
└── ML_DEMO.md           # This file
```

## 🔧 Dependencies Added

- **scikit-learn**: Machine learning algorithms
- **numpy**: Numerical computing
- **pandas**: Data manipulation (optional but useful)

## 💡 Learning Outcomes

By exploring this demo, you'll learn:
- How to integrate ML models with FastAPI
- Building RESTful APIs for ML predictions
- Frontend-backend communication with ML
- Using scikit-learn for classification tasks
- Creating responsive web UIs for ML applications

## 🎓 Next Steps

Try extending this demo by:
- Adding more ML models (regression, clustering, NLP)
- Implementing model training endpoints
- Adding data validation and error handling
- Creating visualizations for predictions
- Building a model comparison feature
- Implementing feature importance visualization

## 📝 Notes

- The model is pre-trained on startup for demo purposes
- In production, you'd typically load pre-trained models from disk
- The demo uses the classic Iris dataset from UCI ML Repository
- All predictions happen in real-time with millisecond response times

Enjoy learning ML with FastAPI! 🚀
