import flet as ft


def main(page: ft.Page):
    page.title = 'Gerenciador de tarefas'
    page.window.width = 725
    page.window.height = 735
    drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(
                content=ft.Text("Menu", size=20, weight=ft.FontWeight.BOLD),
                padding=20,
            ),
            ft.Divider(),
            ft.NavigationDrawerDestination(
                icon=ft.icons.HOME,
                label="Início"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.icons.INFO,
                label="Sobre"
            ),
        ]
    )
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Ínicio"),
            ft.NavigationBarDestination(icon=ft.Icons.DOORBELL_OUTLINED, label="Lembretes"),
            ft.NavigationBarDestination(
                icon=ft.Icons.FEATURED_PLAY_LIST,
                selected_icon=ft.Icons.FEATURED_PLAY_LIST,
                label="Projetos",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.SETTINGS,
                selected_icon=ft.Icons.SETTINGS,
                label="Configurações",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON,
                selected_icon=ft.Icons.PERSON,
                label="Perfil",
            ),
        ]
    )
    meu_dia = ft.Text(
        spans=[
            ft.TextSpan(
                "Meu dia",
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
    page.appbar = ft.AppBar(title=ft.Text("Meus compromissos"), leading=ft.IconButton(ft.icons.MENU, on_click=lambda _: drawer.open()))
    page.drawer = drawer
    page.add(meu_dia)
    page.update()



    
    

ft.app(target=main, view=ft.AppView.FLET_APP)
