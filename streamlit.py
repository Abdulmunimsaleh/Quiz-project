import streamlit as st
import pandas as pd
import joblib


st.title('Quiz Grade Predictor')

# Load the trained model from the file
model_path = 'extra_trees_model.pkl'  # Ensure this path is correct
loaded_model = joblib.load(model_path)

# User input for the grades
st.header('Enter Grades')
G1 = st.number_input('G1 Grade', min_value=0, max_value=100, value=50)
G2 = st.number_input('G2 Grade', min_value=0, max_value=100, value=50)

# Predict button
if st.button('Predict Final Grade'):
    # Create a DataFrame from the input
    trial_input = pd.DataFrame({'G1': [G1], 'G2': [G2]})
    
    # Make a prediction
    prediction = loaded_model.predict(trial_input)
    
    # Display the prediction
    st.write(f'Predicted Final Grade (G3): {prediction[0]:.2f}')

st.write("Upload the model file named 'extra_trees_model.pkl' to the same directory as this Streamlit app for it to function correctly.")
