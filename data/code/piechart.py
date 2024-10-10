import streamlit as st
from streamlit_elements import elements, mui, html, nivo


# Prepare data
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
            

# Call piechart function    
piechart(type_data)
