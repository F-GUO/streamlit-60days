import streamlit as st

st.header('st.checkbox')

st.write('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
  st.write('Great!! Here is some more 🍦')
if coffee:
  st.write('OK, heres com coffee ☕')

if cola:
  st.write('Here you go')