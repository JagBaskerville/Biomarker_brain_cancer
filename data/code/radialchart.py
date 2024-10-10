import streamlit as st
from streamlit_elements import elements, mui, html, nivo


# Prepare data
# gender statistics
gender_data = [
    {"id": "Male", "data": [{"x": "Male", "y": 58.21}]},
    {"id": "Female", "data": [{"x": "Female", "y": 41.49}]},
    {"id": "Not reported", "data": [{"x": "Not reported", "y": 0.3}]}
]


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
            


# Call piechart function    
radialbar(gender_data)
