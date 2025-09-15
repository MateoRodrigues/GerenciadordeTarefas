import flet as ft

class AppBarHome(ft.AppBar):
    def __init__(self, on_menu_click=None, drawer=None):
        super().__init__(
            leading=ft.IconButton(ft.Icons.MENU,on_click= drawer)
        )