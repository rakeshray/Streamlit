import numpy as np
import pandas as pd
import datetime
import streamlit as st 
import pickle

df = pd.read_csv('cars24-car-price.csv')
#st.write(df)

st.write(
		"""
			# Used Cars Price Prediction
		"""
	)
st.dataframe(df.head(), use_container_width=True)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
	fuel_type = st.selectbox("Select the fuel type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])

with col2:
	engine = st.slider("Engine Power", 500, 5000, step=100)
with col3:
	transmission_type = st.selectbox('Select Gear', ["Manual", "Automatic"])
with col4:
	seats = st.selectbox("Enter no of seats", [2,3,4,5,6,7,8])

encode_dict = {
	"fuel_type" : {"Diesel" : 1, "Petrol":2, "CNG":3, "LPG":4, "Electric":5},
	"transmission_type" : {"Manual":1, "Automatic":2},
	"seller_type" : {"Dealer":1, "Individual":2,"Trustmark Dealer":3}
}

def model_pred(fuel_type, engine, transmission_type, seats):
	with open("car_pred", 'rb') as file:
		reg_model = pickle.load(file)
		input_features = [[2018, 1, 4000, fuel_type, transmission_type,19.70, engine, 86.30, seats]]

		return reg_model.predict(input_features)

if st.button("Predict Car Price"):
	# Encode the user inputs to use in model for prediction
	fuel_type = encode_dict["fuel_type"][fuel_type]
	transmission_type = encode_dict["transmission_type"][transmission_type]

	#seller_type = encode_dict["seller_type"][fuel_type]
	price = model_pred(fuel_type, engine, transmission_type, seats)
	st.text(f" # Predicted price of car is : {price} ")
