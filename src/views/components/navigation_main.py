import flet as ft

class NavigationMain(ft.NavigationBar):
    def __init__(self, on_change=None):
        super().__init__(
            bgcolor=ft.Colors.LIGHT_BLUE_500,
            indicator_color=ft.Colors.LIGHT_BLUE_300,
            destinations=[ 
            # Ícones da barra de navegação
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),

            ft.NavigationBarDestination(icon=ft.Icons.DOORBELL_SHARP, label="Inbox"),
            ft.NavigationBarDestination(
                icon=ft.Icons.FEATURED_PLAY_LIST,
                selected_icon=ft.Icons.FEATURED_PLAY_LIST,
                label="Projects",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.SETTINGS,
                selected_icon=ft.Icons.SETTINGS,
                label="Settings",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON,
                selected_icon=ft.Icons.PERSON,
                label="Account",
            ),
        ],
            on_change=lambda e: on_change(e.control.selected_index) if on_change else None
        )
