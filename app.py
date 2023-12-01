import streamlit as st
import pandas as pd
import pickle

model_file = "insurance.pkl"
with open(model_file, "rb") as file:
    model = pickle.load(file)

age_range = (0, 100)
bmi_range = (10, 60)
bp_range = (60, 150)

diabetic_options = ['No', 'Yes']
smoker_options = ['No', 'Yes']

def get_user_inputs():
    st.sidebar.header("User Input")
    age = st.sidebar.slider("Age", min_value=age_range[0], max_value=age_range[1], value=30)
    bmi = st.sidebar.slider("BMI", min_value=bmi_range[0], max_value=bmi_range[1], value=25)
    blood_pressure = st.sidebar.slider("Blood Pressure", min_value=bp_range[0], max_value=bp_range[1], value=80)
    diabetic = st.sidebar.selectbox("Diabetic", diabetic_options)
    smoker = st.sidebar.selectbox("Smoker", smoker_options)

    return age , bmi, blood_pressure, diabetic , smoker

def predict_claim(age, bmi, blood_pressure, diabetic,smoker):

    input_data = pd.DataFrame({
        'age': [age],
        'bmi': [bmi],
        'bloodpressure': [blood_pressure],
        'diabetic': [diabetic],
        'smoker': [smoker],
    })

    input_data = input_data[['age', 'bmi', 'bloodpressure', 'diabetic', 'smoker']]

    prediction = model.predict(input_data)

    return prediction[0]

def main():
    st.title("Insurance Claim Prediction App")
    

    age,bmi, blood_pressure, diabetic, smoker = get_user_inputs()

    if st.sidebar.button("Predict", key='predict_button'):
        prediction = predict_claim(age, bmi, blood_pressure, diabetic, smoker)

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
