import streamlit as st


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


st.title("Lung Cancer")
st.markdown("""
    This page is under maintenance. Please check back later.
""")

st.image("data/gif/undermaintenance.gif", use_column_width=True)

st.page_link("Cancer_App.py", label="Homepage", help="Go to Homepage", icon="❤️‍🩹")