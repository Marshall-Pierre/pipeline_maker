from ..BaseUI import Base
import flet as ft


class HomeBase(Base):
    def __init__(self, page):
        super().__init__(page, "Page d'acceuil")
        self.page_content = self.build_page()

    def build_page(self):
        return ft.Column(
            expand=True,
            controls=[
                self.add_header(),
                ft.Text("Bienvenue !")
            ]
        )
