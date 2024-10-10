import streamlit as st
from streamlit_elements import elements, mui, html, nivo
import pandas as pd


# Prepare data
# survival statistics
sur_data = pd.read_csv('data/statistics/brain_survival.csv') # Read the CSV data
survival_data = [
    {
        "id": "5-Year Relative Survival",
        "data": [{"x": str(int(row["Year"])), "y": int(row["5-Year Relative Survival% — SEER 8"])} for _, row in sur_data.iterrows()]
    }
]


# Define linechart function
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
            )




# Call piechart function    
linechart(survival_data)
