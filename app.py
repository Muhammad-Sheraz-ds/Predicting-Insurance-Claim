import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model_file = "insurance.pkl"
with open(model_file, "rb") as file:
    model = pickle.load(file)

# Define the input ranges and options
age_range = (0, 100)
bmi_range = (10, 60)
bp_range = (60, 150)
children_range = (0, 10)

gender_options = ['Male', 'Female']
diabetic_options = ['No', 'Yes']
smoker_options = ['No', 'Yes']
region_options = ['Southeast', 'Northwest', 'Southwest', 'Northeast']


def get_user_inputs():
    st.sidebar.header("User Input")
    age = st.sidebar.slider("Age", min_value=age_range[0], max_value=age_range[1], value=30)
    gender = st.sidebar.selectbox("Gender", gender_options)
    bmi = st.sidebar.slider("BMI", min_value=bmi_range[0], max_value=bmi_range[1], value=25)
    blood_pressure = st.sidebar.slider("Blood Pressure", min_value=bp_range[0], max_value=bp_range[1], value=80)
    diabetic = st.sidebar.selectbox("Diabetic", diabetic_options)
    children = st.sidebar.slider("Number of Children", min_value=children_range[0], max_value=children_range[1], value=0)
    smoker = st.sidebar.selectbox("Smoker", smoker_options)
    region = st.sidebar.selectbox("Region", region_options)

    return age, gender, bmi, blood_pressure, diabetic, children, smoker, region

# Function to make a prediction
def predict_claim(age, gender, bmi, blood_pressure, diabetic, children, smoker, region):
    regions = ['Southeast', 'Northwest', 'Southwest', 'Northeast']
    region_num = regions.index(region)

    # Create a DataFrame for prediction
    input_data = pd.DataFrame({
        'age': [age],
        'gender': [gender.lower()],
        'bmi': [bmi],
        'bloodpressure': [blood_pressure],
        'diabetic': [diabetic],
        'children': [children],
        'smoker': [smoker],
        'region': [region.lower()],
    })

    # Ensure the columns match the ones used during training
    input_data = input_data[['age', 'gender', 'bmi', 'bloodpressure', 'diabetic', 'children', 'smoker', 'region']]

    # Make prediction
    prediction = model.predict(input_data)

    return prediction[0]

# Main function to run the app
def main():
    st.title("Insurance Claim Prediction App")
    st.sidebar.markdown(
        """
        This app predicts the estimated insurance claim amount based on user inputs.
        Adjust the sliders and options on the left, then click the "Predict" button.
        """
    )

    # Get user inputs
    age, gender, bmi, blood_pressure, diabetic, children, smoker, region = get_user_inputs()

    # Add a "Predict" button
    if st.sidebar.button("Predict", key='predict_button'):
        # Make prediction
        prediction = predict_claim(age, gender, bmi, blood_pressure, diabetic, children, smoker, region)

        # Display the prediction in a clear and bold format
        st.subheader("Estimated Insurance Claim Amount:")
        st.write(f"Rs. {prediction[0]:,.2f}", key='prediction_result', font=("Arial", 24, 'bold'))

    # Additional information and tips
    st.markdown(
        """
        ### Tips:
        - Adjust the sliders and options to customize your input.
        - Click the "Predict" button to see the estimated claim amount.
        - Explore different scenarios to understand the impact on the prediction.
        """
    )

# Run the app
if __name__ == "__main__":
    main()
