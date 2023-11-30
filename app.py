import streamlit as st
import pandas as pd
import pickle

model_file = "insurance.pkl"
with open(model_file, "rb") as file:
    model = pickle.load(file)

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

def predict_claim(age, gender, bmi, blood_pressure, diabetic, children, smoker, region):
    regions = ['Southeast', 'Northwest', 'Southwest', 'Northeast']
    region_num = regions.index(region)

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

    input_data = input_data[['age', 'gender', 'bmi', 'bloodpressure', 'diabetic', 'children', 'smoker', 'region']]

    prediction = model.predict(input_data)

    return prediction[0]

def main():
    st.title("Insurance Claim Prediction App")
    st.sidebar.markdown(
        """
        ### User Input
        Adjust the sliders and options on the left, then click the "Predict" button.
        """
    )

    age, gender, bmi, blood_pressure, diabetic, children, smoker, region = get_user_inputs()

    if st.sidebar.button("Predict", key='predict_button'):
        prediction = predict_claim(age, gender, bmi, blood_pressure, diabetic, children, smoker, region)

        st.subheader("Estimated Insurance Claim Amount:")
        st.write(f"**$ {prediction:,.2f}**", key='prediction_result', font=("Arial", 24, 'bold'), use_container_width=True)

    st.markdown(
        """
        ### Tips:
        - Adjust the sliders and options to customize your input.
        - Click the "Predict" button to see the estimated claim amount.
        - Explore different scenarios to understand the impact on the prediction.
        """
    )

if __name__ == "__main__":
    main()
