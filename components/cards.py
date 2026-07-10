import flet as ft

from utils.colors import customTextColor, customTextHeaderColor


class CustomDisplayCard(ft.Container):
    def __init__(self, iconbg, title, value):
        super().__init__()

        self.iconbg = iconbg
        self.title = title
        self.value = value

        self.shadow = ft.BoxShadow(spread_radius=1, blur_radius=5, color="black")

        self.width = 250
        self.height = 80
        self.bgcolor = "white"

        self.card = ft.Row(
            controls=[
                ft.Container(
                    height=100,
                    width=80,
                    bgcolor=self.iconbg,
                    content=ft.Icon(icon=ft.Icons.PERSON_SHARP, color="white", size=50),
                ),
                ft.Container(
                    padding=ft.Padding.only(left=5, right=5),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                self.title,
                                color=customTextColor,
                                size=25,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                self.value,
                                color=customTextHeaderColor,
                                size=25,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ]
                    ),
                ),
            ]
        )

        self.content = self.card
