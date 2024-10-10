import streamlit as st
import streamlit.components.v1 as components
from streamlit_elements import elements, mui, html, nivo, editor
import pandas as pd



st.set_page_config(
    page_title="About",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
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

# Our Team
with elements("style_mui_sx_team"):
    mui.Typography("Our Team", variant="h2", sx={"marginBottom": 3})

col1, col2, col3, col4 = st.columns([1,1,1,1])

with col1:
    with st.popover("🐯 Quinn",use_container_width=True):
        st.write("""
            **Role**: General data collection, crawling and organization.
        """)
with col2:
    with st.popover("🐱 Jag",use_container_width=True):
        st.write("""
            **Role**: TCGA cancer data analysis, DEGs indentification, STRING database, hub genes analysis.
        """)
with col3:
    with st.popover("🐧 Wayne",use_container_width=True):
        st.write("""
            **Role**: Linking cancer hub genes data output to 3D protein structure visualization from protein databank (PDB) and AlphaFold database.
        """)
with col4:
    with st.popover("🦊 Vincent",use_container_width=True):
        st.write("""
            **Role**: Web app development, design and visualization.
        """)

st.container(height=100, border=False)



# Our purpose
with elements("style_mui_sx"):

    mui.Typography("Our Purpose", variant="h2", sx={"marginBottom": 3})

    with mui.Paper(sx={"padding": 3, "maxWidth": 800, "marginBottom":30}, elevation=5):
        mui.Typography("""
            Our purpose is to analyze the TCGA database and investigate gene expression patterns in various cancers. We aim to provide a simple Cancer Web Application that visualizes cancer data.
        """)


st.image("https://www.cancer.gov/ccg/sites/g/files/xnrzdm256/files/styles/cgov_article/public/cgov_infographic/2022-05/tcga-infographic-enlarge.png?itok=0JSjXHTY", 
         use_column_width=True)

st.container(height=100, border=False)

# Our workflow
with elements("workflow_1"):
    mui.Typography("Our Workflow", variant="h2", sx={"marginBottom": 3})
    mui.Typography("Database crawling, analysis, organization and filtering.", variant="h5", sx={ "marginBottom": 1, "textAlign": "center"})  
st.image("data/images/workflow.svg", use_column_width=True)
st.container(height=30, border=False)
with elements("workflow_2"):
    mui.Typography("Biomarker Identification and Visualization",variant="h5", sx={"marginBottom": 1, "textAlign": "center"})
    with mui.Paper(sx={"padding": 3, "marginBottom":3, "display": "flex", "justifyContent": "center"}, elevation=5):
        mui.Typography("Protein Databank (PDB) and AlphaFold database integration.", sx={"marginBottom": 1})
    mui.Typography("▼", sx={"fontSize": 30, "marginBottom": 3, "textAlign": "center"})
    with mui.Paper(sx={"padding": 3, "marginBottom":30, "display": "flex", "justifyContent": "center"}, elevation=5):
        mui.Typography("3D structure visualization", sx={"marginBottom": 1})
    

st.container(height=100, border=False)

# Databases
with elements("databases"):
    mui.Typography("Databases",variant="h2", sx={"marginBottom": 1})
with st.container(border=True):
    col1, col2= st.columns([1,1], gap="large")
    with col1:
        st.container(height=20, border=False)
        st.image("https://www.cancer.gov/ccg/sites/g/files/xnrzdm256/files/ncids_header/logos/Logo_CCG_0.svg", width=600)
        st.container(height=5, border=False)
        st.page_link("https://www.cancer.gov/ccg/research/genome-sequencing/tcga", label="NIH TCGA Cancer Database", help="Go to TCGA website")
        st.container(height=40, border=False)
        st.image("https://version11.string-db.org/images/string_logo_2015.png")
        st.container(height=15, border=False)
        st.page_link("https://string-db.org/", label="STRING Database", help="Go to STRING website")


    with col2:
        st.container(height=10, border=False)
        st.image("https://cdn.rcsb.org/rcsb-pdb/v2/common/images/rcsb_logo.png")
        st.page_link("https://www.rcsb.org/", label="Protein Data Bank", help="Go to PDB website")
        st.image("https://news.gbimonthly.com/upload/article/pharmalogo/alphafold30509.jpg")
        st.page_link("https://alphafold.ebi.ac.uk/", label="AlphaFold Database", help="Go to AlphaFold website")



st.container(height=100, border=False)

# Web application development
with elements("webapp"):
    mui.Typography("Web Application Development",variant="h2", sx={"marginBottom": 1})

with st.container(border=False):
    st.markdown("""
        This web application was developed using Streamlit, a Python library that allows you to create web applications with simple Python scripts.
        The application was developed using the data prepared by the team members listed above.
    """)
    col1, col2= st.columns([1,1])
    with col1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcgR1Zx9YwowMwku3WkkUV4FZYlx1bfDn2Dw&s", width=300)
        st.container(height=10, border=False)
        st.page_link("https://streamlit.io/", label="Streamlit.io", help="Go to Streamlit website")
    with col2:
        st.image("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png", width=300)
        st.page_link("https://www.python.org/", label="Python.org", help="Go to Python website")

st.container(height=50, border=False)
st.write("See the code we used to create this web application below.")    
with st.expander("Show code", expanded=False):
    with open("pages/demo.py") as f:
        code = f.read()
        st.code(code, language="python")