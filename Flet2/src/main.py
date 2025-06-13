import flet as ft

def main(page: ft.Page):

    page.theme = ft.Theme(
        text_theme=ft.TextTheme(body_medium=ft.TextStyle(color=ft.Colors.BLUE))
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS),
        ]
    )

    page.add(
        ft.Row(
            controls=[
                ft.Image(
                    src="hokage.jpg",  
                    height=100,
                    width=100,
                ),
                ft.Container(
                    content=ft.Text("Earl James C. Yonson", color="blue"),
                    alignment=ft.alignment.center_left,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")