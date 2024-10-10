import streamlit as st
import streamlit.components.v1 as components
from streamlit_elements import elements, mui, html, nivo


st.set_page_config(
    page_title="About",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Navigation Sidebar
with st.sidebar:
    st.title("Cancer App")
    st.sidebar.page_link("pages/About_this_project.py", label="About this project", icon="📚")
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
    

# Main content on reflection of this project
st.header("Reflection - Limitations and improvements")
st.markdown("""
    <p style="font-size:16px;">This project is a collaborative effort to create an interactive web application for cancer research.
    Some aspects of the project were successful, while others presented challenges.
    The following are some limitations and potential improvements for this project:</p>
    <br>
    <h3>Limitations and improvements:</h3>
    <ul>
        <li><strong>Data availability:</strong> The project relied on publicly available data sources, which may have limitations in terms of completeness and accuracy.</li>
        <li><strong>Data processing:</strong> The project involved processing large datasets, which can be computationally intensive and time-consuming. We therefore focus only on brain cancer as a demo for this project.</li>
        <li><strong>Model complexity:</strong> The project used simple analysis models to predict cancer types, which may not capture the full complexity of cancer biology. Currently just for reference and proof-of-concept only.</li>
        <li><strong>Data visualization:</strong> The project used various data visualization techniques to present the data, but there may be other visualization methods that could provide additional insights.</li>
        <li><strong>Deployment:</strong> This project is not deployed on a server, so it can only be run locally. This limits the accessibility of the application.</li>
    </ul>
    <hr>
    <p style="font-size:12px;">05 June 2024</p>
""", unsafe_allow_html=True)