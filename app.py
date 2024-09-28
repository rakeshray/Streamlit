import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.header("Cars24 Data :sunglasses:")
st.header("Bar Chart", divider="gray")
#st.header("These headers have rotating dividers", divider=True)
#st.header("One", divider=True)
#st.header("Two", divider=True)
#st.header("Three", divider=True)
#st.header("Four", divider=True)
df = pd.read_csv('cars24-car-price.csv')
st.dataframe(df.head(2))
st.bar_chart(data=df, x='fuel_type',y='mileage')

d = st.date_input("Enter the date", datetime.date(2023,1,2))

#st.text('Datatime is : ')
#st.show('Datatime is : ')
#from PIL import Image
#image = Image.open("sunrise.jpg")
#st.image(image)