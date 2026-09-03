import streamlit as st
import pandas as pd

# Display Functions

st.title('Learning Streamlit')
st.header('Exploring Streamlit function')
st.subheader('Display functions')

st.code(print('Hello World'))
st.text('Exited to learn Streamlit')
st.write('a + b =',5)

st.markdown('**Bold**,*Italic*')


#User Input functions

st.number_input('Enter the number',min_value=0,max_value=100)

st.text_input('Enter the text')
st.text_area('Enter the text')

st.date_input('Enter the date')
st.time_input('Enter time')

#buttons

st.button('Predict')
    