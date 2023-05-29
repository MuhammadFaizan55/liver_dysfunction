import streamlit as st
import numpy as np
import pandas as pd
import joblib
import sklearn 
#title of page
st.set_page_config(page_title='ALT Detection Sys',page_icon='h1.jpeg',layout="centered")
st.markdown("""# **welcome to Liver dysfunction detection app**""")

# Load the models
render_model = joblib.load("render1.joblib")

def hide_streamlit_style():
   
   
    hide_footer_style = """
        <style>
        .reportview-container .main footer {
            visibility: hidden;
        }
        footer { display: none; }
        </style>
    """

    st.markdown(hide_footer_style, unsafe_allow_html=True)

Gender = st.selectbox("Gender of the patient	 (1 for Male, 0 for Female)", [1, 0])
age = st.text_input("Age of the patient (years.months)", "1.0")
Total_Bilirubin = st.number_input("Total Bilirubin", min_value=0.0, max_value=10.0, value=3.0, step=0.05)
Direct_Bilirubin = st.number_input("Direct Bilirubin ",min_value=0.0, max_value=40.0, value=0.9, step=.01)
Alkphos_Alkaline_Phosphotase = st.number_input("Alkphos Alkaline Phosphotase", min_value=0.0, max_value=2500.0, value=187.0, step=.1)
Sgpt_Alamine_Aminotransferase = st.number_input("Sgpt Alamine Aminotransferase",min_value=0.0, max_value=2000.0, value=64.0, step=1.0)
Sgot_Aspartate_Aminotransferase = st.number_input("Sgot Aspartate Aminotransferase ",min_value=0.0, max_value=5000.0, value=30.0, step=0.1)
Total_Protiens = st.number_input("Total Protiens ",min_value=0.0, max_value=30.0, value=10.0, step=0.01)
ALB_Albumi = st.number_input("ALB Albumi ",min_value=0.0, max_value=30.0, value=10.0, step=0.01)
AG_Ratio_Albumin_and_Globulin_Ratio = st.number_input("A/G Ratio Albumin and Globulin Ratio",min_value=0.0, max_value=20.0, value=10.0, step=0.01)

# Create a function to predict diseases
def predict_disease(Gender, age, Total_Bilirubin, Direct_Bilirubin, Alkphos_Alkaline_Phosphotase, Sgpt_Alamine_Aminotransferase, Sgot_Aspartate_Aminotransferase, Total_Protiens,
                     ALB_Albumi, AG_Ratio_Albumin_and_Globulin_Ratio):
    input_data = [[Gender, age, Total_Bilirubin, Direct_Bilirubin, Alkphos_Alkaline_Phosphotase, Sgpt_Alamine_Aminotransferase, Sgot_Aspartate_Aminotransferase, Total_Protiens,
                     ALB_Albumi, AG_Ratio_Albumin_and_Globulin_Ratio]]
    
    prediction = render_model.predict(input_data)[0]

    if prediction is not None:
        result = "Positive" if prediction == 0 else "Negative"
    else:
        result = "Invalid disease selection"
    
    return result

if st.button("Predict"):
                # Call the predict_diseases function with user input
                results = predict_disease(Gender, age, Total_Bilirubin, Direct_Bilirubin, Alkphos_Alkaline_Phosphotase, Sgpt_Alamine_Aminotransferase, Sgot_Aspartate_Aminotransferase, Total_Protiens,
                     ALB_Albumi, AG_Ratio_Albumin_and_Globulin_Ratio)

                # Display the predictions
                st.subheader("Prediction Results")
                st.write(results)
                reset_button_style = """
                    <style>
                    .stButton button {
                        background-color: #4CAF50; /* Green */
                        border: none;
                        color: white;
                        padding: 10px 24px;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin: 4px 2px;
                        cursor: pointer;
                    }
                    </style>
                    """
                st.markdown(reset_button_style, unsafe_allow_html=True)
    
if __name__ == '__main__':
    try:
        state = st.session_state       
        hide_streamlit_style()

    except Exception as e:
        print(f"An error occurred: {e}")