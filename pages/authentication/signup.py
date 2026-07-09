import asyncio

import flet as ft


from db import db_path
from db.crud import check_data_exists, connect_to_database, insert_data
from utils.colors import customTextHeaderColor, customBorderColor, customPrimaryColor
from components.fields import CustomTextField
from utils.validation import Validation


class SignUp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.bgcolor = "white"
        self.expand = True
        self.validation = Validation()
        self.error_border = ft.Border.all(3, "red")
        self.default_border = ft.Border.all(1, customBorderColor)
        self.error_field = ft.Text(value="", color="red", size=0)

        self.first_name = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(label="First Name"),
            border=ft.Border.all(1, customBorderColor),
        )
        self.surname = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(label="Surname"),
            border=ft.Border.all(1, customBorderColor),
        )
        self.email = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(label="Email"),
            border=ft.Border.all(1, customBorderColor),
        )
        self.password = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(
                label="Password", password=True, can_reveal_password=True
            ),
            border=ft.Border.all(1, customBorderColor),
        )
        self.confirm_password = ft.Container(
            padding=ft.Padding.all(4),
            content=CustomTextField(
                label="Confirm Password", password=True, can_reveal_password=True
            ),
            border=ft.Border.all(1, customBorderColor),
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
                            self.error_field,
                            self.first_name,
                            self.surname,
                            self.email,
                            self.password,
                            self.confirm_password,
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=40,
                                bgcolor=customPrimaryColor,
                                content=ft.Text("Signup"),
                                on_click=self.signup,
                            ),
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                height=40,
                                content=ft.Text(
                                    "Have an Account/Login", color=customTextHeaderColor
                                ),
                                on_click=lambda e: page.navigate("/login"),
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

    async def signup(self, e):
        print("this is our signup")
        first_name = self.first_name.content.value
        surname = self.surname.content.value
        email = self.email.content.value
        password = self.password.content.value
        confirm_password = self.confirm_password.content.value

        if first_name and surname and email and password and confirm_password:
            conn = connect_to_database(db_path)

            if not self.validation.is_valid_email(email):
                self.email.border = self.error_border
                self.error_field.value = "Enter a valid email"
                self.error_field.size = 12
                self.error_field.update()
                self.email.update()

                await asyncio.sleep(1)
                self.email.border = self.default_border
                self.error_field.size = 0
                self.error_field.update()
                self.email.update()

            elif not check_data_exists(conn, "user", f"email='{email}'"):
                insert_data(conn, "user", (first_name, surname, email, password))
                self.page.splash = ft.ProgressBar()
                self.error_field.value = "You have succefully been registered"
                self.error_field.color = "green"
                self.error_field.size = 12
                self.page.update()

                await asyncio.sleep(1)
                self.page.splash = None
                self.page.update()
                self.page.navigate("/login")

            else:
                self.email.border = self.error_border
                self.error_field.value = "Email already exists"
                self.error_field.size = 12
                self.error_field.update()
                self.email.update()

                await asyncio.sleep(1)
                self.email.border = self.default_border
                self.error_field.size = 0
                self.error_field.update()
                self.email.update()
        else:
            self.error_field.value = "all fields are needed"
            self.error_field.size = 12
            self.error_field.update()

            await asyncio.sleep(2)

            self.error_field.size = 0
            self.error_field.update()
