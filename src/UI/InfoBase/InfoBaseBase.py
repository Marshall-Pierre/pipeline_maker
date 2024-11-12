import flet as ft
from sqlalchemy.orm import Session

from ..BaseUI import Base
from src.UI.Components import SearchComponent
from . import DataTableUI
from src.Controller import InfoBaseController
from src.DB.Connection import SessionLocal
from src.Utils.EventBusInstance import event_bus


event_bus = event_bus


class InfoBase(Base):
    def __init__(self, page):
        self.db: Session = SessionLocal()
        self.data_info_base = InfoBaseController.get_all_info_base(self.db)
        super().__init__(page, "Bases")
        self.page_content = self.build_page()
        event_bus.subscribe("actualise_data", self.actualise_data)

    def update_data_table_ui(self):
        print("ok")

    def actualise_data(self):
        self.data_info_base = InfoBaseController.get_all_info_base(self.db)
        self.page_content.controls[2] = DataTableUI.data_table_ui(self.page, data=self.data_info_base)
        self.page.update()

    def build_page(self):
        return ft.Column(
            expand=True,
            controls=[
                self.add_header(),
                SearchComponent.search_component("Libelle", self.page),
                DataTableUI.data_table_ui(self.page, data=self.data_info_base)
            ]
        )