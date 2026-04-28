import streamlit as st

st.title("Mi primera app 🚀")

st.write("Hola Jose, ya funciona!")

numero = st.slider("Elige un número", 0, 100)

st.write("Elegiste:", numero)
