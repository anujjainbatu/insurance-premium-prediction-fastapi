# insurance-premium-prediction-fastapi

This project is an **Insurance Premium Prediction API** built with FastAPI. The main objective is not only to provide a working insurance premium prediction service, but also to serve as a blueprint for building industry-grade FastAPI applications. The codebase demonstrates best practices in API design, modular code organization, input/output validation, and production readiness.

## Features

- **FastAPI**: High-performance, easy-to-use Python web framework.
- **Modular Structure**: Clear separation of models, schemas, and API logic.
- **Input Validation**: Uses Pydantic for robust request/response validation.
- **Prediction Endpoint**: `/predict` endpoint for premium category prediction.
- **Health Check**: `/health` endpoint for service monitoring.
- **Interactive Docs**: Swagger UI available at `/docs`.
- **Error Handling**: Graceful error responses for invalid requests or server issues.
- **Production Ready**: Example `.gitignore`, clear project structure, and extensible code.

## Demo

Below is a demonstration of the working product:

![Insurance Premium Prediction API Demo](assets/demo.gif)

## Project Structure

```
insurance-premium-prediction/
│
├── app.py                      # Main FastAPI application
├── model/
│   └── predict.py              # Model loading and prediction logic
│   └── model.pkl               # Serialized ML model (not included in repo)
├── schema/
│   ├── user_input.py           # Pydantic model for input validation
│   └── prediction_response.py  # Pydantic model for output schema
├── venv/                       # Virtual environment (excluded from git)
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
└── ...
```

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd insurance-premium-prediction
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API**
   ```bash
   uvicorn app:app --reload
   ```

5. **Access the API**
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Health check: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

## Example Request

**POST** `/predict`

```json
{
  "bmi": 27.5,
  "lifestyle_risk": "medium",
  "age_group": "30-40",
  "city_tier": "tier_1",
  "income_lpa": 12,
  "occupation": "salaried"
}
```

**Response**
```json
{
  "premium_category": "Medium",
  "confidence": 0.85,
  "class_probabilities": {
    "Low": 0.1,
    "Medium": 0.2,
    "High": 0.7
  }
}
```

## Notes

- This project is intended as a reference for building scalable, maintainable FastAPI applications in a production setting.

## License

MIT License

---

**Blueprint for Industry-Grade FastAPI Apps**  
Use this project as a starting point for your own robust, production-ready APIs!
