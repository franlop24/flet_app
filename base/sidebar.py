import flet as ft

from utils.colors import customBgColor, customTextColor


class SideBar(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        page.padding = 0

        self.width = 200
        self.bgcolor = customBgColor
        self.alignment = ft.Alignment.CENTER

        self.menu = ft.Column(
            spacing=0,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    margin=0,
                    padding=ft.Padding.only(top=20, left=10),
                    content=ft.Column(
                        alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                padding=ft.Padding.only(bottom=20, left=40),
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "My POS", size=19, color=customTextColor
                                        )
                                    ]
                                ),
                            ),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(
                                            icon=ft.Icons.DASHBOARD_OUTLINED,
                                            color="black",
                                        ),
                                        ft.Text(
                                            "Dashboard", size=14, color=customTextColor
                                        ),
                                    ]
                                ),
                            ),
                            ft.Divider(
                                color=customTextColor, height=0.5, thickness=0.5
                            ),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(
                                            icon=ft.Icons.DASHBOARD_OUTLINED,
                                            color="black",
                                        ),
                                        ft.Text(
                                            "Profile", size=14, color=customTextColor
                                        ),
                                    ]
                                ),
                            ),
                            ft.Divider(
                                color=customTextColor, height=0.5, thickness=0.5
                            ),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(
                                            icon=ft.Icons.DASHBOARD_OUTLINED,
                                            color="black",
                                        ),
                                        ft.Text(
                                            "Products", size=14, color=customTextColor
                                        ),
                                    ]
                                ),
                            ),
                            ft.Divider(
                                color=customTextColor, height=0.5, thickness=0.5
                            ),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(
                                            icon=ft.Icons.DASHBOARD_OUTLINED,
                                            color="black",
                                        ),
                                        ft.Text(
                                            "Logout", size=14, color=customTextColor
                                        ),
                                    ]
                                ),
                            ),
                            ft.Divider(
                                color=customTextColor, height=0.5, thickness=0.5
                            ),
                        ],
                    ),
                )
            ],
        )

        self.content = self.menu
