COMMON_SPACES = {
    "Auditorium": {
        "price":    50,
        "qty":      0,
        "size":     5,
        "color":    "#e54c28",
    },
    "Meeting Room": {
        "price":    10,
        "qty":      0,
        "size":     1,
        "color":    "#cbebde",
    },
    # "Atrium": {
    #     "price":    10,
    #     "qty":      0,
    #     "size":     1,
    #     "color":    "",
    # },
    "Lounge": {
        "price":    10,
        "qty":      0,
        "size":     2,
        "color":    "#30618C",
    },
    "Cafe": {
        "price":    30,
        "qty":      0,
        "size":     2,
        "color":    "#f9941b",
    },
    # "Retail": {
    #     "price":    10,
    #     "qty":      0,
    #     "size":     1,
    #     "color":    "",
    # },
    "Exhibition Space": {
        "price":    20,
        "qty":      0,
        "size":     3,
        "color":    "#2D402A",
    },
    # "Plaza/Terrace": {
    #     "price":    10,
    #     "qty":      0,
    #     "size":     1,
    #     "color":    "",
    # },
    "Library": {
        "price":    10,
        "qty":      0,
        "size":     3,
        "color":    "#BFBA73",
    },
    "Community Garden": {
        "price":    10,
        "qty":      0,
        "size":     2,
        "color":    "#022859",
    },
    "Entranceway": {
        "price":    30,
        "qty":      0,
        "size":     2,
        "color":    "#5F734C",
    },
    "Kitchen": {
        "price":    20,
        "qty":      0,
        "size":     1,
        "color":    "#D9C9BA",
    },
    "Huddle": {
        "price":    20,
        "qty":      0,
        "size":     1,
        "color":    "#e7531c",
    },
}


TECH_SPACES = {
    "Flex Engineering Lab": {
        "price":    40,
        "qty":      0,
        "size":     2,
        "color":    "#022859",
    },
    "Classroom": {
        "price":    15,
        "qty":      0,
        "size":     1,
        "color":    "#fdb10e",
    },
}


ACADEMIC_SPACES = {
    "Wet Lab": {
        "price":    80,
        "qty":      0,
        "size":     1,
        "color":    "#0c74bc",
    },
    "Private Office": {
        "price":    10,
        "qty":      0,
        "size":     0.5,
        "color":    "#4abd8d",
    },
}


BIZNESS_SPACES = {
    "Co-Working Space": {
        "price":    25,
        "qty":      0,
        "size":     2,
        "color":    "#733E39",
    },
    "Prototyping Lab":  {
        "price":    45,
        "qty":      0,
        "size":     3,
        "color":    "#EBEEF2",
    },
}


AMENITIES = {
    "Free Public Transit":  {
        "price":    20,
        "qty":      0,
        "size":     1,
    },
    "Free Meals":  {
        "price":    25,
        "qty":      0,
        "size":     1,
    },
    "Community Liasons":  {
        "price":    75,
        "qty":      0,
        "size":     1,
    },
}


SPACES = {
    **COMMON_SPACES, 
    **TECH_SPACES, 
    **ACADEMIC_SPACES, 
    **BIZNESS_SPACES, 
}
    # **AMENITIES,
    # **CUSTOM_SPACES}