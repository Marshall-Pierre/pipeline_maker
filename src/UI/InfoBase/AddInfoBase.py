import flet as ft
from sqlalchemy.orm import Session

from src.Controller import InfoBaseController
from src.DB.Connection import SessionLocal
from src.Schema import InfoBaseSchema

# Variables pour stocker les champs de texte
libelle_field = ft.TextField(label="Libelle", width=200)
link_field = ft.TextField(label="Lien", width=200)


def add_info_modal():
    # Création de la boîte de dialogue modale pour la saisie
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Ajouter des informations"),
        content=ft.Column([
            libelle_field,  # Utilise directement les champs de texte définis en haut
            link_field
        ]),
        actions=[
            ft.TextButton("Annuler", on_click=lambda e: close_dialog(dialog)),
            ft.TextButton("Enregistrer", on_click=lambda e: save_data(dialog))
        ],
        on_dismiss=lambda e: print("Dialogue fermé")
    )
    return dialog


# Fonction pour fermer la boîte de dialogue
def close_dialog(dialog):
    dialog.open = False
    dialog.page.update()


# Fonction pour sauvegarder les données saisies
def save_data(dialog):
    db: Session = SessionLocal()
    # Récupère les valeurs des champs de texte
    libelle = libelle_field.value
    link = link_field.value
    new_info_base = InfoBaseSchema.Create(libelle=libelle, link_file_batch=link)
    created_info_base = InfoBaseController.add_info_base(db, new_info_base)
    if created_info_base:
        print(f"Données enregistrées : Nom = {libelle}, Email = {link}")
    # Réinitialise les champs de texte après enregistrement
    libelle_field.value = ""
    link_field.value = ""
    dialog.page.update()
    # Fermer le dialogue
    close_dialog(dialog)