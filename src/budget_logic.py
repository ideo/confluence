import streamlit as st
import matplotlib.pyplot as plt
import squarify

from .budget_config import (BIZNESS_SPACES, COMMON_SPACES, TECH_SPACES, 
    ACADEMIC_SPACES, AMENITIES, OPTIONS)


def initialize_session_state():
    if "spend" not in st.session_state:
        st.session_state["spend"] = 0


def update_budget():
    st.session_state["spend"] = sum(
        OPTIONS[space]["qty"]*OPTIONS[space]["price"] for space in OPTIONS
        )


def space_sliders(st_col, label, config):
    with st_col.expander(label, expanded=True):
        # st.markdown(f"**{label}**")
        options = sorted(config.keys())
        for option in options:
            quantity_slider(option, config)
        update_budget()

    
def quantity_slider(option, config):
    label = f"{option} – ${config[option]['price']} per room"
    qty = st.slider(label, 
        value=0,
        min_value=0,
        max_value=5,
        key=f"{option}_qty_slider")
    config[option]["qty"] = qty


def amenity_checkboxes(st_col, title):
    with st_col.expander(title, expanded=True):
        for offer in AMENITIES:
            label = f"{offer} – ${AMENITIES[offer]['price']}"
            checked = st.checkbox(label, key=f"{offer}_checkbox")
            AMENITIES[offer]["qty"] = 1 if checked else 0
        update_budget()


def treemap(st_col, ttl, name):
    spaces, sizes = [], []
    categories = [BIZNESS_SPACES, COMMON_SPACES, TECH_SPACES, ACADEMIC_SPACES]
    for category in categories:
        for room_type in category:
            qty = category[room_type]["qty"]
            if qty:
                spaces += [room_type]*qty
                sizes += [category[room_type]["size"]]*qty
    
    # colors = [st.session_state["color_defs"][spc] for spc in spaces]
    # spaces = [spc.replace(" ", "\n") for spc in spaces]

    fig, ax = plt.subplots()
    plt.rc('font', size=8)
    # squarify.plot(sizes=sizes, label=spaces, color=colors, alpha=0.7, pad=True)
    squarify.plot(sizes=sizes, label=spaces, alpha=0.7, pad=True)
    plt.axis('off')
    
    title = f"{ttl.title()}\nby: {name}" if name else ttl.title()
    # title = f"2D Discovery Partners Institue\nMade by {name}" if name else "2D Discovery Partners Institue"
    plt.title(title)
    st_col.pyplot(fig)
    # return title


def download(st_col, name):
    name = name.lower().replace("", "_")
    filename = f"2D_DPI_{name}.png"
    plt.savefig(filename, dpi=150)

    with open(filename, "rb") as file:
        btn = st_col.download_button(
             label="Download Layout",
             data=file,
             file_name=filename,
             mime="image/png"
           )