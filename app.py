#print('hello')
import streamlit as st
import pandas as pd
import plotly.express as px

df_cars= pd.read_csv('vehicles_us.csv')

agree1 = st.checkbox("Check if interested in cars less than 20000 miles")

if agree1:
    df_cars = df_cars[df_cars['odometer'] <= 20000]
    

st.plotly_chart(px.scatter(df_cars, x='odometer', y='price', title='Car Prices vs Odometer'))

agree2 = st.checkbox("Check if year >= 2005")

if agree2:
    df_cars = df_cars[df_cars['model_year'] >= 2011]
    

st.plotly_chart(px.histogram(df_cars, x='model_year', nbins=50, title='Car Prices'))

st.header('Car Analysis')

st.write('')

