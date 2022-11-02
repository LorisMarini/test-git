#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd

# Which guest you want to analyze
guest_name = st.text_input("lGuest name (lowercase)", "salma")

# Load the data
file = st.file_uploader("Please choose a file")

if file is not None:

    #To read file as bytes:
    data = pd.read_csv(file)
    print("Data frame built successfully")

else:
	print("Error, load the data!")

#Lowercase textual data
to_lowercase = ["Network","Post","Tags","Content Type","Post Type", "Profile","Sent by"]

for c in to_lowercase:
    data[c] = data[c].str.lower()
    
#drop na
data = data.fillna(value=0)

#infer data types
data = data.infer_objects()

#Remove all commas
data.replace(to_replace=",",value="", inplace=True)

for c in ["Video Views", "Potential Reach"]:
    
    data[c] = data[c].str.replace(",","")
    data[c]  =data[c].astype(float)

# select data you need
data = data[['Date', 'Post ID', 'Network', 'Post Type', 'Content Type', 'Profile',
               'Sent by', 'Link', 'Post', 'Impressions',
               'Organic Impressions', 'Paid Impressions', 'Reach', 'Organic Reach',
               'Paid Reach', 'Potential Reach','Engagement Rate (per Impression)',
               'Engagements', 'Reactions', 'Likes', 'Dislikes', 'Video Views', 
               'Organic Video Views', 'Paid Video Views','Partial Video Views', 
               'Organic Partial Video Views','Paid Partial Video Views', 'Full Video Views',
               'Organic Full Video Views', 'Paid Full Video Views']]


st.write("\nX-CHANNEL REPORT FOR", guest_name, ":\n")

# Find guest
g = data[data.Post.str.contains(guest_name).fillna(value=False)]

tot_views = 0

networks=data.Network.unique()

for n in networks:
    
    this_network = g[g["Network"]==n]
    
    views = this_network["Video Views"].sum()
    posts = this_network["Video Views"].count()
    
    tot_views +=views
    
    st.write("\n", n, "\n")
    st.write("posts = ", posts)
    st.write("views = ", views)
    
st.write("\nTOT X-Channel Views = ", tot_views)