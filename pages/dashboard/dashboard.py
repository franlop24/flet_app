import flet as ft


class Dashboard(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.content = ft.Text("This is the dashboard page XD", color="black")
