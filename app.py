import streamlit.components.v1 as components

components.html(open("index.html", "r", encoding="utf-8").read(), height=600)
