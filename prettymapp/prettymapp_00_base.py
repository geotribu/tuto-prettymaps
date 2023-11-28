# import des bibliothèques utilisées dans le script
from prettymapp.geo import get_aoi
from prettymapp.osm import get_osm_geometries
from prettymapp.plotting import Plot
from prettymapp.settings import STYLES

# variables
adresse = "Saint-Malo, France"
adresse = 50.98682, 2.12736
# adresse = 48.89312, 2.38987
style_name = "PEACH"

if isinstance(adresse, str):
    output_name = f"{''.join(e for e in adresse if e.isalnum())}_{style_name}.png"
    aoi = get_aoi(address=adresse, radius=600, rectangular=False)
elif isinstance(adresse, tuple):
    output_name = (
        f"{''.join(str(e).replace('.', '_') for e in adresse)}_{style_name}.png"
    )
    aoi = get_aoi(coordinates=adresse, radius=500, rectangular=False)

df = get_osm_geometries(aoi=aoi)

fig = Plot(
    df=df,
    aoi_bounds=aoi.bounds,
    draw_settings=STYLES[style_name.title()],
    name_on=True,
    name="Fort de Gravelines",
    text_x=-35,
    text_y=40,
    text_rotation=-25,
).plot_all()

fig.savefig(
    output_name,
    metadata={"Author": "Geotribu", "Software": "prettymapp"},
)
