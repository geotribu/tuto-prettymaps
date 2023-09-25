# import des bibliothèques utilisées dans le script
import prettymaps

# adresse
adresse = "13 rue de l'Université, Paris, France"

# génération de la carte avec une adresse et un profil de paramètres par défaut
plot: prettymaps.draw.Plot = prettymaps.plot(
    query=adresse, save_as="sciencespo_paris.png"
)
