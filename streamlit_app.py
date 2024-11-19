import streamlit as st

st.header('st.button')

if st.button('Say hello', 100, 'print text'):
  st.write('Why hello there')
else:
  st.write('Goodbye')

