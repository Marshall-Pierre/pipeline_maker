import flet as ft
from sqlalchemy.orm import Session

from src.Controller import InfoBaseController
from src.DB.Connection import SessionLocal
from src.Schema import InfoBaseSchema
from src.Utils import EventBusInstance


libelle_field = ft.TextField(label="Libelle")
link_field = ft.TextField(multiline=True, label="Lien")
diffusion_field = ft.TextField(multiline=True, label="Diffusion")

event_bus = EventBusInstance.event_bus

def edit_base(row):
    libelle_field.value = row.libelle
    link_field.value = row.link_file_batch
    diffusion_field.value = row.diffusion
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(f"Modifier des informations de la base: {row.libelle}"),
        content=ft.Column([
            libelle_field,  # Utilise directement les champs de texte définis en haut
            link_field,
            diffusion_field
        ]),
        actions=[
            ft.TextButton("Supprimer", on_click=lambda e: delete_data(dialog, row),
                          style=ft.ButtonStyle(color=ft.colors.RED)),
            ft.TextButton("Annuler", on_click=lambda e: close_dialog(dialog)),
            ft.TextButton("Enregistrer", on_click=lambda e: save_data(dialog, row))
        ],
        on_dismiss=lambda e: print("Dialogue fermé")
    )
    return dialog

# Fonction pour fermer la boîte de dialogue
def close_dialog(dialog):
    dialog.open = False
    dialog.page.update()

def save_data(dialog, row):
    db: Session = SessionLocal()
    # Récupère les valeurs des champs de texte
    row.libelle = libelle_field.value
    row.link_file_batch = link_field.value
    row.diffusion = diffusion_field.value

    update_info_base = InfoBaseController.update_info_base(db, row)
    print(update_info_base)
    # Réinitialise les champs de texte après enregistrement
    libelle_field.value = ""
    link_field.value = ""
    diffusion_field.value = ""
    dialog.page.update()
    event_bus.emit("actualise_data", 1)
    # Fermer le dialogue
    close_dialog(dialog)

def delete_data(dialog, row):
    db: Session = SessionLocal()
    delete_info_base = InfoBaseController.delete_info_base(db, row.id)
    print(delete_info_base)
    dialog.page.update()
    event_bus.emit("actualise_data", 1)
    # Fermer le dialogue
    close_dialog(dialog)




