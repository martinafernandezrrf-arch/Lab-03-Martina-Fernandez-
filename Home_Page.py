import streamlit as st

# Title of App
st.title("Web Development Lab03 🏀")
st.header("CS 1301 - Intro To Computing 🔵")
st.image("Images/nba.png", width=800)
         
# Assignment Data 
# TODO: Fill out your team number, section, and team members


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description


st.subheader("Team 39 (Pro Ballers team), Web Development - Section E")
st.image("Images/title.png", use_container_width=True)
st.subheader("Team Members: Martina Fernandez, Jonah Thov")


st.markdown(
    """
Welcome to our Streamlit Web Development Lab03 app! Here you can explore hoops data, compare players,
and get AI powered insights all in one place.Have fun, and we are happy to have you here! 
"""
)


st.subheader("Overview of the Pages in this App: ")

st.markdown(
    """

1. Home Page 🏠: You're here! Overview of this project, team info, and navigation to all pages. 

2. NBA API Data Explorer 🔎: Pulls in real NBA data (teams, players, or stats) and lets you filter and explore interactively.

3. API Insights with Gemini 💻: Uses google gemini to generate summaries, comparisons, and explanations based on the basketball data. 

4. Basketbot🏀: A friendly basketball chatbot that remembers context and helps answer questions using the API data and AI. 
"""
)

