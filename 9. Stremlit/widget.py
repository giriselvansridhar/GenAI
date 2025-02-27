import streamlit as st
import pandas as pd

st.title('Streamlit Text Input')

name = st.text_input("Enter your name")
age = st.slider("SELECT YOUR AGE: ", 0, 100, 25)
st.write(f"Your age: {age}")

options1 = ["Python", "C", "C++"]
language = st.selectbox("Choose a programming language:", options1)

if name: 
    st.write(f"Hello, {name}!")

upload_file = st.file_uploader("Upload a CSV file", type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)

    st.camera_input(label="Cam")
    




