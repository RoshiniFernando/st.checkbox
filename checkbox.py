# Import streamlit
import streamlit as st

# Header text
st.header('st.checkbox')

st.write('Helloo!')
st.write ('What would you like to order?')

# Check boxes
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

# Display selected 
if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")