import streamlit as st

import src.logic as lg
from src.config import ACADEMIC_SPACES, COMMON_SPACES


st.set_page_config(
    page_title="Design Your DPI",
    page_icon="img/logo.jpeg")


lg.initialize_session_state()
st.header("Design Your Discover Partners Institute")


st.subheader("1. Choose which spaces to include")
msg = "Choose from predefined rooms, or create your own."
st.write(msg)
academic = st.multiselect("Academic Spaces", ACADEMIC_SPACES)
common = st.multiselect("Common Spaces", COMMON_SPACES)

new_space = st.text_input("Define a New Space")
new_space = new_space.title().replace("'S", "'s")
if new_space not in st.session_state["custom_spaces"]:
    st.session_state["custom_spaces"].append(new_space)
if "" in st.session_state["custom_spaces"]:
    st.session_state["custom_spaces"].remove("")
custom = st.multiselect("Custom Spaces", sorted(st.session_state["custom_spaces"]),
    default=sorted(st.session_state["custom_spaces"]))
spaces = academic + common + custom


if spaces:
    st.subheader("2. Size 'em up!")
    msg = "How big should each space be, relative to everything else?"
    st.write(msg)
    for space in spaces:
        # with st.expander(space, expanded=False):
        # label = f"How big is your {space}, relative to everything else?"
        size = st.slider(space, min_value=0, max_value=10, key=space, format="")
        # st.session_state["space_sizes"][space] = size
sizes = [st.session_state[spc] for spc in spaces]


if sum(sizes) > 0:
    st.subheader("3. Here's Your Two Dimensional DPI!")
    ttl = st.text_input("Name your piece!", value="My 2D Discovery Partners Institute")
    name = st.text_input("Sign your work!")
    title = lg.treemap(spaces, sizes, ttl, name)
    lg.download(title)
    msg = "Email your downloaded image to [jgambino@ideo.com](mailto:jgambino@ideo.com) and we will add it to our collection!"
    st.markdown(msg)