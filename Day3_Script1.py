# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:05:45 2025

@author: kbmaf
"""


import streamlit as st
import pandas as pd


# Title of the app
st.title("**Personal Portfolio**")

# Collect basic information
name = "Kamohelo Mafejane"
field = "Data Analytics"
institution = "University of The Western Cape"

# Display basic profile information
st.header("Here is information of my university career.")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")


#Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")


# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")



#A section to find githubportfolio
st.header("Sites to connect with me.")
st.write("Site options: \n Github \n LinkedIn")
site_visit = st.text_input("Insert the site you wish to connect with me on.")
if site_visit == "Github":
    st.write("You are about to go to Github")
    st.link_button("Go to Github", "https://github.com/Keyno-savicc" )
elif site_visit == "LinkedIn":
    st.write("You are about to go to my LinkedIn profile")
    st.link_button("Go to LinkedIn", "https://www.linkedin.com/in/kamohelo-mafejane-b9a424296/" )
else:
    st.write(f"{site_visit} is no an available site at the moment.")

#A section to guess what my favourite codinglanguage is
st.header("Pick a language you think I ammost proffecient in.")
choice= st.selectbox("Pick a language",["Python", "HTML5", "C#", "PHP", "SQL"])

if choice == "SQL":
    st.write("Correct!")
else:
    st.write("The option you have selected is incorrect")
    
    
# Add a contact section
st.header("Contact Information")
email = "kbmafejane03@gmail.com"
st.write(f"You can reach {name} at {email}.")
