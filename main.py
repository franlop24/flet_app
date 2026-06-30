import flet as ft

from router import views_handler


def main(page: ft.Page):
    def route_change():
        page.views.clear()
        page.views.append(views_handler(page)[page.route])

        page.fonts = {"abeezee": "fonts/ABeeZee-Regular"}

    page.on_route_change = route_change

    page.go("/login")


ft.app(target=main, assets_dir="assets")
