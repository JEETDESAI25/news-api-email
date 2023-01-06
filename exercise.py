import streamlit as st
import requests

api_key = "Yo4VEDl4KROCC9Zp6PplBC2S86xyclnuYFZNvEEG"

url = "https://api.nasa.gov/planetary/apod?api_key=Yo4VEDl4KROCC9Zp6PplBC2S86xyclnuYFZNvEEG"

request = requests.get(url)

content = request.json()



st.title(content["title"])

st.image(content["url"])

st.write(content["explanation"])
