import flet as ft
from controllers.init import app
from ..components.navigation_main import NavigationMain
from ..components.appbarhome import AppBarHome
from ..components.list_view import ListView


def main(page: ft.Page):
    # configurações da página
    page.title = 'Feeny'
    page.window.width = 725
    page.window.height = 900
    page.theme_mode = ft.ThemeMode.LIGHT


    #Menu lateral
    drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(
                content=ft.Text("Menu", size=20, weight=ft.FontWeight.BOLD),
                padding=20,
            ),
            ft.Divider(),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.WB_SUNNY,
                label="My Day"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.CALENDAR_MONTH,
                label="Event"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.TASK_ALT_OUTLINED,
                label="Tasks"
            ),
        ]
    )

    def enddrawer(e):
        e.control.page.drawer = drawer
        drawer.open = True
        e.control.page.update()

    page.navigation_bar = NavigationMain()
    # Texto com efeito de gradiente
    meu_dia = ft.Text(
        spans=[
            ft.TextSpan(
                f"{app()!s}",
                ft.TextStyle(
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    foreground=ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            (0, 20), (150, 20), [ft.Colors.GREEN, ft.Colors.BLUE]
                        )
                    ),
                ),
            ),
        ],
    )
    page.appbar = AppBarHome(drawer=enddrawer)
    


    page.drawer = drawer
    page.add(meu_dia)
    page.add(ListView())
    page.update()