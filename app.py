import streamlit as st

import src.logic as lg
from src.config import ACADEMIC_SPACES, COMMON_SPACES


st.set_page_config(
    page_title="Design Your DPI",
    page_icon="img/logo.jpeg")


lg.initialize_session_state()
st.header("Design Your Discover Partners Institute")


st.subheader("1. Choose which spaces to include")
msg = "Choose from predefined rooms, or create your own."
st.write(msg)
academic = st.multiselect("Academic Spaces", ACADEMIC_SPACES)
common = st.multiselect("Common Spaces", COMMON_SPACES)

new_space = st.text_input("Define a New Space")
new_space = new_space.title()
if new_space not in st.session_state["custom_spaces"]:
    st.session_state["custom_spaces"].append(new_space)
if "" in st.session_state["custom_spaces"]:
    st.session_state["custom_spaces"].remove("")
custom = st.multiselect("Custom Spaces", sorted(st.session_state["custom_spaces"]))
spaces = academic + common + custom


if spaces:
    st.subheader("2. Size 'em up!")
    msg = "How big should each space be, relative to everything else?"
    st.write(msg)
    for space in spaces:
        # with st.expander(space, expanded=False):
        # label = f"How big is your {space}, relative to everything else?"
        size = st.slider(space, min_value=0, max_value=10, key=space)
        # st.session_state["space_sizes"][space] = size
sizes = [st.session_state[spc] for spc in spaces]


if sum(sizes) > 0:
    st.subheader("3. Here's Your Two Dimensional DPI!")
    lg.treemap(spaces, sizes)


print(st.session_state)
# if "room_types" not in st.session_state:
#     st.session_state["room_types"] = ["Public Space", "Classroom", "Coworking", "Research Lab", "Cafe", "Nursery"]


# st.multiselect("What do you like?", st.session_state["room_types"])


# new_type = st.text_input("Add a room type")
# if new_type not in st.session_state["room_types"]:
#     st.session_state["room_types"].append(new_type)


# if "rooms" not in st.session_state:
#     st.session_state["rooms"] = {rm:0 for rm in st.session_state["room_types"]}

# for room_type in st.session_state["room_types"]:
#     if room_type != "":
#         with st.expander(room_type):
#             st.session_state["rooms"][room_type] = st.slider(f"How many {room_type} type rooms do you want?", min_value=1, max_value=10, key=room_type)

# if "" in st.session_state["rooms"]:
#     del(st.session_state["rooms"][""])
# print(st.session_state["rooms"])

# # volume = [350, 220, 170, 150, 50]
# # labels = ['Liquid\n volume: 350k', 'Savoury\n volume: 220k',
# #          'Sugar\n volume: 170k', 'Frozen\n volume: 150k',
# #          'Non-food\n volume: 50k']
# volume = st.session_state["rooms"].values()
# labels = st.session_state["rooms"].keys()
# color_list = ['#0f7216', '#b2790c', '#ffe9a3',
#              '#f9d4d4', '#d35158', '#ea3033']


# fig, ax = plt.subplots()
# plt.rc('font', size=14)
# squarify.plot(sizes=volume, label=labels,
#              color=color_list, alpha=0.7)
# plt.axis('off')
# st.pyplot(fig)


# # data = lg.treemap_dictionary(st.session_state["rooms"])
# # for node in data:
# #     print(node)


# # spec = plt.treemap(data)
# # st.vega_lite_chart(data, spec)