import flet as ft


def main(page: ft.Page):
    page.title = 'Gerenciador de tarefas'
    page.theme = "light"
    page.update()
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )

    
    

ft.app(target=main)
