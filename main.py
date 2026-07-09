import flet as ft

from db.db import create_database
from pages.authentication.login import Login
from pages.authentication.signup import SignUp

# from postgres.database import test_connection

# from router import views_handler


def main(page: ft.Page):
    # test_connection()
    create_database()

    page.bgcolor = "white"
    page.padding = ft.Padding.all(0)

    def route_change():
        page.clean()
        # page.views.append(views_handler(page)[page.route])
        if page.route == "/login":
            page.add(Login(page))

        if page.route == "/signup":
            page.add(SignUp(page))

        page.fonts = {"abeezee": "fonts/ABeeZee-Regular"}

    page.on_route_change = route_change

    page.navigate("/login")


ft.app(target=main, assets_dir="assets")
