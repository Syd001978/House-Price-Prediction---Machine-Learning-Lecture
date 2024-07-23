import pandas as pd
data1 = pd.read_csv("data1.csv")
data2 = pd.read_csv("data2.csv")

def preprocess_data(data1, data2):
  
    # Ubah nama fitur di data2 agar konsisten dengan data1
    data2 = data2.rename(columns={'Price': 'price', 'Bedrooms': 'bedrooms', 
                                  'Bathrooms': 'bathrooms', 'floors': 'floors',
                                  'Year_Built': 'yr_built', 'SqFt' : 'sqft_living'})  

    # Gabungkan dataset
    combined_data = pd.concat([data1, data2], ignore_index=True)

    # Pilih fitur yang relevan
    features = ['price', 'bedrooms', 'bathrooms', 'floors', 'yr_built','sqft_living']
    combined_data = combined_data[features]

    # Handle missing values 
    combined_data = combined_data.fillna(combined_data.median())

    return combined_data