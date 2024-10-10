import streamlit as st
from streamlit_elements import elements, mui, html, nivo
import pandas as pd


# Prepare data
# age statistics
age_data = [
    {"age group": "10.9 to <26.72", "% cases": 5.13},
    {"age group": "26.72 to <42.54", "% cases": 23.25},
    {"age group": "42.54 to <58.36", "% cases": 31.43},
    {"age group": "58.36 to <74.18", "% cases": 31.28},
    {"age group": "74.18 to <90", "% cases": 8.92}
]

# Define linechart function
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




# Call piechart function    
barchart(age_data)
