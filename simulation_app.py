
import streamlit as st

import src.simulation_logic as lg
from src.simulation_config import (COMMON_SPACES, ACADEMIC_SPACES, 
    BIZNESS_SPACES, TECH_SPACES)


st.set_page_config(
    page_title="DPI Simulation",
    page_icon="img/logo.jpeg",
    # layout="wide",
    initial_sidebar_state="collapsed")


lg.initialize_session_state()
st.title("Build and Test a DPI Layout")


st.subheader("Choose which spaces to include")
label = "Select how many of each room type to include."
with st.expander(label, expanded=True):
    col1, _, col2 = st.columns([5, 1, 5])
    lg.space_sliders(col1, "Shared Spaces", COMMON_SPACES)
    lg.space_sliders(col2, "Academic Spaces", ACADEMIC_SPACES)
    lg.space_sliders(col2, "Start-Up Spaces", BIZNESS_SPACES, spacer=True)
    lg.space_sliders(col2, "Student Spaces", TECH_SPACES, spacer=True)
lg.update_nodes()


st.subheader("Add connections between rooms")
node1, node2 = lg.select_two_nodes()
clicked = st.button("Connect!")
if clicked and node1 and node2:
    lg.connect(node1, node2)


# print(st.session_state)
st.subheader("Network Diagram")
st.write("This network diagram represents the flow of access from room to room in DPI.")
lg.draw_graph()



st.write("Where is the next component?")