import json
from pathlib import Path

import prettymaps

# charge les préréglages depuis un JSON
preset_christmas_file = Path(__file__).parent.joinpath("preset_christmas.json")
with preset_christmas_file.open(mode="r", encoding="UTF-8") as file:
    christmas_preset = json.load(file)


# enregistre le préréglage
prettymaps.create_preset("christmas", **christmas_preset)

# Define the location - Rovaniemi, Finland = village du Père Noël
# location = "Joulupukin Pajakylä, Rovaniemi, Finland"
# location = (66.5070, 25.7312)
location = (48.646201, -2.015234)  # bassin Jacques Cartier, Saint-Malo, France

# Plot the map using the 'christmas' preset
plot = prettymaps.plot(
    query=location,
    preset="christmas",  # Use the Christmas preset
    save_as="test_noel.png",
    # figsize=(10, 10),  # Define the size of the plot
)
