# Mushroom Classification ML Project With MLOps Integration

## Overview

This repository contains a machine learning solution for mushroom classification with MLOps implementation. The project determines whether a mushroom is edible or poisonous based on various physical attributes, utilizing modern machine learning techniques and proper DevOps practices.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training Pipeline](#model-training-pipeline)
- [Web Application](#web-application)
- [Docker Deployment](#docker-deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
Mushroom_Prediction_ML_project/
├── .github/                   # GitHub workflow configurations
├── artifacts/                 # Generated model artifacts
├── config/                    # Configuration files
├── mlruns/                    # MLflow tracking files
├── research/                  # Jupyter notebooks for research and development
│   ├── data_ingestion.ipynb
│   ├── data_validation.ipynb
│   ├── data_transformation.ipynb
│   ├── model_trainer.ipynb
│   ├── model_evaluation.ipynb
│   └── mushrooms.csv          # Raw dataset
├── src/                       # Main package
│       ├── components/        # ML Pipeline components
│       ├── config/            # Configuration management
│       ├── constants/         # Constant values
│       ├── entity/            # Data classes
│       ├── pipeline/          # Pipeline orchestration
│       ├── utils/             # Utility functions
│       └── unit_tests/        # Unit tests
├── static/                    # Static files for web application
├── templates/                 # HTML templates for web application
│   ├── index.html             # Main page
│   └── results.html           # Results page
├── app.py                     # Flask web application
├── main.py                    # Main entry point for training pipeline
├── Dockerfile                 # Docker configuration
├── requirements.txt           # Project dependencies
├── setup.py                   # Package installation configuration
├── params.yaml                # Hyperparameters
└── schema.yaml                # Data schema specification
```

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Jakee4488/Mushroom_Prediction_ML_project.git
    cd Mushroom_Prediction_ML_project
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Training the Model

To train the complete model pipeline:

```bash
python main.py
```

This will execute the following stages:
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Model Evaluation

### Web Application

To run the web application locally:

```bash
python app.py
```

Then navigate to `http://localhost:8080` in your web browser.

### Making Predictions

The web interface allows you to input mushroom characteristics and get a prediction on whether it's edible or poisonous.

## Model Training Pipeline

The project implements a modular ML pipeline with the following components:

1. **Data Ingestion**: Downloads and prepares the mushroom dataset
2. **Data Validation**: Validates the dataset schema and quality
3. **Data Transformation**: Preprocesses and transforms features
4. **Model Training**: Trains classification models
5. **Model Evaluation**: Evaluates model performance and selects the best model

## Web Application

The project includes a Flask web application with:
- User interface for entering mushroom characteristics
- Backend prediction service using the trained model
- Result visualization

## Docker Deployment

To build and run the application using Docker:

```bash
docker build -t mushroom-classifier .
docker run -p 8080:8080 mushroom-classifier
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the license included in the repository.


