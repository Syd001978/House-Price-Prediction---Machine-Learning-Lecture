import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
from preprocess import preprocess_data,data1,data2

def train_and_save_model(data):
 

    X = data.drop('price', axis=1)  
    y = data['price']

    # Bagi data menjadi training dan testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inisialisasi model regresi linear
    model = LinearRegression()

    # Train model
    model.fit(X_train, y_train)

    # Simpan model ke file 'model.pkl'
    filename = 'model.pkl'
    pickle.dump(model, open(filename, 'wb'))

    print(f"Model telah disimpan ke '{filename}'")

    return model

# Panggil fungsi untuk melatih dan menyimpan model
if __name__ == "__main__":
    combined_data = preprocess_data(data1, data2)
    train_and_save_model(combined_data)