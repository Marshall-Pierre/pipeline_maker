import flet as ft
from sqlalchemy.orm import Session

from ..BaseUI import Base
from src.UI.Components import SearchComponent
from src.UI.Components import DataTableComponent
from src.Controller import InfoBaseController
from src.DB.Connection import SessionLocal


class InfoBase(Base):
    def __init__(self, page):
        self.db: Session = SessionLocal()
        self.data_info_base = InfoBaseController.get_all_info_base(self.db)
        super().__init__(page, "Bases")
        self.page_content = self.build_page()



    def build_page(self):
        return ft.Column(
            expand=True,
            controls=[
                self.add_header(),
                SearchComponent.search_component("Libelle", self.page),
                DataTableComponent.data_table_component(
                    {"id":"ID", "libelle": "Libelle", "state": "Statut"}, rows=self.data_info_base
                )
            ]
        )
