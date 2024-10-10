import streamlit as st
from streamlit_elements import elements, mui, html, nivo
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
from lifelines import KaplanMeierFitter
import time
import networkx as nx
import requests
import py3Dmol




# Set page configuration

st.set_page_config(
    page_title="Brain",
    page_icon="🧠",
    layout="wide"
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

#data
# define read_tsv function
def read_tsv(file_path):
    data = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            values = line.strip().split('\t')
            if len(values) >= 2:  # Ensure there are at least two values
                entry = {
                    "id": values[0],
                    "label": values[0],
                    "value": float(values[1])
                }
                data.append(entry)
    return data


# call read_tsv function
type_data = read_tsv("data/statistics/brain_types.tsv")

# gender statistics
gender_data = [
    {"id": "Male", "data": [{"x": "Male", "y": 58.21}]},
    {"id": "Female", "data": [{"x": "Female", "y": 41.49}]},
    {"id": "Not reported", "data": [{"x": "Not reported", "y": 0.3}]}
]

# age statistics
age_data = [
    {"age group": "10.9 to <26.72", "% cases": 5.13},
    {"age group": "26.72 to <42.54", "% cases": 23.25},
    {"age group": "42.54 to <58.36", "% cases": 31.43},
    {"age group": "58.36 to <74.18", "% cases": 31.28},
    {"age group": "74.18 to <90", "% cases": 8.92}
]

# survival statistics
sur_data = pd.read_csv('data/statistics/brain_survival.csv') # Read the CSV data
survival_data = [
    {
        "id": "5-Year Relative Survival",
        "data": [{"x": str(int(row["Year"])), "y": int(row["5-Year Relative Survival% — SEER 8"])} for _, row in sur_data.iterrows()]
    }
]

# incidence statistics
inc_data = pd.read_csv('data/statistics/brain_incident.csv') # Read the CSV data

incident_data = [] # Transform the data into the format required by nivo.Stream
for i, row in inc_data.iterrows():
    incident_data.append({
        "Year": str(int(row["Year of Diagnosis"])),
        "Female": row["Female"],
        "Male": row["Male"]
    })

# define piechart
def piechart(data):
    with elements("nivo_charts"):
        with mui.Box(sx={"height": 400, "margin": "auto"}):
            # Nivo Pie Chart
            nivo.Pie(
                data=data,
                margin={"top": 50, "right": 50, "bottom": 50, "left": 50},
                innerRadius=0.6,
                padAngle=1,
                cornerRadius=3,
                activeOuterRadiusOffset=8,
                colors={"scheme": "nivo"},
                borderWidth=1,
                borderColor={"from": "color", "modifiers": [["darker", 0.2]]},
                enableArcLinkLabels=True,
                startAngle=-300,
                defs=[
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "size": 4,
                            "padding": 1,
                            "stagger": True
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10
                        }
                    ],
                    legends=[
                        {
                            "anchor": "bottom",
                            "direction": "column",
                            "justify": False,
                            "translateX": -300,
                            "translateY": 40,
                            "itemsSpacing": 0,
                            "itemWidth": 100,
                            "itemHeight": 18,
                            "itemTextColor": "#999",
                            "itemDirection": "left-to-right",
                            "itemOpacity": 1,
                            "symbolSize": 12,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ]
                )

# Define radialbar chart
def radialbar(data):
    with elements("nivo_charts_radialbar"):
        with mui.Box(sx={"height": 400, "margin": "auto"}):
            # Nivo Radial Bar Chart
            nivo.RadialBar(
                data=data,
                margin={"top": 40, "right": 120, "bottom": 40, "left": 40},
                innerRadius=0.3,
                padAngle=0,
                cornerRadius=2,
                colors={"scheme": "nivo"},
                borderWidth=0,
                borderColor={"from": "color", "modifiers": [["darker", 1]]},
                enableRadialGrid=True,
                enableCircularGrid=True,
                animate=True,
                radialAxisStart={
                    "tickSize": 5,
                    "tickPadding": 5,
                    "tickRotation": 0
                },
                circularAxisOuter={
                    "tickSize": 5,
                    "tickPadding": 12,
                },
                legends=[
                    {
                        "anchor": "right",
                        "direction": "column",
                        "justify": False,
                        "translateX": 80,
                        "translateY": 0,
                        "itemsSpacing": 6,
                        "itemWidth": 100,
                        "itemHeight": 18,
                        "itemTextColor": "#999",
                        "symbolSize": 18,
                        "symbolShape": "square",
                        "effects": [
                            {
                                "on": "hover",
                                "style": {
                                    "itemTextColor": "#000"
                                }
                            }
                        ]
                    }
                ]
            )

# Define bar chart
def barchart(data):
    with elements("nivo_charts_bar"):
        with mui.Box(sx={"height": 400, "margin": "auto"}):
            # Nivo Bar Chart
            nivo.Bar(
                data=data,
                margin={"top": 50, "right": 130, "bottom": 50, "left": 60},
                padding=0.3,
                keys=["% cases"],
                indexBy=["age group"],
                groupMode='grouped',
                valueScale={"type": 'linear'},
                indexScale={"type": 'band', "round": True},
                colors={"scheme": 'nivo'},
                colorBy='indexValue',
                animate=True,
                motionConfig='wobbly',
                isFocusable=True,
                defs=[
                    {
                        "id": 'dots',
                        "type": 'patternDots',
                        "background": 'inherit',
                        "color": '#38bcb2',
                        "size": 4,
                        "padding": 1,
                        "stagger": True
                    },
                    {
                        "id": 'lines',
                        "type": 'patternLines',
                        "background": 'inherit',
                        "color": '#eed312',
                        "rotation": -45,
                        "lineWidth": 6,
                        "spacing": 10
                    }
                ],
                borderColor={
                    "from": 'color',
                    "modifiers": [["darker", 1.6]]
                },
                axisTop=None,
                axisRight=None,
                axisBottom={
                    "tickSize": 5,
                    "tickPadding": 5,
                    "tickRotation": 0,
                    "legend": 'age groups',
                    "legendPosition": 'middle',
                    "legendOffset": 32
                },
                axisLeft={
                    "tickSize": 5,
                    "tickPadding": 5,
                    "tickRotation": 0,
                    "legend": '% cases',
                    "legendPosition": 'middle',
                    "legendOffset": -40
                },
                labelSkipWidth=12,
                labelSkipHeight=12,
                labelTextColor={
                    "from": 'color',
                    "modifiers": [["darker", 1.6]]
                }
            )

# Define line chart
def linechart(data):
    with elements("nivo_charts_line"):
        with mui.Box(sx={"height": 400, "margin": "auto"}):
            # Nivo Line Chart
            nivo.Line(
                data=data,
                margin={"top": 50, "right": 110, "bottom": 50, "left": 60},
                xScale={"type": 'point'},
                yScale={
                    "type": 'linear',
                    "min": 'auto',
                    "max": 'auto',
                    "stacked": True,
                    "reverse": False
                },
                yFormat=" >-.2f",
                xFormat="=.0f",
                axisTop=None,
                axisRight=None,
                axisBottom={
                    "tickSize": 5,
                    "tickPadding": 5,
                    "tickRotation": 45,
                    "legend": 'Year',
                    "legendOffset": 36,
                    "legendPosition": 'middle',
                    "truncateTickAt": 0
                },
                axisLeft={
                    "tickSize": 5,
                    "tickPadding": 5,
                    "tickRotation": 0,
                    "legend": '5-Year Relative Survival (%)',
                    "legendOffset": -40,
                    "legendPosition": 'middle',
                    "truncateTickAt": 0
                },
                colors={'rgb(255, 105, 97)'},
                pointSize=10,
                pointColor={"theme": 'background'},
                pointBorderWidth=2,
                pointBorderColor={"from": 'serieColor'},
                pointLabel="yFormatted",
                pointLabelYOffset=-12,
                enableTouchCrosshair=True,
                useMesh=True
                # legends=[
                #     {
                #         "anchor": 'bottom-right',
                #         "direction": 'column',
                #         "justify": False,
                #         "translateX": 100,
                #         "translateY": 0,
                #         "itemsSpacing": 0,
                #         "itemDirection": 'left-to-right',
                #         "itemWidth": 80,
                #         "itemHeight": 20,
                #         "itemOpacity": 0.75,
                #         "symbolSize": 12,
                #         "symbolShape": 'circle',
                #         "symbolBorderColor": 'rgba(0, 0, 0, .5)',
                #         "effects": [
                #             {
                #                 "on": 'hover',
                #                 "style": {
                #                     "itemBackground": 'rgba(0, 0, 0, .03)',
                #                     "itemOpacity": 1
                #                 }
                #             }
                #         ]
                #     }
                #]
            )

# Define stream chart
def stream_chart(data):
    with elements("nivo_charts_stream"):
        with mui.Box(sx={"height": 400, "margin": "auto"}):
            # Nivo Stream Chart
            nivo.Stream(
                data=data,
                keys=["Female", "Male"],
                margin={"top": 50, "right": 110, "bottom": 50, "left": 60},
                axisTop=None,
                axisRight=None,
                axisBottom={
                    "orient": 'bottom',
                    "tickSize": 5,
                    "tickPadding": 5,
                    "tickRotation": 0,
                    "legend": 'Year of Diagnosis (2000-2021)',
                    "legendOffset": 36,
                    "legendPosition": 'middle'
                },
                axisLeft={
                    "orient": 'left',
                    "tickSize": 5,
                    "tickPadding": 5,
                    "tickRotation": 0,
                    "legend": 'Incidence Rate',
                    "legendOffset": -40
                },
                enableGridX=True,
                enableGridY=True,
                offsetType="none",
                order="ascending",
                colors={"scheme": 'nivo'},
                fillOpacity=0.85,
                borderColor={"theme": 'background'},
                curve="catmullRom",
                defs=[
                    {
                        "id": 'dots',
                        "type": 'patternDots',
                        "background": 'inherit',
                        "color": '#2c998f',
                        "size": 4,
                        "padding": 2,
                        "stagger": True
                    },
                    {
                        "id": 'squares',
                        "type": 'patternSquares',
                        "background": 'inherit',
                        "color": '#e4c912',
                        "size": 6,
                        "padding": 2,
                        "stagger": True
                    }
                ],
                dotSize=8,
                dotColor={"from": 'color'},
                dotBorderWidth=2,
                dotBorderColor={
                    "from": 'color',
                    "modifiers": [
                        ["darker", 0.7]
                    ]
                },
                motionConfig="wobbly",
                legends=[
                    {
                        "anchor": 'bottom-right',
                        "direction": 'column',
                        "translateX": 100,
                        "itemWidth": 80,
                        "itemHeight": 20,
                        "itemTextColor": '#999999',
                        "symbolSize": 12,
                        "symbolShape": 'circle',
                        "effects": [
                            {
                                "on": 'hover',
                                "style": {
                                    "itemTextColor": '#000000'
                                }
                            }
                        ]
                    }
                ]
            )



# Page Layout    
st.title("Brain Cancer")

tab1, tab2, tab3 = st.tabs(["General", "Statistics", "Biomarkers"])

with tab1: #General tab
    st.header("General Information about brain cancer")

    with st.container():

        col1, col2 = st.columns([0.7, 0.3])

        col1.image('data/images/brain_tumor_loc.jpg', 
                use_column_width=True, 
                caption='The locations of tumors in the brain.')

        col2.container(border=False, height=100)
        col2.subheader("What is brain cancer?")
        col2.write('Brain cancer occurs when abnormal cells in the brain grow in an uncontrolled way. Brain tumours can be benign or malignant.')
    
    st.container(height=50, border=False)

    with st.container():
        col1, col2 = st.columns([0.4, 0.6])
        with col1:
            st.container(border=False, height=50)
            st.markdown("""
                <div>
                    <h3>Types of brain cancer:</h3>
                    <p> Brain tumours are named after the cells in which the cancer first develops, such as neurons (nerve cells), glial cells and meninges. 
                        They can be classified in several ways.</p>
                    <p>There are two main types of brain cancer:</p>   
                </div>
                """, unsafe_allow_html=True)
            
            with st.expander("Gliomas"):
                st.markdown("""
                    <div>
                        <strong>Gliomas (the most common brain cancer type)</strong> - Arise from glial cells, which support and protect neurons. There are different subtypes of gliomas based on the specific cell type involved:
                        <ul>
                            <li><strong>Astrocytomas</strong> - These can be slow-growing (low-grade) or fast-growing (high-grade). High-grade astrocytomas, also known as glioblastomas, are the most aggressive type of brain tumor.</li>
                            <li><strong>Oligodendrogliomas</strong> - These are usually slow-growing tumors.</li>
                            <li><strong>Ependymomas</strong> - These can arise in the lining of the brain's ventricles (fluid-filled cavities) or spinal cord.</li>
                        </ul>
                    </div>           
                """, unsafe_allow_html=True)

            with st.expander("Non-gliomas"):
                st.markdown("""
                    <div>
                        <strong>Non-gliomas</strong> - refer to brain tumors that don't originate from glial cells. In contrast, non-gliomas arise from other cell types or tissues within the central nervous system (CNS) or its surrounding structures.
                        <ul>
                            <li><strong>Meningiomas</strong> - Develop from the meninges, the membranes that surround the brain and spinal cord. These are usually benign (noncancerous) but can sometimes be malignant.</li>
                            <li><strong>Primitive neuroectodermal tumors (PNETs)</strong> - These are aggressive tumors that can arise in the brain or spinal cord. They are more common in children.</li>
                            <li><strong>Schwannoma (Vestibular schwannoma)</strong> - These arise from the Schwann cells, which wrap around nerves and provide insulation. They are typically benign and often develop on the auditory nerve (acoustic neuroma), affecting hearing and balance.</li>
                            <li><strong>Pituitary tumors</strong> - These form in the pituitary gland, a small gland located at the base of the brain. Pituitary tumors can be benign or malignant and can affect hormone production.</li>
                        </ul>
                    </div>           
                """, unsafe_allow_html=True)

        with col2:
            st.image("data/images/brain_types.png",
                    use_column_width=True,
                    caption="Types of brain tumors."
                 )
        
    with st.container(border=True):
        st.markdown("""
        #### Classification of brain tumors based on where they start growing: 
        - **Primary brain tumours** - originate from the cells and structures within the brain.
        - **Secondary or metastatic brain tumours** - start in another part of the body and spread to the brain.

        #### Classification of brain tumors based on their developmental process:
        - **Benign brain tumours (called grade I or II)** - usually grow slowly and are unlikely to spread to other parts of the body. They may grow and affect how the brain works – this can be life-threatening.
        - **Malignant brain tumours (called grade III or IV)** - can grow quickly and may spread within the brain and spinal cord (but usually do not spread further). A malignant brain tumour may be called brain cancer.
        """)
    
    st.container(height=50, border=False)

    with st.container():
        st.subheader("Stages and grades of brain cancer")
        st.image("data/images/brain_grades.jpg", use_column_width=False, caption="Grades of brain cancer.")

        st.markdown("""
        Grading is a way of dividing tumour cells into groups. The more normal the cells look, the lower the grade. The more abnormal the cells look, the higher the grade.

        - **Grade 1 and 2 tumours** are low grades. 
        - **Grade 3 and 4 tumours** are high grade. The high grades are a form of cancer. 

        """)

        with st.container(border=True):
            col1, col2 = st.columns([0.3, 0.7], gap="medium")
            with col1:
                grade = st.slider("Select the grade of brain cancer", 1, 4, 1)

            with col2:
                placeholder = st.empty()
                if grade == 1:
                    placeholder.write("**Grade 1**: These are slow-growing tumors with the most normal-looking cells. They are considered low-grade and often benign (not cancerous).")
                if grade == 2:
                    placeholder.write("**Grade 2**: These tumors grow somewhat faster than grade 1 and have slightly more abnormal cell features. They are also considered low-grade but have a higher chance of recurring (coming back) after treatment.")
                if grade == 3:
                    placeholder.write("**Grade 3**: These are anaplastic tumors, meaning they show significant cellular abnormalities and have a faster growth rate. They are considered malignant (cancerous).")
                if grade == 4:
                    placeholder.write("**Grade 4**: These are the most aggressive and fastest-growing brain tumors, with highly abnormal cell features. Glioblastoma, the most common malignant brain tumor, falls under this grade.")

    st.container(height=50, border=False)

    with st.container():
        col1, col2 = st.columns([0.3, 0.7])
        with col1:
            st.container(border=False, height=200)
            st.subheader("Symptoms of brain cancer")
            st.markdown("""
                        The symptoms of brain cancer depend on where the tumour is in the brain, the size of the tumour and how quickly it is growing.
                    """)
        with col2:
            st.image("data/images/brain_symptoms.png", use_column_width=True, caption="Symptoms of brain cancer.")


    st.container(height=50, border=False)
    with st.container():
        col1, col2 = st.columns([0.65, 0.35])

        with col1:
            st.container(border=False, height=25)
            st.image("data/images/brain_treatment.png", use_column_width=True, caption="Treatment of brain cancer.")

        with col2:
            st.subheader("Treatment of brain cancer")
            st.markdown("""
                    Treatment and care of people with cancer is usually provided by a team of health professionals, both medical and allied health, called a multidisciplinary team (MDT).   
                        
                    Treatments may involve:
                    """)
            st.markdown("""
                    - **Surgery** - to remove the affected area of the brain.
                    - **Radiation therapy** - generally after surgery.
                    - **Chemotherapy** - possibly at the same time as radiation therapy and after completion of radiotherapy.
                    - **Targeted therapy** - such as bevacizumab, to slow the growth of the tumour.
                        """)

    # References
    st.container(height=50, border=False)
    st.divider()
    st.subheader("References")    
    st.markdown("""
                <div>
                <li> https://www.cancerresearchuk.org/about-cancer/brain-tumours </li>
                <li> https://brain-cancer.canceraustralia.gov.au/ </li>
                </div>
        """, unsafe_allow_html=True)





    st.container(height=100, border=False)
    # Button to go back to top of the page
    js = '''
    <script>
        var body = window.parent.document.querySelector(".main");
        console.log(body);
        body.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    </script>
    '''

    if st.button("Back to top"):
        temp = st.empty()
        with temp:
            st.components.v1.html(js)
            time.sleep(.5) # To make sure the script can execute before being deleted
        temp.empty()


with tab2: #statistics tab
    st.header("Statistics on brain cancer")

    tabType, tabGender, tabAge, tabSurvival, tabIncidence = st.tabs([
        "Types of brain tumor", 
        "Gender distribution", 
        "Age distribution", 
        "Survival rate", 
        "Incidence rate"
        ])

    with tabType:
        piechart(type_data)
        st.container(height=50, border=False)
        with st.expander("Show code", expanded=False):
            with open("data/code/piechart.py") as f:
                code = f.read()
                st.code(code, language="python")
    
    with tabGender:
        radialbar(gender_data)
        with st.expander("Show code", expanded=False):
            with open("data/code/radialchart.py") as f:
                code = f.read()
                st.code(code, language="python")

    with tabAge:
        barchart(age_data)
        with st.expander("Show code", expanded=False):
            with open("data/code/barchart.py") as f:
                code = f.read()
                st.code(code, language="python")

    with tabSurvival:
        linechart(survival_data)
        with st.expander("Show code", expanded=False):
            with open("data/code/linechart.py") as f:
                code = f.read()
                st.code(code, language="python")

    with tabIncidence:
        stream_chart(incident_data)
        with st.expander("Show code", expanded=False):
            with open("data/code/streamchart.py") as f:
                code = f.read()
                st.code(code, language="python")

 

with tab3:
    st.header("Biomarkers for brain cancer")

    st.markdown("""
        <div>
            <h3>What are biomarkers?</h3>
            <p>Biomarkers are molecules that can be measured in the body to indicate the presence of a disease or condition. They can be found in the blood, urine, or other body fluids, and can be used to diagnose, monitor, and treat diseases.</p>
            <p>Biomarkers can be used to:</p>
            <ul>
                <li>Diagnose brain cancer</li>
                <li>Monitor the progression of the disease</li>
                <li>Predict how well a patient will respond to treatment</li>
                <li>Identify new treatments for brain cancer</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.container(height=50, border=False)

    # Initial gene list related to brain cancer from TCGA
    st.subheader("Initial gene list related to brain cancer from TCGA")
    TCGA_brain_genes = pd.read_csv('data/statistics/resLFC_brain_df.csv', sep=',', index_col = False)
    cola, colb = st.columns([0.7, 0.3])
    with cola:
        st.write(TCGA_brain_genes)
    
    with colb:
        with st.container(border=True, height=100):
            gene_count = len(TCGA_brain_genes)
            st.write("Gene count:", gene_count)


    #String to display the biomarkers
    
    graph_colormap = plt.get_cmap('plasma')
    brain_string_db_top30 = pd.read_csv('data/statistics/hub_genes_brain.csv', sep=',', index_col = False)
    

    st.subheader("Top genes related to brain cancer ")

    protein_list = brain_string_db_top30.node_name.tolist()
    proteins = '%0d'.join(protein_list)
    url = 'https://string-db.org/api/tsv/network?identifiers=' + proteins + '&species=9606'
    r = requests.get(url)
    lines = r.text.split('\n') # pull the text from the response object and split based on new lines
    data = [l.split('\t') for l in lines] # split each line into its components based on tabs
    # convert to dataframe using the first row as the column names; drop empty, final row
    df = pd.DataFrame(data[1:-1], columns = data[0]) 


    # Display the first 30 rows of the STRING dataframe
    cola, colb = st.columns([0.7, 0.3])
    with cola:
        st.write(df)
    
    with colb:
        with st.container(border=True, height=100):
            gene_count_DEG = len(df)
            st.write("Gene count:", gene_count_DEG)
    

    # DataFrame with the preferred names of the two proteins and the score of the interaction
    interactions = df[['preferredName_A', 'preferredName_B', 'score']]
    # Create the graph
    G = nx.Graph(name='Protein Interaction Graph')
    interactions = np.array(interactions)
    # Add weighted edges to the graph
    for i in range(len(interactions)):
        interaction = interactions[i]
        a = interaction[0]  # Protein a node
        b = interaction[1]  # Protein b node
        w = float(interaction[2])  # Score as weighted edge where high scores = low weight
        G.add_weighted_edges_from([(a, b, w)])  # Add weighted edge to graph
    # Function to rescale values
    def rescale(l, newmin, newmax):
        arr = list(l)
        min_arr = min(arr)
        max_arr = max(arr)
        if max_arr == min_arr:
            return [(newmin + newmax) / 2] * len(arr)
        return [(x - min_arr) / (max_arr - min_arr) * (newmax - newmin) + newmin for x in arr]
    # Node color varies with degree
    c = rescale([G.degree(v) for v in G], 0.0, 0.9)
    c = [graph_colormap(i) for i in c]
    # Node size varies with betweenness centrality - map to range [1500, 7000]
    bc = nx.betweenness_centrality(G)
    s = rescale([v for v in bc.values()], 1500, 7000)
    # Edge width shows 1-weight - strength of interaction
    ew = rescale([float(G[u][v]['weight']) for u, v in G.edges], 0.1, 4)
    # Edge color also shows weight
    ec = rescale([float(G[u][v]['weight']) for u, v in G.edges], 0.1, 1)
    ec = [graph_colormap(i) for i in ec]
    # Define the layout for the graph
    pos = nx.spring_layout(G)


    st.subheader("STRING network map for top 30 genes related to brain cancer")
    
    cola, colb = st.columns([0.7, 0.3])
    with cola:
        svg_file = "data/statistics/combined_network.svg"
        st.image(svg_file)
    with colb:
        with st.container(border=True, height=100):
            gene_count_string = 5*6
            st.write("Gene count:", gene_count_string)
    


    with st.expander("Show code", expanded=False):
        with open("data/code/network_code.py") as f:
            code = f.read()
            st.code(code, language="python")

    st.container(height=50, border=False)

    # Filter brain cancer biomarkers
    st.subheader("Filtered brain cancer biomarkers")

    col_data, col_code = st.columns([0.3, 0.7])
    with col_data:
        filtered_results_brain = pd.read_csv('data/statistics/filtered_results_brain.csv', sep=',', index_col = False)
        st.write(filtered_results_brain)

    with col_code:
        with st.expander("Show code", expanded=False):
            with open("data/code/filter_results_brain.py") as f:
                code = f.read()
                st.code(code, language="python")

    
    # Survival rate analysis with candidate gene
    st.container(height=50, border=False)
    st.subheader("Survival rate analysis with candidate gene")
    #Show genes have significant log rank test and Hazard Ratio >= 1.2
    filtered_results_brain= pd.read_csv('data/statistics/filtered_results_brain.csv', sep=',', index_col = False)
    filtered_results_brain = filtered_results_brain.sort_values('Hazard_Ratio',ascending = False)
    # Import data for survival analysis with candidate gene
    ## Merged gene expression
    merged_gene_expression_brain= pd.read_csv('data/statistics/merged_gene_expression_brain.csv', sep=',', index_col = False)
    ## brain metadata survival
    brain_metadata_survival = pd.read_csv('data/statistics/brain_metadata_survival.csv', sep=',', index_col = False)
    # brain code
    brain_code = pd.read_csv('data/statistics/brain_code.csv', sep=',', index_col = False)

    def plot_gene_analysis(data, gene, brain_code, survival_data):
        # Filter the data for the specific gene
        brain_gene = data[data['Gene name'] == gene]
        # Create a figure with two subplots
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        
        # Plot boxplot for gene expression
        brain_gene_boxplot = pd.merge(brain_gene, brain_code, how='inner', on='barcode')
        sns.boxplot(data=brain_gene_boxplot, x='shortLetterCode', y='Expression', ax=axes[0])
        axes[0].set_title(f'{gene} expression')
        axes[0].set_ylabel('Normalized gene expression')
        axes[0].set_xlabel('')
        
        # Calculate the median expression level for survival curve
        median_expression = np.median(brain_gene['Expression'])    
        # Create 'strata' column based on median expression
        brain_gene['strata'] = np.where(brain_gene['Expression'] <= median_expression, 'low', 'high')
        # Merge with survival data
        brain_gene_survival = pd.merge(brain_gene, survival_data, how='inner', on='barcode')
        # Drop rows with missing survival data
        brain_gene_survival = brain_gene_survival.dropna(subset=['overall_survival'])
        # Initialize the KaplanMeierFitter
        kmf = KaplanMeierFitter()
        strata = brain_gene_survival['strata'].unique()
        
        # Plot survival curve
        for stratum in strata:
            mask = brain_gene_survival['strata'] == stratum
            kmf.fit(durations=brain_gene_survival['overall_survival'][mask], 
                    event_observed=brain_gene_survival['deceased'][mask], 
                    label=stratum)
            kmf.plot_survival_function(ax=axes[1])  
        
        # Add survival plot details
        axes[1].set_title(f'Survival Curve for {gene}')
        axes[1].set_xlabel('Time (Days)')
        axes[1].set_ylabel('Survival Probability')
        axes[1].legend(title='Gene Expression')
        
        # Adjust layout
        plt.tight_layout()
        
        # Return the figure
        return fig

    gene_list = filtered_results_brain.Gene.tolist()
    gene = st.selectbox('Select a gene for survival rate analysis:', gene_list)
    fig = plot_gene_analysis(merged_gene_expression_brain, gene , brain_code, brain_metadata_survival)
    st.pyplot(fig)

    with st.expander("Show code", expanded=False):
        with open("data/code/st_for_survival_plot.py") as f:
            code = f.read()
            st.code(code, language="python")

    st.container(height=100, border=False)
    st.subheader("3D Protein Structures of Biomarker Genes")


    # 3D Protein Structures of Biomarker Genes
    def get_gene_name(csv_file):
        try:
            df = pd.read_csv(f'{csv_file}', sep=',')
            second_column = df.iloc[:, 0]
            unique_values = second_column.drop_duplicates()
            unique_list = unique_values.tolist()
            unique_list.insert(0,'None')
            return unique_list
        except:
            raise ValueError

    def get_uniprot_id(gene_name):
        url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene_name}&format=json"
        response = requests.get(url)
        with st.spinner("Looking for UniProt entry..."):
            time.sleep(3)
        data = response.json()

        if 'results' in data and data['results']:
            return data['results'][0]['primaryAccession']
        else:
            raise ValueError(f"No UniProt entry found for gene: {gene_name}")

    def submit_mapping_request(from_db, to_db, ids):
        url = "https://rest.uniprot.org/idmapping/run"
        params = {
            'from': from_db,
            'to': to_db,
            'ids': ids
        }
        response = requests.post(url, data=params)
        if response.status_code == 200:
            return response.json()["jobId"]
        else:
            raise Exception(f"Error {response.status_code}: Unable to submit mapping request.")

    def check_job_status(job_id):
        url = f"https://rest.uniprot.org/idmapping/status/{job_id}"
        while True:
            response = requests.get(url)
            if response.status_code == 200:
                job_status = response.json()
                if 'jobStatus' in job_status:
                    if job_status["jobStatus"] == "FINISHED":
                        return True
                    elif job_status["jobStatus"] == "RUNNING":
                        time.sleep(2)
                    else:
                        raise Exception("Job failed or unknown status.")
                elif 'results' in job_status:
                    return True
                else:
                    raise Exception(f"Unexpected response format: {job_status}")
            else:
                raise Exception(f"Error {response.status_code}: Unable to check job status.")

    def retrieve_mapping_results(job_id):
        url = f"https://rest.uniprot.org/idmapping/results/{job_id}"
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json()
            if 'results' in results:
                return results['results']
            else:
                return []
        else:
            raise Exception(f"Error {response.status_code}: Unable to retrieve results.")

    def convert_uniprot_to_pdb(uniprot_id):
        from_db = 'UniProtKB_AC-ID'
        to_db = 'PDB'
        job_id = submit_mapping_request(from_db, to_db, uniprot_id)
        if check_job_status(job_id):
            results = retrieve_mapping_results(job_id)
            if results:
                pdb_ids = [result['to'] for result in results]
                return pdb_ids
            else:
                return ValueError
            
    def get_entry_id(uniprot_id):
        try:
            response = requests.get(f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}?")
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            return data[0]['entryId']
        except requests.exceptions.RequestException:
            return ValueError("Invalid PDB ID or network issue")

    def fetch_AF_PDB(uniprot_id):
        try:    
            response = requests.get(f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}?")
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            url = data[0]['pdbUrl']
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                raise ValueError("Invalid URL or network issue")
        except requests.exceptions.RequestException:
            return ValueError("Invalid UniProt ID or network issue")

            
    def fetch_pdb(pdb_id):
        url = f'https://files.rcsb.org/download/{pdb_id}.pdb'
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise ValueError("Invalid PDB ID or network issue")

    def get_protein_name(Id):
        if len(Id) == 4:
            url = f'https://data.rcsb.org/rest/v1/core/entry/{Id}'
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                return data['struct']['title']
            else:
                raise ValueError("Invalid PDB ID or network issue")
        else:
            UniProtId = Id.replace('AF-', '').replace('-F1', '')
            url = f'https://alphafold.ebi.ac.uk/api/prediction/{UniProtId}?'
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                return data[0]['uniprotDescription']
            else:
                raise ValueError("Invalid PDB ID or network issue")

    def generate_3d_html(Id, Data):
        view = py3Dmol.view(width=1000, height=1000)
        view.addModel(Data, 'pdb')
        view.setStyle({'cartoon': {'color': 'spectrum'}})
        view.zoomTo()
        view.addLabel(get_protein_name(Id), {'fontColor':'black','backgroundColor':'white', 'font': 'calibri', 'fontSize': 18, 'useScreen': True, 'position':{'x': 10, 'y': 60, 'z': 0 }})
        view.addLabel(f'{Id}', {'fontColor':'black','backgroundColor':'white', 'font': 'calibri', 'fontSize': 36, 'useScreen': True, 'position':{'x': 10, 'y': 5, 'z': 0 }})
        view.spin(True)
        
        html_content = view._make_html()
        
        return html_content

    def main(csv_file):
        # st.title("Protein Structure Display")
        try:
            gene_list = get_gene_name(csv_file)
        except ValueError:
            st.warning('Errooooooooor')
        gene_name = st.selectbox("Select the protein coding gene:",gene_list)

        if gene_name == 'None':
            st.warning("Please select a protein coding gene.")
            return

        try:
            uniprot_id = get_uniprot_id(gene_name)
            with st.spinner("Don't rush, it's coming..."):
                time.sleep(3)
            st.text(f'UniProt ID for {gene_name}: {uniprot_id}.')
        except ValueError:
            st.text('UniProt ID not found.')
            return

        try:
            pdb_ids = convert_uniprot_to_pdb(uniprot_id)
            if isinstance(pdb_ids, list):
                try:
                    display_Id = st.selectbox('Please select the PDB ID: ', pdb_ids)
                    pdb_data = fetch_pdb(display_Id)
                    with st.spinner("Don't rush, it's coming..."):
                        time.sleep(3)
                    html_content = generate_3d_html(display_Id, pdb_data)
                    with st.spinner("Fetching your protein..."):
                        time.sleep(3)
                    components.html(html_content, height=1000, width= 1000)
                except ValueError:
                    st.text('PDB ID not found. Now searching in AlphaFold database...')
            else:
                try:
                    pdb_data = fetch_pdb(pdb_ids)
                    html_content = generate_3d_html(pdb_ids, pdb_data)
                    components.html(html_content, height=1000, width= 1000)
                except ValueError:
                    st.text('PDB ID not found. Now searching in AlphaFold database...')
        except ValueError:
            st.text('PDB ID not found. Now searching in AlphaFold database...')
            pass

        try:
            AF_data = fetch_AF_PDB(uniprot_id)
            AF_ID = get_entry_id(uniprot_id)
            with st.spinner("Don't rush, it's coming..."):
                time.sleep(3)            
            html_content = generate_3d_html(AF_ID, AF_data)
            st.text('AlphaFold predicted structure')
            components.html(html_content, height=800, width= 800)
        except:
            st.text('AlphaFold predicted structure not found.')

    if __name__ == "__main__":
        main('data/statistics/filtered_results_brain.csv')

    with st.expander("Show code", expanded=False):
        with open("data/code/protein.py") as f:
            code = f.read()
            st.code(code, language="python")






