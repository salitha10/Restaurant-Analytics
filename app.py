import streamlit as st
from multiapp import MultiApp
from apps import Apriori, Predict_Rating, Dashboard, Sentimental_Analysis # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Alalytics", Dashboard.app)
app.add_app("Market Basket Analysis", Apriori.app)
app.add_app("Predict Rating", Predict_Rating.app)
app.add_app("Sentimental Analysis", Sentimental_Analysis.app)

# The main app
app.run()