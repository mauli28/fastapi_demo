# FastAPI ML Demo - Iris Flower Classification

A complete FastAPI project demonstrating machine learning integration with an interactive web interface. This project includes a fully trained Random Forest classifier for iris flower classification.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [Accessing the Application](#accessing-the-application)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Learning Resources](#learning-resources)

## 🎯 Overview

This project is a learning resource that combines:
- **FastAPI** - Modern, fast web framework for building APIs
- **Machine Learning** - Scikit-learn for flower classification
- **Interactive UI** - Beautiful HTML/JavaScript frontend for real-time predictions

Perfect for learning how to integrate ML models with web applications!

## ✨ Features

### 🌸 ML Capabilities
- Real-time iris flower classification
- Confidence scores displayed as probability bars
- Model accuracy information (typically 95%+)
- Batch prediction support
- Example data for quick testing

### 🎨 Web Interface
- Responsive, modern UI
- Real-time predictions without page reload
- Visual probability bars
- Pre-loaded flower examples
- Model information dashboard
- Error handling and validation

### 📡 REST API
- Full API documentation (Swagger UI)
- Three ML endpoints for different use cases
- Type-safe request/response validation
- Easy integration with external applications

## 📦 Prerequisites

Before you begin, ensure you have:
- **Python 3.8+** (3.10+ recommended)
- **pip** (Python package manager)
- **Git** (optional, for version control)
- **Command line/Terminal** access

## 🚀 Installation

### Step 1: Clone or Download the Project
```bash
# If using git
git clone <repository-url>
cd fastapi_demo

# Or simply navigate to your project directory
```

### Step 2: Create a Virtual Environment (Recommended)

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `pydantic` - Data validation
- `scikit-learn` - Machine learning
- `numpy` - Numerical computing
- `pandas` - Data manipulation

**Verify Installation:**
```bash
pip list
```

You should see all packages listed with their versions.

## ▶️ Running the Server

### Start the FastAPI Application

```bash
uvicorn app.main:app --reload
```

**Output should show:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete
```

### Server Options

**With automatic reload (development):**
```bash
uvicorn app.main:app --reload
```

**With custom port:**
```bash
uvicorn app.main:app --port 8080
```

**With host binding (to access from other machines):**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**Production mode (no reload):**
```bash
uvicorn app.main:app
```

## 🌐 Accessing the Application

Once the server is running, open your browser:

### 🏠 Home Page
```
http://127.0.0.1:8000/
```
- Welcome page with links to API docs and ML demo

### 🌸 ML Demo (Interactive Interface)
```
http://127.0.0.1:8000/static/ml-demo.html
```
- Beautiful web interface for flower classification
- Enter measurements or use example buttons
- See real-time predictions with confidence scores

### 📚 API Documentation (Swagger UI)
```
http://127.0.0.1:8000/docs
```
- Interactive API documentation
- Test endpoints directly in the browser
- See request/response schemas

### 🔧 Alternative API Docs (ReDoc)
```
http://127.0.0.1:8000/redoc
```

## 📡 API Endpoints

### 1. Single Flower Prediction
**POST** `/ml/iris/predict`

Predict a single iris flower type.

**Request:**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

**Response:**
```json
{
  "features": {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  },
  "prediction": "Setosa",
  "probability": [0.98, 0.02, 0.0],
  "flower_types": ["Setosa", "Versicolor", "Virginica"]
}
```

### 2. Model Information
**GET** `/ml/iris/info`

Get model details and accuracy metrics.

**Response:**
```json
{
  "dataset": "Iris Flower Classification",
  "model": "Random Forest Classifier",
  "num_trees": 10,
  "test_accuracy": 0.9667,
  "flower_types": ["Setosa", "Versicolor", "Virginica"],
  "features": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
  "description": "Predicts iris flower type based on petal and sepal measurements"
}
```

### 3. Batch Predictions
**POST** `/ml/iris/batch`

Predict multiple flowers at once.

**Request:**
```json
[
  {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  },
  {
    "sepal_length": 5.9,
    "sepal_width": 3.0,
    "petal_length": 4.2,
    "petal_width": 1.5
  }
]
```

**Response:**
```json
{
  "predictions": [
    {...prediction 1...},
    {...prediction 2...}
  ],
  "count": 2
}
```

### 4. Health Check
**GET** `/health`

```json
{"status": "ok"}
```

### 5. Status Check
**GET** `/status`

```json
{"status": "running"}
```

### User Management Endpoints (CRUD)
**POST** `/users/` - Create user
**GET** `/users/` - List all users
**GET** `/users/{user_id}` - Get specific user

## 📁 Project Structure

```
fastapi_demo/
├── app/
│   ├── main.py                 # FastAPI app setup and configuration
│   ├── routes.py               # All API endpoints and ML model
│   ├── schemas.py              # Pydantic data models
│   ├── models.py               # Database models (if needed)
│   └── static/
│       ├── index.html          # Home page
│       └── ml-demo.html        # Interactive ML demo UI
├── venv/                       # Virtual environment (after setup)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── ML_DEMO.md                  # ML-specific documentation
└── SETUP_SUMMARY.md            # Implementation summary
```

### Key Files Explanation

| File | Purpose |
|------|---------|
| `app/main.py` | FastAPI application initialization, static file serving |
| `app/routes.py` | ML endpoints, model training, prediction logic |
| `app/schemas.py` | Pydantic models for request/response validation |
| `app/static/ml-demo.html` | Interactive web interface with JavaScript |
| `requirements.txt` | List of Python dependencies and versions |

## 🧠 Example Iris Data

Three iris species with typical measurements:

### Setosa
- Sepal Length: 5.1 cm
- Sepal Width: 3.5 cm
- Petal Length: 1.4 cm
- Petal Width: 0.2 cm

### Versicolor
- Sepal Length: 5.9 cm
- Sepal Width: 3.0 cm
- Petal Length: 4.2 cm
- Petal Width: 1.5 cm

### Virginica
- Sepal Length: 6.3 cm
- Sepal Width: 3.3 cm
- Petal Length: 6.0 cm
- Petal Width: 2.5 cm

## 📚 Learning Resources

### Understanding the Project

1. **FastAPI Documentation**
   - https://fastapi.tiangolo.com/
   - Learn about routing, request models, responses

2. **Scikit-learn Documentation**
   - https://scikit-learn.org/
   - Understand Random Forest and classification

3. **Pydantic Documentation**
   - https://docs.pydantic.dev/
   - Data validation and serialization

4. **Iris Dataset**
   - https://en.wikipedia.org/wiki/Iris_flower_data_set
   - Historical dataset used for machine learning

### Topics to Explore

- **ML Concepts**: Classification, decision trees, ensemble methods
- **Web Development**: REST APIs, HTTP, JSON
- **Python**: Virtual environments, pip, dependencies
- **Frontend**: HTML, CSS, JavaScript, async/await

## 🔧 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'sklearn'`
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Port 8000 is already in use
**Solution:** Use a different port
```bash
uvicorn app.main:app --port 8080
```

### Issue: 404 error when accessing ML demo
**Solution:** Make sure you're using the correct path
```
http://127.0.0.1:8000/static/ml-demo.html
```

### Issue: Virtual environment not activating
**Windows (PowerShell):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 🚀 Next Steps & Extensions

### Beginner Tasks
- [ ] Modify example data in the UI
- [ ] Change the number of trees in Random Forest
- [ ] Add CSS styling to the demo page

### Intermediate Tasks
- [ ] Add a new ML model (e.g., SVM, KNN)
- [ ] Create model comparison endpoint
- [ ] Add input data validation with error messages
- [ ] Store predictions in a database

### Advanced Tasks
- [ ] Implement model training endpoint
- [ ] Add feature importance visualization
- [ ] Create model persistence (save/load)
- [ ] Build a prediction history dashboard
- [ ] Add image upload for flower classification
- [ ] Deploy to cloud (Heroku, AWS, GCP)

## 💡 Tips for Learning

1. **Start with the UI** - Use `/static/ml-demo.html` to understand how predictions work
2. **Explore the API** - Use `/docs` to test endpoints directly
3. **Read the Code** - Comments in `routes.py` explain ML logic
4. **Experiment** - Try different measurements and see predictions change
5. **Modify Gradually** - Change one thing at a time and test

## 📝 Notes

- The ML model is trained on application startup
- In production, pre-trained models are typically loaded from disk
- The Iris dataset is a classic ML benchmark (150 samples)
- Random Forest uses 10 trees for this demo (adjustable)
- Test accuracy is typically 96-97%

## 🤝 Contributing

Feel free to:
- Extend the project with new features
- Add more ML models
- Improve the UI
- Add more endpoints
- Fix bugs and improve code quality

## 📄 License

This project is provided as-is for educational purposes.

## ❓ Getting Help

1. Check the error message in the terminal
2. Review `ML_DEMO.md` for ML-specific questions
3. Look at FastAPI docs for framework questions
4. Test endpoints using the Swagger UI at `/docs`

---

**Happy Learning! 🎓** 

Enjoy exploring machine learning with FastAPI! Start with the interactive demo and gradually explore the API to deepen your understanding.
