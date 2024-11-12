import flet as ft
from src.Enums.StateEnum import StateEnum
from src.Utils import LaunchBase
from . import EditInfoBase

def data_table_ui(page, data):
    def get_color(state):
        if state == StateEnum.DOWN.value:
            return ft.colors.RED
        else:
            return ft.colors.BLACK

    def launch_base(row):
        LaunchBase.launch_base([row.link_file_batch])

    def edit_base(row):
        dialog = EditInfoBase.edit_base(row)
        page.dialog = dialog
        dialog.open = True
        page.update()

    def on_button_click(_id):
        print(f"ID de la ligne: {_id}")

    return ft.Row(
        controls=[
            ft.DataTable(
                expand=True,
                columns=[
                    ft.DataColumn(ft.Text("ID")),
                    ft.DataColumn(ft.Text("Libelle")),
                    ft.DataColumn(ft.Text("Etat")),
                    ft.DataColumn(ft.Text("Action"))
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(d.id)),
                            ft.DataCell(ft.Text(d.libelle)),
                            ft.DataCell(ft.Text(StateEnum(d.state).name, color=get_color(StateEnum(d.state).value))),
                            ft.DataCell(
                                content=ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.IconButton(
                                                icon=ft.icons.NOT_STARTED_ROUNDED,
                                                on_click=lambda e, row=d: launch_base(row)),
                                            ft.IconButton(
                                                icon=ft.icons.MODE_EDIT_ROUNDED,
                                                on_click=lambda e, row=d: edit_base(row)),
                                        ]
                                    )
                                )
                            )
                        ]
                    ) for d in data
                ]
            )
        ]
    )