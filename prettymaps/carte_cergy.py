# import des bibliothèques utilisées dans le script
import prettymaps

# génération de la carte et sauvegarde sous forme d'image
plot: prettymaps.draw.Plot = prettymaps.plot(
    # query=(49.0332, 2.0490),
    query="étang de la Folie, Cergy, France",
    preset="macao",
    save_as="cergy.png",
    title="Étang de la Folie, Cergy",
    radius=False,
)
