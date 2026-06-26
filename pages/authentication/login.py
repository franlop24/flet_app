import flet as ft


from utils.colors import customTextHeaderColor, customBorderColor, customPrimaryColor
from components.fields import CustomTextField


class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        self.email = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(label="Email"),
            border=ft.Border.all(width=1, color=customBorderColor)
        )

        self.password = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(
                label="Password", password=True, can_reveal_password=True),
            border=ft.Border.all(width=1, color=customBorderColor)
        )

        self.content = ft.Row(
            controls=[
                ft.Container(
                    expand=2,
                    padding=ft.Padding.all(40),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                        controls=[
                            ft.Text("Welcome Back", color=customTextHeaderColor,
                                    size=40, weight=ft.FontWeight.NORMAL),
                            self.email,
                            self.password,
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=40,
                                bgcolor=customPrimaryColor,
                                content=ft.Text("Login")
                            ),
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=40,
                                content=ft.Text(
                                    "Create new account", color=customTextHeaderColor),
                                on_click=lambda e: page.go("/signup")

                            )
                        ]
                    )
                ),
                ft.Container(
                    expand=2,
                    image=ft.DecorationImage(
                        src="images/bg.png",  # Tu URL o ruta local
                        fit="cover"           # Cómo se adapta la imagen
                    ),
                    padding=ft.Padding.all(40),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(icon=ft.Icons.LOCK_PERSON_ROUNDED,
                                    size=200, color="white"),
                            ft.Text("Login section", color="white",
                                    size=20, weight=ft.FontWeight.BOLD)
                        ]
                    )
                )
            ]
        )
