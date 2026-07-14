import flet as ft

from utils.colors import customTextColor, customBgColor, customPrimaryColor


class TopBar(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.padding = ft.Padding.only(left=20, right=20)
        self.margin = 0
        self.shadow = ft.BoxShadow(spread_radius=2, blur_radius=2, color="1a000000")

        self.bgcolor = customPrimaryColor

        self.height = 50

        self.menu = ft.Row(
            controls=[
                ft.Icon(icon=ft.Icons.MENU_OUTLINED, color="black"),
                ft.Container(
                    content=ft.MenuBar(
                        expand=True,
                        style=ft.MenuStyle(
                            bgcolor=customPrimaryColor,
                            mouse_cursor={
                                ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                                ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                            },
                        ),
                        controls=[
                            ft.SubmenuButton(
                                content=ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Icon(
                                                icon=ft.Icons.PERSON, color="black"
                                            ),
                                            ft.Text("Welcome Admin", color="black"),
                                        ]
                                    )
                                ),
                                controls=[
                                    ft.MenuItemButton(
                                        width=150,
                                        content=ft.Text("Profile", color="black"),
                                        leading=ft.Icon(
                                            icon=ft.Icons.INFO, color="black"
                                        ),
                                        style=ft.ButtonStyle(bgcolor="white"),
                                    ),
                                    ft.MenuItemButton(
                                        width=150,
                                        content=ft.Text("Logout", color="black"),
                                        leading=ft.Icon(
                                            icon=ft.Icons.LOGOUT_OUTLINED, color="black"
                                        ),
                                        style=ft.ButtonStyle(bgcolor="white"),
                                        on_click=lambda _: self.page.navigate("/login"),
                                    ),
                                ],
                            )
                        ],
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        self.content = self.menu
