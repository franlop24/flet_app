import flet as ft
from utils.colors import customTextColor


class CustomTextField(ft.TextField):
    def __init__(
            self,
            label,
            icon=None,
            password=False,
            can_reveal_password=False,
            error_text=None,      # Movido hacia arriba
            input_filter=None,    # Movido hacia arriba
            border=ft.InputBorder.NONE,  # Los valores por defecto complejos van al final
            **kwargs
    ):
        super().__init__(
            label=label,
            border=border,
            color=customTextColor,
            password=password,
            can_reveal_password=can_reveal_password,
            content_padding=ft.Padding.only(
                top=0, bottom=0, left=0, right=0),  # Tu sintaxis con mayúscula
            hint_style=ft.TextStyle(size=14, color=customTextColor),
            label_style=ft.TextStyle(color=customTextColor),
            input_filter=input_filter,
            focus_color=customTextColor,
            prefix_icon=icon,
            **kwargs
        )

        self.error_text = error_text,
