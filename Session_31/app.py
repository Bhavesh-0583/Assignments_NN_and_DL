import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction App")

st.write("Enter house details to predict price")

# Inputs
square_footage = st.number_input("Square Footage")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
year_built = st.number_input("Year Built")
lot_size = st.number_input("Lot Size")
garage_size = st.number_input("Garage Size")
neighborhood_quality = st.number_input("Neighborhood Quality")

# Prediction button
if st.button("Predict Price"):
    
    features = np.array([[square_footage, bedrooms, bathrooms,
                          year_built, lot_size, garage_size,
                          neighborhood_quality]])
    
    prediction = model.predict(features)
    
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")