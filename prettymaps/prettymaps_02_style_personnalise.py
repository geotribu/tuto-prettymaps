import prettymaps

adresse = "Saint-Malo, France"


plot: prettymaps.draw.Plot = prettymaps.plot(
    query=adresse,
    title="Geotribu",
    # credit="Geotribu",
    save_as="SaintMalo_advanced.png",
    circle=True,
    radius=1100,
    layers={
        "green": {
            "tags": {
                "landuse": "grass",
                "natural": ["island", "wood"],
                "leisure": "park",
            }
        },
        "forest": {"tags": {"landuse": "forest"}},
        "water": {"tags": {"natural": ["water", "bay"]}},
        "parking": {
            "tags": {"amenity": "parking", "highway": "pedestrian", "man_made": "pier"}
        },
        "streets": {
            "width": {
                "motorway": 2.5,
                "trunk": 2,
                "primary": 2,
                "secondary": 2,
                "tertiary": 2,
                "residential": 2,
            }
        },
        "building": {
            "tags": {"building": True},
        },
        "bars": {
            "tags": {"amenity": ["bar", "pub"]},
        },
    },
    style={
        "background": {
            "fc": "#EAEAE5",
            "ec": "#EAEAE5",
            "hatch": "ooo...",
        },
        "perimeter": {
            "fc": "#EAEAE5",
            "ec": "#EAEAE5",
            "lw": 0,
            "hatch": "ooo...",
        },
        "green": {
            "fc": "#EAEAE5",
            "ec": "#EAEAE5",
            "lw": 1,
        },
        "forest": {
            "fc": "#EAEAE5",
            "ec": "#EAEAE5",
            "lw": 1,
        },
        "water": {
            "fc": "#EAEAE5",
            "ec": "#EAEAE5",
            "hatch": "ooo...",
            "hatch_c": "#EAEAE5",
            "lw": 1,
        },
        "parking": {
            "fc": "#EAEAE5",
            "ec": "#EAEAE5",
            "lw": 1,
        },
        "streets": {
            "fc": "#EAEAE5",
            "ec": "#EAEAE5",
            "alpha": 1,
            "lw": 0,
        },
        "building": {
            "palette": ["#EAEAE4", "#EAEAE5", "#EAEAE6"],
            "ec": "#EAEAE5",
            "lw": 0.5,
        },
        "bars": {
            "fc": "#EAEAE5",
            "lw": 1,
        },
    },
)


plot = prettymaps.plot(
    "Praça Ferreira do Amaral, Macau",
    circle=True,
    radius=1100,
    layers={
        "green": {
            "tags": {
                "landuse": "grass",
                "natural": ["island", "wood"],
                "leisure": "park",
            }
        },
        "forest": {"tags": {"landuse": "forest"}},
        "water": {"tags": {"natural": ["water", "bay"]}},
        "parking": {
            "tags": {"amenity": "parking", "highway": "pedestrian", "man_made": "pier"}
        },
        "streets": {
            "width": {
                "motorway": 5,
                "trunk": 5,
                "primary": 4.5,
                "secondary": 4,
                "tertiary": 3.5,
                "residential": 3,
            }
        },
        "building": {
            "tags": {"building": True},
        },
    },
    style={
        "background": {
            "fc": "#F2F4CB",
            "ec": "#dadbc1",
            "hatch": "ooo...",
        },
        "perimeter": {
            "fc": "#F2F4CB",
            "ec": "#dadbc1",
            "lw": 0,
            "hatch": "ooo...",
        },
        "green": {
            "fc": "#D0F1BF",
            "ec": "#2F3737",
            "lw": 1,
        },
        "forest": {
            "fc": "#64B96A",
            "ec": "#2F3737",
            "lw": 1,
        },
        "water": {
            "fc": "#a1e3ff",
            "ec": "#2F3737",
            "hatch": "ooo...",
            "hatch_c": "#85c9e6",
            "lw": 1,
        },
        "parking": {
            "fc": "#F2F4CB",
            "ec": "#2F3737",
            "lw": 1,
        },
        "streets": {
            "fc": "#2F3737",
            "ec": "#475657",
            "alpha": 1,
            "lw": 0,
        },
        "building": {
            "palette": ["#FFC857", "#E9724C", "#C5283D"],
            "ec": "#2F3737",
            "lw": 0.5,
        },
    },
)
