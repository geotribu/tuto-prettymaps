# import des bibliothèques utilisées dans le script
from prettymapp.geo import get_aoi
from prettymapp.osm import get_osm_geometries
from prettymapp.plotting import Plot
from prettymapp.settings import STYLES

# variables
adresse = "Saint-Malo, France"
adresse = 50.98682, 2.12736
radius = 600

# télécharge les objets et les charge en data frame
for style_name in STYLES.keys():
    if isinstance(adresse, str):
        output_name = f"{''.join(e for e in adresse if e.isalnum())}_{style_name}.png"
        aoi = get_aoi(address=adresse, radius=radius, rectangular=False)
    elif isinstance(adresse, tuple):
        aoi = get_aoi(coordinates=adresse, radius=radius, rectangular=False)
        output_name = (
            f"{''.join(str(e).replace('.', '_') for e in adresse)}_{style_name}.png"
        )
    df = get_osm_geometries(aoi=aoi)

    fig = Plot(
        df=df, aoi_bounds=aoi.bounds, draw_settings=STYLES[style_name]
    ).plot_all()

    fig.savefig(output_name, pil_kwargs={"quality": 80})

    del fig
