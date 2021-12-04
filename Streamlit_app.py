#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from PIL import Image
import pandas as pd
import glob
import os
from multiapp import MultiApp
root_path = "C:\\Users\mruna\Downloads\img_highres\input_Images"
add_selectbox = st.sidebar.radio(
    "Select the type of SEARCH METHOD",
    ("SIMILARITY SEARCH Method", "FAISS Method", "Upload image")
)
  
 
def load_image(image_file):
    img = Image.open(image_file)
    return img


def asearch():
    st.title("Images using Artistic Style Similarity Search Method")
    st.write("-------------------------------------------------------------------------------------------------")
    
    def get_data():
        return pd.read_csv(r'C:\Users\mruna\Downloads\img_highres\Artistic.csv')
       
    n = 1
    df = get_data()
    images = df['0'].unique()
    st.subheader("Choose an image from the dropdown : ")
    pic = st.selectbox('Choices : ', images)
    st.image(os.path.join(root_path,pic), width=None)
    
    st.subheader('How Many Images do you want to see?')
    z = st.slider('How many images do you want to see?', 1, 10, 1)
    st.subheader("Similar Products you may want to buy")
    for index, row in df.iterrows():
        if row['0'] == pic:     
            while n < z + 1:
                st.image(os.path.join(root_path,row[n]), width=100, caption=row[str(n)])
                n += 1

def fbfa():
    st.title("Images using Facebook FAISS")
    st.write("-------------------------------------------------------------------------------------------------")

    def get_data():
        return pd.read_csv(r'C:\Users\mruna\Downloads\img_highres\Faiss.csv')

    n = 1
    df = get_data()
    images = df['0'].unique()
    st.subheader("Choose an image from the below menu: ")
    pic = st.selectbox('Choices : ', images)
    st.image(os.path.join(root_path,pic), width=None)
    z = st.slider('Similar images to be shown?', 1, 10, 1)
    st.subheader("Similar Products")
    for index, row in df.iterrows():
        if row['0'] == pic:
            while n < z + 1:
                st.image(os.path.join(root_path,row[str(n)]), width=100, caption=row[str(n)])
                n += 1


def uploadImage():
    st.title("Upload Image")
    st.write("-------------------------------------------------------------------------------------------------")
    def get_data():
        return pd.read_csv('./merged.csv')
    n = 1
    df = get_data()
    images = df['0'].unique()
    st.subheader("Upload an image below: ")
    try:
        pic = st.file_uploader("Upload file", ["png", "jpg"])
        st.image(pic, width=None)
        z = st.slider('Similar images to be shown?', 1, 10, 1)
        st.subheader("Similar Products")
        for index, row in df.iterrows():
            if os.path.basename(str(row['0'])) == str(pic.name):         
                while n < z + 1:
                    st.image(row[str(n)], width=100, caption=row[str(n)])
                    n += 1
    except:
        print("Empty File!")
    
               
if add_selectbox == 'SIMILARITY SEARCH Method' :
    asearch()   
elif add_selectbox == 'FAISS Method':
    fbfa()   
elif add_selectbox == 'Upload image':
    uploadImage()    

