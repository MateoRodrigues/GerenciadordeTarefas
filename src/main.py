import flet as ft


def main(page: ft.Page):
    page.title = 'Gerenciador de tarefas'
    page.window_height = 400
    page.window_width = 400
    page.window_resizable = False
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
    page.add(ft.Text("Tarefas!"))
    page.update()



    
    

ft.app(target=main, view=ft.AppView.FLET_APP)
