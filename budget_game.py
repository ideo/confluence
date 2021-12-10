import streamlit as st

import src.budget_logic as lg
from src.budget_config import (BIZNESS_SPACES, COMMON_SPACES, TECH_SPACES, 
    ACADEMIC_SPACES, AMENITIES)


st.set_page_config(
    page_title="Design Your DPI",
    # page_icon="src/img/pink-pomelo-3723496-3104020.png",
    layout="wide")


lg.initialize_session_state()


st.header("Design Your DPI")
msg = """
    Choose what to include in your ideal Discovery Partners Institute. But, 
    careful! We don't have unlimited budget.
"""
st.write(msg)
col1, col2, _, col3 = st.columns([2, 2, 1, 5])
lg.space_sliders(col1, "Shared Spaces", COMMON_SPACES)
lg.space_sliders(col2, "Tech Talent Development", TECH_SPACES)
lg.space_sliders(col2, "Applied R&D", ACADEMIC_SPACES)
lg.space_sliders(col2, "Entrepreneurial", BIZNESS_SPACES)
lg.amenity_checkboxes(col2, "Amenities")

col3.metric("You've spent", f"${st.session_state['spend']}")
ttl = col3.text_input("Name your piece!", value="My 2D Discovery Partners Institute")
name = col3.text_input("Sign your work!")
lg.treemap(col3, ttl, name)
lg.download(col3, name)