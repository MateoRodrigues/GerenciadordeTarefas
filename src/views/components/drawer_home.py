import flet as ft

class NavigationDrawerHome(ft.NavigationDrawer):
    def __init__(self, **kwargs):
        super().__init__(
        controls = [
            ft.Container(
                content=ft.Text("Menu", size=20, weight=ft.FontWeight.BOLD),
                padding=20,
            ),
            ft.Divider(),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.HOME,
                label="Início"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.SETTINGS,
                label="Sobre"
            ),
        ], **kwargs)
