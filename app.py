import streamlit as st

import src.app_logic as lg
from src.app_config import ACADEMIC_SPACES, COMMON_SPACES


st.set_page_config(
    page_title="Design Your DPI",
    page_icon="img/logo.jpeg",
    layout="wide")


lg.initialize_session_state()
st.header("Design Your Discover Partners Institute")
col1, col2, col3 = st.columns((4, 1, 5))


with col1:
    st.subheader("1. Choose which spaces to include")
    msg = "Choose from predefined rooms, or create your own."
    st.write(msg)
    academic = st.multiselect("Academic Spaces", ACADEMIC_SPACES)
    common = st.multiselect("Common Spaces", COMMON_SPACES)
    custom = lg.add_custom_space()
    spaces = academic + common + custom
    lg.create_color_dictionary(spaces)


    if spaces:
        st.subheader("2. Size 'em up!")
        msg = "How big should each space be, relative to everything else?"
        st.write(msg)
        for space in spaces:
            size = st.slider(space, value=4, min_value=0, max_value=10, key=space, format="")
            label = "Add a note about this room"
            btn = st.button(label, key=f"{space}_btn")
            if btn:
                note = st.text_area("Add a note about this room", key=f"{space}_note")
                if note:
                    st.session_state["notes"]["space"] = note
    sizes = [st.session_state[spc] for spc in spaces]


with col3:
    if sum(sizes) > 0:
        st.subheader("3. Here's Your Two Dimensional DPI!")
        ttl = st.text_input("Name your piece!", value="My 2D Discovery Partners Institute")
        name = st.text_input("Sign your work!")
        title = lg.treemap(spaces, sizes, ttl, name)
        lg.download(title)
        msg = "Email your downloaded image to [jgambino@ideo.com](mailto:jgambino@ideo.com) and we will add it to our collection!"
        st.markdown(msg)