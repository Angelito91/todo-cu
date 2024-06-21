import flet as ft

def main(page: ft.Page):
    page.title = "ToDo CU"
    page.adaptive = True
    page.theme = ft.Theme(color_scheme_seed="red")
    page.window.width = 800
    page.window.height = 600
    page.scroll = "always"

    page.add(ft.Text("Hola"))


ft.app(main)