import flet as ft


from utils.colors import customTextHeaderColor, customBorderColor, customPrimaryColor
from components.fields import CustomTextField


class SignUp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        self.first_name = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(label="First Name"),
            border=ft.Border.all(width=1, color=customBorderColor),
        )
        self.surname = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(label="Surname"),
            border=ft.Border.all(width=1, color=customBorderColor),
        )
        self.email = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(label="Email"),
            border=ft.Border.all(width=1, color=customBorderColor),
        )
        self.email = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(label="Email"),
            border=ft.Border.all(width=1, color=customBorderColor),
        )
        self.password = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(
                label="Password", password=True, can_reveal_password=True
            ),
            border=ft.Border.all(width=1, color=customBorderColor),
        )
        self.confirm_password = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(
                label="Confirm Password", password=True, can_reveal_password=True
            ),
            border=ft.Border.all(width=1, color=customBorderColor),
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
                            ft.Text(
                                "Register",
                                color=customTextHeaderColor,
                                font_family="abeezee",
                                size=28,
                                weight=ft.FontWeight.NORMAL,
                            ),
                            ft.Divider(
                                color=customBorderColor, height=0.5, thickness=1.5
                            ),
                            self.first_name,
                            self.surname,
                            self.email,
                            self.password,
                            self.confirm_password,
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=40,
                                bgcolor=customPrimaryColor,
                                content=ft.Text("Login"),
                            ),
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=40,
                                content=ft.Text(
                                    "Create new account", color=customTextHeaderColor
                                ),
                                on_click=lambda e: page.go("/signup"),
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    expand=2,
                    image=ft.DecorationImage(
                        src="images/bg.png",
                        fit=ft.BoxFit.COVER,
                    ),
                    padding=ft.Padding.all(40),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(
                                icon=ft.Icons.LOCK_PERSON_ROUNDED,
                                size=200,
                                color="white",
                            ),
                            ft.Text(
                                "Signup section",
                                color="white",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                    ),
                ),
            ]
        )
