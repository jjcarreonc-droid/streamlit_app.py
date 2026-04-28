import streamlit as st

st.title("Mi primera 1 ve hoy app 🚀")

st.write("Hola Jose, ya funciona!")

numero = st.slider("Elige un número", 0, 100)

st.write("Elegiste:", numero)
