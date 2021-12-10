import streamlit as st

from src.budget_config import OPTIONS


def sidebar():
    st.sidebar.header("Top Secret Settings")

    for option in OPTIONS:
        price = st.sidebar.slider(
            f"{option} Price",
            value=OPTIONS[option]["price"],
            min_value=0,
            max_value=100,
            key=f"{option}_price"
        )
