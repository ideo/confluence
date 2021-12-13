import streamlit as st

from src.budget_config import OPTIONS


def sidebar(budget_cap):
    st.sidebar.header("Top Secret Settings")

    new_budget_cap = st.sidebar.slider("Set Budget Cap", 
        value=budget_cap,
        min_value=0, 
        max_value=budget_cap*5,
        format="$%s")

    st.sidebar.markdown("---")

    for option in OPTIONS:
        price = st.sidebar.slider(
            f"{option} Price",
            value=OPTIONS[option]["price"],
            min_value=0,
            max_value=100,
            key=f"{option}_price",
            format="$%s"
        )

    return new_budget_cap

    
