import streamlit as st
st.title('This is a title')

st.write('This is are **books** :books:')

st.button('Reset',type="primary")
if st.button ('say Hello'):
  st.write("why hello there")
else:
  st.write("goodbye")