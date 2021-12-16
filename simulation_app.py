
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

st.subheader("Design Your Space")
st.markdown("##### 1. Upload a saved graph")
msg = """
    If you have a previously saved graph, upload it here. Or, skip this step 
    and design a new layout.
"""
st.write(msg)
lg.upload()

st.markdown("##### 2. Choose which spaces to include")
label = "Click here to select how many of each room type to include."
with st.expander(label, expanded=False):
    col1, _, col2 = st.columns([5, 1, 5])
    lg.space_sliders(col1, "Shared Spaces", COMMON_SPACES)
    lg.space_sliders(col2, "Academic Spaces", ACADEMIC_SPACES)
    lg.space_sliders(col2, "Start-Up Spaces", BIZNESS_SPACES, spacer=True)
    lg.space_sliders(col2, "Student Spaces", TECH_SPACES, spacer=True)
lg.update_nodes()


st.markdown("#### 3. Add connections between rooms")
graph = lg.retrive_graph()
node1, node2 = lg.select_two_nodes(graph)
clicked = st.button("Connect!")
if clicked and node1 and node2:
    lg.connect(node1, node2, graph)


st.markdown("#### 4. Download your graph to reuse later")
lg.download()
st.markdown("---")


# print(st.session_state)
st.subheader("Network Diagram")
st.write("This network diagram represents the flow of access from room to room in DPI.")
lg.draw_graph()



# st.write("Where is the next component?")