import streamlit as st

import src.budget_logic as lg
from src.budget_sidebar import sidebar
from src.budget_config import (BIZNESS_SPACES, COMMON_SPACES, TECH_SPACES, 
    ACADEMIC_SPACES, CUSTOM_SPACES)


st.set_page_config(
    page_title="Design Your DPI",
    page_icon="img/logo.jpeg",
    layout="wide",
    initial_sidebar_state="collapsed")


lg.initialize_session_state()
budget_cap = lg.calculate_budget_cap()
budget_cap = sidebar(budget_cap)

st.header("Design Your DPI")
msg = """
    Choose what to include in your ideal Discovery Partners Institute.
"""
st.write(msg)
col1, col2, _, col3 = st.columns([2, 2, 1, 5])
lg.space_sliders(col1, "Shared Spaces", COMMON_SPACES)
lg.space_sliders(col2, "Tech Talent Development", TECH_SPACES)
lg.space_sliders(col2, "Applied R&D", ACADEMIC_SPACES)
lg.space_sliders(col2, "Entrepreneurial", BIZNESS_SPACES)
lg.amenity_checkboxes(col1, "Amenities")
lg.define_your_own(col2, "Custom Spaces", CUSTOM_SPACES)


col3.subheader(f"Be careful. You only have ${budget_cap} to spend!")
col3.metric("You've spent", f"${st.session_state['spend']}")
lg.total_spend(col3, budget_cap, st.session_state["spend"])
ttl = col3.text_input("Name your piece!", value="My 2D Discovery Partners Institute")
name = col3.text_input("Sign your work!")
lg.treemap(col3, ttl, name)
lg.download(col3, name)