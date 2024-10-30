from src.DB import Migration, Connection
import flet as ft
from src.Router import InitRouter


Migration.Base.metadata.create_all(bind=Connection.engine)

def main(page: ft.Page):
    page.title = "Pipeline Maker"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT

    router = InitRouter.InitRouter(page)
    page.on_route_change = lambda e: router.navigate(e.route)
    page.go("/")

ft.app(target=main)
