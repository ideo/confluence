import streamlit as st
import matplotlib.pyplot as plt
import squarify
import pandas as pd

from .budget_config import CUSTOM_SPACES, AMENITIES, OPTIONS


def initialize_session_state():
    if "spend" not in st.session_state:
        st.session_state["spend"] = 0


def update_budget():
    st.session_state["spend"] = sum(
        # OPTIONS[space]["qty"]*OPTIONS[space]["price"] for space in OPTIONS
        OPTIONS[space]["qty"]*st.session_state[f"{space}_price"] for space in OPTIONS
        )


def space_sliders(st_col, label, config):
    with st_col.expander(label, expanded=True):
        # st.markdown(f"**{label}**")
        options = sorted(config.keys())
        for option in options:
            quantity_slider(option, config)
        update_budget()

    
def quantity_slider(option, config):
    price = st.session_state[f"{option}_price"]
    # label = f"{option} – ${config[option]['price']} per room"
    label = f"{option} – ${price} per room"
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


def define_your_own(st_col, title, config):
    with st_col.expander(title, expanded=True):
        new_space = st.text_input("Define a New Space")
        new_space = new_space.title().replace("'S", "'s")

        if new_space not in config and new_space != "":
            specs = {
                "price":    30,
                "qty":      0,
                "size":     2,
                "color":    "#A4A680",
            }
            config[new_space] = specs
            OPTIONS[new_space] = specs
            st.session_state[f"{new_space}_price"] = 30

        for option in config:
            quantity_slider(option, config)
        update_budget()


def calculate_budget_cap():
    limit = 2
    budget_cap = sum(OPTIONS[space]["price"]*limit for space in OPTIONS)
    budget_cap = int(round(budget_cap / 100.0)) * 100
    return budget_cap


def total_spend(st_col, budget_cap, total_spend):
    df = pd.DataFrame(columns=["Spend", "Legend", "Limit", "Order", "Budget"])
    df = df.append({
        "Spend": "", 
        "Legend": "Under Budget", 
        "Limit": budget_cap*0.8,
        "Budget": total_spend,
        "Order": 0}, ignore_index=True)
    df = df.append({
        "Spend": "", 
        "Legend": "Cutting it Close", 
        "Limit": budget_cap*0.2,
        "Budget": total_spend,
        "Order": 1}, ignore_index=True)
    
    if total_spend > budget_cap:
        df = df.append({
            "Spend": "", 
            "Legend": "Over Budget", 
            "Limit": total_spend-budget_cap, 
            "Budget": total_spend,
            "Order": 2}, ignore_index=True)

    print(df)

    color_codes = {
        "Under Budget": "#94C343CC",
        "Cutting it Close": "#E0A21DCC",
        "Over Budget": "#C01214CC",
    }
    labels = sorted(df["Legend"].value_counts().index.tolist())
    colors = [color_codes[l] for l in labels]

    spec1 = {
        "mark": "bar",
        "encoding": {
            "color": {
                "field": "Legend",
                "scale": {"range": colors}},
            "x": {"aggregate": "sum", "field": "Limit", "title": "Budget"},
            "y": {"field": "Spend"},
            "order": {"field": "Order", "type": "ordinal"}
        }
    }
    spec2 = {
        "mark": "rule",
        "encoding": {
            # "x": {"aggregate": "mean", "field": "Budget"},
            "x": {"datum": total_spend, "title": ""},
            "color": {"value": "black"},
            "size": {"value": 3}
            }
    }
    spec = {
        "layer": [spec1, spec2],
        # "title": f"Your Budget is ${budget_cap}"}
    }
    st_col.vega_lite_chart(df, spec, use_container_width=True)


def treemap(st_col, ttl, name):
    spaces, sizes, colors = [], [], []
    all_spaces = [room for room in OPTIONS if room not in AMENITIES]

    for room_type in all_spaces:
        qty = OPTIONS[room_type]["qty"]
        if qty:
            spaces += [room_type]*qty
            sizes += [OPTIONS[room_type]["size"]]*qty
            colors += [OPTIONS[room_type]["color"]]*qty
    
    spaces = [spc.replace(" ", "\n") for spc in spaces]

    fig, _ = plt.subplots()
    plt.rc('font', size=8)
    squarify.plot(sizes=sizes, label=spaces, color=colors, alpha=0.7, pad=True)
    # squarify.plot(sizes=sizes, label=spaces, alpha=0.7, pad=True)
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