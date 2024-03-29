from random import choice

import streamlit as st
import matplotlib.pyplot as plt
import squarify

from .app_config import ACADEMIC_COLORS, COMMON_COLORS, CUSTOM_COLORS


def initialize_session_state():
    if "custom_spaces" not in st.session_state:
        st.session_state["custom_spaces"] = []

    if "notes" not in st.session_state:
        st.session_state["notes"] = {}
    
    if "space_sizes" not in st.session_state:
        st.session_state["space_sizes"] = {}
    
    if "color_defs" not in st.session_state:
        # color_defs = ACADEMIC_COLORS | COMMON_COLORS
        st.session_state["color_defs"] = {**ACADEMIC_COLORS, **COMMON_COLORS}


def add_custom_space():
    new_space = st.text_input("Define a New Space")
    new_space = new_space.title().replace("'S", "'s")

    if new_space not in st.session_state["custom_spaces"]:
        st.session_state["custom_spaces"].append(new_space)

    if "" in st.session_state["custom_spaces"]:
            st.session_state["custom_spaces"].remove("")

    options = st.session_state["custom_spaces"]
    custom = st.multiselect("Custom Spaces", options, default=options)
    return custom


def treemap(spaces, sizes, ttl, name):
    # spaces = [f"{spc}\n{st.session_state[f'{spc}_notes']}" for spc in spaces if st.session_state[spc]]
    spaces = [spc for spc in spaces if st.session_state[spc]]
    sizes = [sz for sz in sizes if sz]
    colors = [st.session_state["color_defs"][spc] for spc in spaces]

    spaces = [spc.replace(" ", "\n") for spc in spaces]
    fig, ax = plt.subplots()
    plt.rc('font', size=8)
    squarify.plot(sizes=sizes, label=spaces, color=colors, alpha=0.7, pad=True)
    plt.axis('off')
    
    title = f"{ttl.title()}\nby: {name}" if name else ttl.title()
    # title = f"2D Discovery Partners Institue\nMade by {name}" if name else "2D Discovery Partners Institue"
    plt.title(title)
    st.pyplot(fig)
    return title


def create_color_dictionary(spaces):
    for space in spaces:
        if space not in st.session_state["color_defs"]:
            st.session_state["color_defs"][space] = choice(CUSTOM_COLORS)


def download(title):
    filename = "2D_DPI.png"
    plt.savefig(filename, dpi=150)

    with open(filename, "rb") as file:
        btn = st.download_button(
             label="Download Layout",
             data=file,
             file_name=filename,
             mime="image/png"
           )