import flet as ft

def main(page: ft.Page):
    page.title = "App"
 
    page.add(ft.Text("Hola"))


ft.app(main)