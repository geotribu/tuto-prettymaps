# standard
import logging

# 3rd party
import prettymaps

# -- Globals
presets = (
    "barcelona",
    "barcelona-plotter",
    "cb-bf-f",
    "default",
    "heerhugowaard",
    "macao",
    "minimal",
    "tijuca",
)


# -- Main
adresse = "Callao, Lima Metropolitan Area, Constitutional Province of Callao, Peru"

for p in presets:
    print(f"Carte de '{adresse}' avec le préréglage '{p}'")
    try:
        plot: prettymaps.draw.Plot = prettymaps.plot(
            query=adresse,
            preset=p,
            save_as=f"{''.join(e for e in adresse if e.isalnum())}_{p}.png",
        )
    except Exception as err:
        logging.error(
            f"La génération de la carte de '{adresse}' avec le préréglage '{p}' a échoué."
            f" Trace : {err}"
        )
        continue
