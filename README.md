# Machine Learning-Based Insurance Claim Prediction App

This repository contains a Streamlit web application for predicting insurance claim amounts based on user input. The predictive model is trained using machine learning techniques.


## Business Problem
Develop a predictive model to estimate the numerical value of an insurance claim based on demographic and health-related features.

## Dataset
- The dataset includes features such as age, gender, smoking status, number of children, diabetic status, and any other relevant information.
- The target variable is a numerical value representing the amount of the insurance claim.

## Tasks
1. **Data Preprocessing:**
   - Handle missing values, if any.
   - Encode categorical variables.
   - Scale or normalize numerical features.

2. **Exploratory Data Analysis (EDA):**
   - Conduct exploratory data analysis to understand the distribution of features.
   - Identify correlations between features and the target variable.

3. **Feature Selection:**
   - Select relevant features that contribute to the prediction task.

4. **Model Selection:**
   - Choose appropriate regression algorithms (e.g., linear regression, decision tree regression, random forest regression, or gradient boosting).

5. **Model Training:**
   - Split the dataset into training and testing sets.
   - Train the selected regression model on the training set.

6. **Model Evaluation:**
   - Evaluate the model's performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE).

7. **Hyperparameter Tuning:**
   - Fine-tune the model's hyperparameters to optimize performance.

8. **Deployment:**
   - Deploy the trained regression model for predicting the insurance claim amount on new data.

## Business Impact
The model aims to provide the insurance company with accurate estimates of the potential claim amount. This information can assist in financial planning, resource allocation, and setting appropriate reserves.

Ensure to follow best practices in each step, and consider continuous monitoring and improvement of the model as needed. Keep in mind that regression models focus on predicting a numerical value rather than a binary outcome as in classification.





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
