import flet as ft
from ..InfoBase.AddInfoBase import add_info_modal

def search_component(libelle, page):
    def open_modal(e):
        dialog = add_info_modal()
        page.dialog = dialog
        dialog.open = True
        page.update()

    return ft.Row(
        controls=[
            ft.TextField(
                expand=True,
                label=libelle,
                autofill_hints=ft.AutofillHint.NAME,
            ),
            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=open_modal)
        ]
    )