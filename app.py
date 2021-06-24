import streamlit as st
from multiapp import MultiApp
from apps import base_app,about,research# import your app modules here

app = MultiApp()


st.markdown("""
# What is Thuto?
Thuto, is a machine learning model that classifies customers sentiment based on thier social media data.
""")

# Add all your application here
app.add_app("More about the company", about.about_page)
app.add_app("Toyota project", base_app.main)
app.add_app("Our Research", research.research_page)

# The main app
app.run()

