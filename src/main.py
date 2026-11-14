import flet as ft


def main(page: ft.Page):
    page.appbar = ft.AppBar(
    leading=ft.Icon(ft.Icons.MENU),
    title=ft.Text("Dashboard"),
    bgcolor=ft.Colors.SURFACE_CONTAINER,
    actions=[
        ft.IconButton(ft.Icons.SEARCH),
        ft.IconButton(ft.Icons.MORE_VERT),
    ],
)
    page.add(ft.SafeArea(content=ft.Column(controls=[ft.Text("Body!")])))


if __name__ == "__main__":
    ft.run(main)
