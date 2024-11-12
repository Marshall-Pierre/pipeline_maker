import flet as ft


def data_table_component(columns, rows):
    return ft.Row(
        controls=[
            ft.DataTable(
                expand=True,
                columns=[
                            ft.DataColumn(ft.Text(label)) for key, label in columns.items()
                            # Utilise l'étiquette pour l'affichage
                        ] + [
                            ft.DataColumn(ft.Text("Action"), numeric=True)  # Colonne "Action" avec largeur réduite
                        ],
                rows=[
                    ft.DataRow(
                        cells=[
                                  ft.DataCell(ft.Text(str(getattr(row, key, "")))) for key in columns.keys()
                                  # Utilise la clé pour extraire la valeur
                              ] + [
                                  ft.DataCell(ft.IconButton(icon=ft.icons.DELETE,
                                                            on_click=lambda e: print(
                                                                f"Action déclenchée pour la ligne {row}")))
                                  # Cellule d'action
                              ]
                    ) for row in rows
                ]
            )
        ]
    )