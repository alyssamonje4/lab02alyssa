import json
import pandas as pd
import streamlit as st
import altair as alt
from pathlib import Path

json_path = Path(__file__).parent.parent / "data.json"

with open(json_path, "r") as f:
    myData = json.load(f)

\
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
    layout="wide"
)
st.title("Data Visualizations 📈")

# PART 1: GRAPHS FROM data.json
sleepData = pd.DataFrame(myData["data_points"][0])
gramsData = pd.DataFrame(myData["data_points"][1])
incomeData = pd.DataFrame(myData["data_points"][2])
paintingData = pd.DataFrame(myData["data_points"][3])

st.title(myData["chart_title"])

st.subheader("Hours of Sleep by Day")
st.bar_chart(
    sleepData,
    x="Day of the Week",
    y="Hours of Sleep"
)

st.subheader("Protein by Meal")
st.line_chart(
    gramsData,
    x="Types of Meals",
    y="Grams of Protein"
)

st.subheader("Income by Person Type")
st.area_chart(
    incomeData,
    x="Person Type",
    y="Income"
)

st.title("Painting hours vs. starting income")

paintingChart = alt.Chart(paintingData).mark_line(point=True).encode(
    x="Number of Hours Painted",
    y="Starting Income after Graduation",
    tooltip=["Number of Hours Painted", "Starting Income after Graduation"],
)

st.altair_chart(paintingChart)
