import streamlit as st
from streamlit import components
import numpy as np
import pandas as pd
from streamlit_elements import elements, mui, html, nivo
import time


st.set_page_config(
    page_title="Cancer",
    page_icon="❤️‍🩹",
    layout="wide"
)



# Navigation Sidebar
with st.sidebar:
    st.title("Cancer App")
    st.sidebar.page_link(r"pages/About_this_project.py", label="About this project", icon="📚")
    st.markdown("""<hr>""", unsafe_allow_html=True)
    st.sidebar.page_link("Cancer_App.py", label="Homepage", icon="❤️‍🩹")
    st.sidebar.page_link("pages/1_Brain_cancer.py", label="Brain Cancer", icon="🧠")
    st.sidebar.page_link("pages/2_Lung_cancer.py", label="Lung Cancer", icon="🫁")
    st.sidebar.page_link("pages/3_Breast_cancer.py", label="Breast Cancer", icon="🤦‍♀️")
    st.sidebar.page_link("pages/4_Liver_cancer.py", label="Liver Cancer", icon="🍺")
    st.markdown("""<hr>""", unsafe_allow_html=True)
    st.sidebar.page_link("pages/Reflection.py", label="Reflection", icon="🤔")
    st.markdown("""
             <div>
                <br><br><br>
                <strong style="font-size:12px;">Created by:<strong>
                <p style="font-size:12px;">VINCENT 林國禎 <br> 
                WAYNE 林佑恩 <br> 
                NGUYEN THI NGAN GIANG <br> 
                NGUYEN HOANG PHUONG UYEN <br>
                <br>
                <p style="font-size:12px;">June 2024</p>
                </p>
            </div>
        """, unsafe_allow_html=True)
    

#Layout
st.title("Cancer Data Visualization App")
st.markdown("""
    <div>
        <h3>This is a simple web application that visualizes cancer data.</h3>
        <h3>You can select a cancer type from the sidebar or click on the link below to view more information.</h3>
    </div>
    """, unsafe_allow_html=True)

with st.container():
    brain_gif_path = 'data/gif/brain.gif'
    st.image(brain_gif_path, use_column_width=True) 
    st.page_link( "pages/1_Brain_cancer.py", label="Go to Brain Cancer", help="Go to Brain Cancer page", use_container_width=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)

with st.container():
    lung_gif_path = 'data/gif/lung.gif'
    st.image(lung_gif_path, use_column_width=True)
    st.page_link("pages/2_Lung_cancer.py", label="Go to Lung Cancer", help="Go to Lung Cancer page", use_container_width=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)

with st.container():
    breast_gif_path = 'data/gif/breast.gif'
    st.image(breast_gif_path, use_column_width=True)
    st.page_link("pages/3_Breast_cancer.py", label="Go to Breast Cancer", help="Go to Breast Cancer page", use_container_width=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)

with st.container():
    liver_gif_path = 'data/gif/liver.gif'
    st.image(liver_gif_path, use_column_width=True)
    st.page_link("pages/4_Liver_cancer.py", label="Go to Liver Cancer", help="Go to Liver Cancer page", use_container_width=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)


with st.expander("Show code", expanded=False):
    with open("Cancer_App.py") as f:
        code = f.read()
        st.code(code, language="python")
