import streamlit as st
from streamlit_elements import elements, mui, html, nivo
import pandas as pd


# Prepare data
# incidence statistics
inc_data = pd.read_csv('data/statistics/brain_incident.csv') # Read the CSV data

incident_data = [] # Transform the data into the format required by nivo.Stream
for i, row in inc_data.iterrows():
    incident_data.append({
        "Year": str(int(row["Year of Diagnosis"])),
        "Female": row["Female"],
        "Male": row["Male"]
    })

# Define linechart function
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




# Call piechart function    
stream_chart()
