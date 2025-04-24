#print('hello')
import streamlit as st
import pandas as pd
import plotly.express as px

df_cars= pd.read_csv('vehicles_us.csv')

agree = st.checkbox("Check if interested in cars less than 20000 miles")

if agree:
    df_cars = df_cars[df_cars['odometer'] <= 20000]
    

st.plotly_chart(px.histogram(df_cars, x='price', nbins=50, title='Car Prices'))



st.header('Car Analysis')

st.write('')

