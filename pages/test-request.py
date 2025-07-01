"""
El objetivo de esta pagina es mostrar una forma de scrapear mediante
la librería requests.
Tambien se usa un parser llamado beautifulSoup
"""

import streamlit as st
import requests
from bs4 import BeautifulSoup

datos = requests.get("https://quotes.toscrape.com/").text

soup = BeautifulSoup(datos, 'html.parser')

span_elements = soup.find_all('span')

span_text = []
for span in span_elements:
    span_text.append(span.text.strip())



st.title("prueba con requests y beautifulSoup")
st.text(f"Hay una cantidad de {len(span_elements)} elementos span en el sitio")
st.text(span_elements)

st.header("Intento de mostrar solo el texto")
st.text(span_text)


