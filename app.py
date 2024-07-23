import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

#Streamlit
st.title('Prediksi Harga Rumah 🏚️')

# Input fitur 
bedrooms = st.number_input('Jumlah Kamar Tidur', min_value=1, max_value=10, value=1)
bathrooms = st.number_input('Jumlah Kamar Mandi', min_value=0, max_value=8, value=0)
floors = st.number_input('Jumlah Lantai ', min_value=1, max_value=6, value=1, step=1)  
yr_built = st.number_input('Tahun Dibangun', min_value=0, max_value=2100, value=0) 
sqft_living = st.number_input('Luas Bangunan (sqft)', min_value=0, value=0)


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

 


