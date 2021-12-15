from numpy import e
import streamlit as st
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

from .simulation_config import SPACES


def initialize_session_state():
    if "graph" not in st.session_state:
        graph = nx.Graph()
        st.session_state["graph"] = nx.to_dict_of_dicts(graph)


def retrive_graph():
    graph = nx.from_dict_of_dicts(st.session_state["graph"])
    if "" in graph.nodes:
        graph.remove_node("")
    return graph


def save_graph(graph):
    st.session_state["graph"] = nx.to_dict_of_dicts(graph)


def space_sliders(st_col, label, config, spacer=False):
    if spacer:
        st_col.markdown("---")
    st_col.markdown(f"**{label}**")
    options = sorted(config.keys())
    for option in options:
        st_col.slider(option, 
            value=0,
            min_value=0,
            max_value=5,
            key=f"{option}")


def update_nodes():
    graph = retrive_graph()
    for space in SPACES:
        qty = st.session_state[space]
        for ii in range(1, qty+1):
            room_name = f"{space} {ii}"
            if room_name not in graph.nodes:
                graph.add_node(room_name)

        deselected_nodes = []
        if qty == 0:
            for node in graph.nodes:
                if space in node:
                    deselected_nodes.append(node)
        graph.remove_nodes_from(deselected_nodes)
    save_graph(graph)


def select_two_nodes():
    col1, col2 = st.columns(2)
    graph = retrive_graph()

    label1 = "Add a connection between this room"
    options1 = list(graph.nodes) if len(graph.nodes) > 1 else []
    node1 = col1.selectbox(label1, options1)

    label2 = "And this room"
    options2 = list(graph.nodes) if len(graph.nodes) > 1 else []
    if node1 in options2:
        options2.remove(node1)
    node2 = col2.selectbox(label2, options2)
    return node1, node2


def connect(node1, node2):
    graph = retrive_graph()
    if (node1, node2) not in graph.edges:
        graph.add_edge(node1, node2)
    save_graph(graph)


def draw_graph():
    # width = st.slider("Width", value=500, min_value=100, max_value=2000)
    # height = st.slider("Height", value=500, min_value=100, max_value=2000)
    ntwk = Network(width=f"100%")   # do not specify height here
    ntwk.from_nx(retrive_graph())

    filename = "simulation_pyvis_graph.html"
    ntwk.show(filename)
    HtmlFile = open(filename, "r", encoding="utf-8")
    source_code = HtmlFile.read()
    components.html(source_code, height=600)