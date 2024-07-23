import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

#Streamlit
st.title('Your House Price Prediction 🏚️')

# Input fitur 
bedrooms = st.number_input('Bedrooms', min_value=1, max_value=10, value=1)
bathrooms = st.number_input('Bathrooms', min_value=0, max_value=8, value=0)
floors = st.number_input('Floors', min_value=1, max_value=6, value=1, step=1)  
yr_built = st.number_input('Year Built', min_value=0, max_value=2100, value=0) 
sqft_living = st.number_input('Area of Building', min_value=0, value=0)


# Tombol Submit
if st.button('Submit'):
    # Buat dataframe input
    input_data = pd.DataFrame({
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'floors': [floors],  
        'yr_built': [yr_built],
        'sqft_living': [sqft_living] 
    })

    # Prediksi harga
    prediction = model.predict(input_data)

    # Tampilkan prediksi harga
    st.subheader('Prediksi Harga:')
    st.write(f"${prediction[0]:,.2f}")

 


