import prettymaps

# Draw several regions on the same canvas
prettymaps.multiplot(
    prettymaps.Subplot(
        "13001, Marseille, France",
        style={"building": {"palette": ["#49392C", "#E1F2FE", "#98D2EB"]}},
    ),
    prettymaps.Subplot(
        "13002, Marseille, France",
        style={"building": {"palette": ["#BA2D0B", "#D5F2E3", "#73BA9B", "#F79D5C"]}},
    ),
    prettymaps.Subplot(
        "13003, Marseille, France",
        style={"building": {"palette": ["#EEE4E1", "#E7D8C9", "#E6BEAE"]}},
    ),
    # Load a global preset
    preset="cb-bf-f",
    # Figure size
    figsize=(12, 12),
    save_as="multi_marseille.png",
)
