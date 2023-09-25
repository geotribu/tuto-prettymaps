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
    },
    style={
        "background": {
            "fc": "#DCE0DC",
            "ec": "#dadbc1",
            "hatch": "ooo...",
        },
        "perimeter": {
            "fc": "#DCE0DC",
            "ec": "#dadbc1",
            "lw": 0,
            "hatch": "ooo...",
        },
        "green": {
            "fc": "#2B2F77",
            "ec": "#2F3737",
            "lw": 1,
        },
        "forest": {
            "fc": "#2B2F77",
            "ec": "#2F3737",
            "lw": 1,
        },
        "water": {
            "fc": "#C2C8CA",
            "ec": "#C2C8CA",
            "hatch": "ooo...",
            "hatch_c": "#C2C8CA",
            "lw": 1,
        },
        "parking": {
            "fc": "#E6E9E5",
            "ec": "#2F3737",
            "lw": 1,
        },
        "streets": {
            "fc": "#1C1F31",
            "ec": "#475657",
            "alpha": 1,
            "lw": 0,
        },
        "building": {
            "palette": ["#EAEAE5", "#EAEAE5", "#EAEAE6"],
            "ec": "#DBDBDA",
            "lw": 0.5,
        },
    },
)
