import flet as ft
import asyncio

from db import db_path
from db.crud import check_data_exists, connect_to_database, get_data
from utils.colors import customTextHeaderColor, customBorderColor, customPrimaryColor
from components.fields import CustomTextField
from utils.validation import Validation


class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True
        self.validation = Validation()
        self.error_border = ft.Border.all(3, "red")
        self.default_border = ft.Border.all(1, customBorderColor)
        self.error_field = ft.Text(value="", color="red", size=0)

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
                                "Welcome Back",
                                color=customTextHeaderColor,
                                font_family="abeezee",
                                size=28,
                                weight=ft.FontWeight.NORMAL,
                            ),
                            self.error_field,
                            self.email,
                            self.password,
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=40,
                                bgcolor=customPrimaryColor,
                                content=ft.Text("Login"),
                                on_click=self.login,
                            ),
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=40,
                                content=ft.Text(
                                    "Create new account", color=customTextHeaderColor
                                ),
                                on_click=lambda e: page.navigate("/signup"),
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
                                "Login section",
                                color="white",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                    ),
                ),
            ]
        )

    async def login(self, e):
        email = self.email.content.value
        password = self.password.content.value

        if email and password:
            conn = connect_to_database(db_path)

            if check_data_exists(conn, "user", f"email='{email}'"):
                get_user = get_data(conn, "user", f"email='{email}'")
                is_email_match = get_user[0]["email"] == email
                is_password_match = get_user[0]["password"] == password

                if is_email_match and is_password_match:
                    self.page.splash = ft.ProgressBar()
                    self.page.update()
                    await asyncio.sleep(1)
                    self.page.splash = None
                    self.page.navigate("/")
            else:
                self.password.border = self.error_border
                self.email.border = self.error_border
                self.error_field.value = "Email or Password is incorrect"
                self.error_field.size = 12
                self.password.update()
                self.email.update()
                self.error_field.update()

                await asyncio.sleep(1)
                self.password.border = self.default_border
                self.email.border = self.default_border
                self.error_field.value = ""
                self.error_field.size = 0
                self.password.update()
                self.email.update()
                self.error_field.update()
