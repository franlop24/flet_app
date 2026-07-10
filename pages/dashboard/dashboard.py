import flet as ft

from components.cards import CustomDisplayCard
from utils.colors import customDashboardBG, customTextHeaderColor


class Dashboard(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True
        self.bgcolor = customDashboardBG

        self.main_content = ft.Column(
            controls=[
                ft.Container(
                    bgcolor="white",
                    padding=ft.Padding.all(20),
                    content=ft.Text(
                        "Dashboard",
                        color=customTextHeaderColor,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
                ft.Divider(color="black", height=0.5, thickness=0.5),
                ft.Container(
                    padding=ft.Padding.all(20),
                    content=ft.Row(controls=[CustomDisplayCard()]),
                ),
            ]
        )

        self.content = ft.Row(
            spacing=0, controls=[ft.Container(expand=True, content=self.main_content)]
        )
