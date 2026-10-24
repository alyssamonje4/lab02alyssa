

import json
import streamlit as st
from pathlib import Path


st.set_page_config(
    page_title="Survey",
    page_icon="📝"
)

# PAGE TITLE
st.title("Nutrition Tracker 📝")
st.write("Please fill out the protein content of your last meal below")


json_path = Path(__file__).parent.parent / "data.json"


if "data" not in st.session_state:
    with open(json_path, "r") as f:
        st.session_state.data = json.load(f)


meals = st.session_state.data["data_points"][1]


with st.form("survey_form"):
    name = st.text_input("Meal name", key="meal_name")

    protein = st.slider(
        "Grams of protein",
        min_value=0,
        max_value=60,
        value=20,
        key="protein"
    )

    submitted = st.form_submit_button("Submit Data")

    if submitted:
        if name.strip():
            # Update both lists
            meals["Types of Meals"].append(name.strip())
            meals["Grams of Protein"].append(int(protein))

      
            with open(json_path, "w") as f:
                json.dump(st.session_state.data, f, indent=4)

            st.success("Your data has been saved to data.json!")
            st.write(f"Meal: {name.strip()}")
            st.write(f"Protein: {protein} g")
        else:
            st.error("Please enter a meal name before submitting.")
