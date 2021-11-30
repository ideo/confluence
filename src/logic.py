import streamlit as st
import matplotlib.pyplot as plt
import squarify

from .config import ACADEMIC_COLORS, COMMON_COLORS, CUSTOM_COLORS


def initialize_session_state():
    if "custom_spaces" not in st.session_state:
        st.session_state["custom_spaces"] = []
    if "space_sizes" not in st.session_state:
        st.session_state["space_sizes"] = {}


def treemap(spaces, sizes):
    spaces = [spc for spc in spaces if st.session_state[spc]]
    sizes = [sz for sz in sizes if sz]

    color_defs = ACADEMIC_COLORS | COMMON_COLORS
    colors = [color_defs[spc] if spc in color_defs else next(CUSTOM_COLORS) for spc in spaces]

    spaces = [spc.replace(" ", "\n") for spc in spaces]
    fig, ax = plt.subplots()
    plt.rc('font', size=8)
    squarify.plot(sizes=sizes, label=spaces, color=colors, alpha=0.7, pad=True)
    plt.axis('off')
    st.pyplot(fig)



# def treemap_dataframe(rooms):
#     df = pd.DataFrame(columns=["Room Type", "Size"])
#     for room_type in rooms:
#         for num_rooms in range(rooms[room_type]):
#             df = df.append({"Room Type": room_type, "Size": 1}, ignore_index=True)

#     return df


# def treemap_dictionary(rooms):
#     _id = 1
#     data = [{
#         "id":   _id,
#         "name": "DPI",
#     }]

#     for room_type in rooms:
#         _id += 1
#         parent_id = _id
#         data.append({
#             "id":   _id,
#             "name": room_type,
#         })

#         for _ in range(rooms[room_type]):
#             _id += 1
#             data.append({
#                 "id":       _id,
#                 "parent":   parent_id,
#                 "name":     f"{room_type}_{_id}",
#                 "size":     10,
#             })
#     return data
