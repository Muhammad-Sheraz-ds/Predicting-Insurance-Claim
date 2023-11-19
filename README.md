# Machine Learning-Based Insurance Claim Prediction App

This repository contains a Streamlit web application for predicting insurance claim amounts based on user input. The predictive model is trained using machine learning techniques.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/MuhammadSheraza002/insurance-claim-prediction.git
    cd insurance-claim-prediction
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the App:**
    ```bash
    streamlit run app.py
    ```

4. **Open in Browser:**
   Visit [http://localhost:8501](http://localhost:8501) in your web browser.

## App Interface

The web application allows users to input various parameters such as age, gender, BMI, blood pressure, diabetic status, number of children, smoker status, and region. After providing the input, the user can click the "Predict" button to receive an estimated insurance claim amount.

## Files

- **app.py:** The main application file containing the Streamlit app.
- **insurance.pkl:** Pickle file containing the trained machine learning model.
- **requirements.txt:** File listing the Python dependencies for the project.

## Model Training

The predictive model is trained on an insurance dataset, and the trained model is saved using pickle. For details on the model training, refer to the original project code.

## Contributing

If you'd like to contribute or report issues, please open an issue or create a pull request.
