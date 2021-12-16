import json
from io import StringIO 
from copy import copy

# from numpy import e
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
    graph = retrive_graph()
    for option in options:
        st_col.slider(option, 
            value=sum(option in node_name for node_name in graph.nodes),
            min_value=0,
            max_value=5,
            key=f"{option}")


def update_nodes():
    graph = retrive_graph()
    for space in SPACES:
        qty = st.session_state[space]
        for ii in range(1, qty+1):
            room_name = f"{space} {ii}"# if qty > 1 else space
            if room_name not in graph.nodes:
                graph.add_node(room_name, color=SPACES[space]["color"])

        for jj in range(qty+1, 6):
            room_name = f"{space} {jj}"
            if room_name in graph.nodes:
                graph.remove_node(room_name)
    save_graph(graph)


def select_two_nodes(graph):
    col1, col2 = st.columns(2)

    label1 = "Add a connection between this room"
    options = list(copy(graph.nodes)) if len(graph.nodes) > 1 else []
    options = sorted(options)
    node1 = col1.selectbox(label1, options)

    label2 = "And this room"
    node2 = col2.selectbox(label2, options)
    return node1, node2


def connect(node1, node2, graph):
    # graph = retrive_graph()
    #  
    if node1 != node2 and (node1, node2) not in graph.edges:
        graph.add_edge(node1, node2)
    save_graph(graph)


def draw_graph():
    # width = st.slider("Width", value=500, min_value=100, max_value=2000)
    # height = st.slider("Height", value=500, min_value=100, max_value=2000)
    ntwk = Network(width=f"100%")   # do not specify height here
    
    graph = retrive_graph()
    get_color = lambda x: SPACES[" ".join(x.split(" ")[:-1])]["color"]
    color=[get_color(node_name) for node_name in graph.nodes]
    ntwk.add_nodes(list(graph.nodes), color=color)
    ntwk.add_edges(graph.edges)

    filename = "simulation_pyvis_graph.html"
    ntwk.show(filename)
    HtmlFile = open(filename, "r", encoding="utf-8")
    source_code = HtmlFile.read()
    components.html(source_code, height=600)


def upload():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        string_data = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
        graph_dict = json.loads(string_data)
        graph = nx.from_dict_of_dicts(graph_dict)
        save_graph(graph)


def download():
    file_name = st.text_input("Name your graph")
    file_name = file_name.lower().replace(" ", "_")
    file_name += ".json"

    graph = retrive_graph()
    graph_dict = nx.to_dict_of_dicts(graph)

    
    with open(file_name, "w") as file:
        json.dump(graph_dict, file)

    with open(file_name, "rb") as file:
        st.download_button(
            label="Download Graph",
            data=file,
            file_name=file_name,
            mime="application/json"
        )