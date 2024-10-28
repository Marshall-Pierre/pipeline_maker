import flet as ft


class InitRouter:
    def __init__(self, page):
        self.page = page
        self.nav_rail = self.create_nav_rail()

    def create_nav_rail(self):
        return ft.NavigationRail(
            selected_index=0,
            bgcolor=ft.colors.RED_900,
            on_change=self.on_nav_change,
            min_width=100,
            min_extended_width=400,
            destinations=[
                ft.NavigationRailDestination(icon=ft.icons.HOME, label_content=ft.Text("Accueil",
                                                                                       color=ft.colors.WHITE, )),
            ]
        )

    def on_nav_change(self, e):
        selected_route = "/" if e.control.selected_index == 0 else "/home"
        self.page.go(selected_route)

    def navigate(self, route):
        if route == "/":
            self.page.views.clear()
            self.page.views.append(
                ft.View(
                    controls=[
                        ft.Row([
                            self.nav_rail,
                        ],
                            expand=True
                        )
                    ]
                )
            )
        self.page.update()
