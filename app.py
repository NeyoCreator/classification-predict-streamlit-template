import streamlit as st
from multiapp import MultiApp
from apps import base_app,about,research# import your app modules here

app = MultiApp()


st.markdown("""
# What is Thuto?
Thuto, Is a machine learning model that classifies customers sentiment based on thier social media data.
""")

# Add all your application here
app.add_app("More about us", about.about_page)
app.add_app("Research", research.research_page)
app.add_app("Our projects", base_app.main)
# The main app
app.run()