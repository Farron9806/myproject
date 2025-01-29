# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:43:28 2025

@author: Be Kind
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Streamlit is amazing!")

st.title("Never use spaces in folders and file names!")

st.title("Hello World")

st.write("This is my first web app")

st.header("Sample data")

data = pd.DataFrame({"x": [1,2,3],
                     "y": [10,20,30]})

#Display the data un the Streamlit app
st.write(data)

#Creat a Plotly Figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)











