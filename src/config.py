ACADEMIC_SPACES = [
    "Flex Engineering Lab",
    "Wet Lab",
    "Private Office",
    "Classroom",
    "Food Research Lab",
]
ACADEMIC_SPACES = sorted(ACADEMIC_SPACES)

ACADEMIC_COLORS = [
    "#022859",
    "#5F734C",
    "#D9C9BA",
    "#8C6151",
    "#733E39",
]
ACADEMIC_COLORS = {name:color for name, color in zip(ACADEMIC_SPACES, ACADEMIC_COLORS)}

COMMON_SPACES = [
    "Auditoriam",
    "Meeting Room",
    "Atrium",
    "Lounge",
    "Cafe",
    "Retail",
    "Exhibition Space",
    "Plaza/Terrace",
    "Library",
    "Community Garden"
]
COMMON_SPACES = sorted(COMMON_SPACES)

COMMON_COLORS = [
    "#1E2940",
    "#30618C",
    "#688EA6",
    "#2D402A",
    "#BFBA73",
    "#022859",
    "#5F734C",
    "#D9C9BA",
    "#8C6151",
    "#733E39",
]
COMMON_COLORS = {name:color for name, color in zip(COMMON_SPACES, COMMON_COLORS)}


CUSTOM_COLORS  = [
    "#EBEEF2",
    "#111E26",
    "#375932",
    "#7F8C4F",
    "#A4A680",
]
# CUSTOM_COLORS = [color for color in CUSTOM_COLORS + list(COMMON_COLORS.values()) + list(ACADEMIC_COLORS.values())]