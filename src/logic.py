import streamlit as st
import matplotlib.pyplot as plt
import squarify

from .config import ACADEMIC_COLORS, COMMON_COLORS, CUSTOM_COLORS


def initialize_session_state():
    if "custom_spaces" not in st.session_state:
        st.session_state["custom_spaces"] = []
    if "space_sizes" not in st.session_state:
        st.session_state["space_sizes"] = {}


def treemap(spaces, sizes, name):
    spaces = [spc for spc in spaces if st.session_state[spc]]
    sizes = [sz for sz in sizes if sz]

    color_defs = ACADEMIC_COLORS | COMMON_COLORS
    colors = [color_defs[spc] if spc in color_defs else next(CUSTOM_COLORS) for spc in spaces]

    spaces = [spc.replace(" ", "\n") for spc in spaces]
    fig, ax = plt.subplots()
    plt.rc('font', size=8)
    squarify.plot(sizes=sizes, label=spaces, color=colors, alpha=0.7, pad=True)
    plt.axis('off')

    ttl = f"2D Discovery Partners Institue\nMade by {name}" if name else "2D Discovery Partners Institue"
    plt.title(ttl)
    st.pyplot(fig)
    return fig


def download():
    filename = "dpi_2D_layout.png"
    plt.savefig(filename, dpi=150)

    with open(filename, "rb") as file:
        btn = st.download_button(
             label="Download Layout",
             data=file,
             file_name=filename,
             mime="image/png"
           )