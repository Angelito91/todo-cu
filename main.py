import flet as ft

def main(page: ft.Page):
    page.title = "ToDo CU"
    page.adaptive = True
    page.theme = ft.Theme(color_scheme_seed="red")
    page.window.width = 800
    page.window.height = 600
    page.scroll = "always"
    page.padding = 0
    page.spacing = 0

    sidebar = ft.Container(
        content=ft.Column([
            ft.Text(
                "Hola, como estas?",
                text_align= ft.TextAlign.CENTER,
                size=20,
                weight=ft.FontWeight.BOLD,
                font_family='monospace',
                italic=True)
        ]),
        height=page.window.height,
        width=page.window.width * 1 / 4,
        padding=ft.padding.all(5),
        border=ft.border.only(right=ft.border.BorderSide(0.1,ft.colors.WHITE30)),
        )

    titlebox = ft.TextField(
        label='Titulo',
        hint_text="Escriba un titulo.. Ej: Primera nota",
        prefix_icon= ft.icons.ADD_TASK,
        width=page.window.width * 2.86 / 4,
        border=ft.InputBorder.NONE,
        fill_color=ft.colors.with_opacity(0.05,'white'),
        filled=True,
        autocorrect=True,
        autofocus=True)
    
    contentbox = ft.TextField(
        label='Contenido',
        hint_text="Escriba de que trata la nota..",
        prefix_icon= ft.icons.BOOKMARKS_SHARP,
        width=page.window.width * 2.86 / 4,
        border=ft.InputBorder.NONE,
        fill_color=ft.colors.with_opacity(0.05,'white'),
        filled=True,
        multiline=True,
        autocorrect=True,
        min_lines=3,
        max_lines=5,
        max_length=200)


    content = ft.Container(
        content=ft.Column([
            ft.Text(
                "En que piensas 🧠?",
                text_align= ft.TextAlign.CENTER,
                size=20,
                weight=ft.FontWeight.BOLD,
                font_family='monospace'),
            titlebox,
            contentbox
        ]),
        height=page.window.height,
        width=page.window.width * 3 / 4,
        padding=ft.padding.all(5),
    )

    layout = ft.Row([
        sidebar,
        content
    ])
    page.add(layout)


ft.app(main,assets_dir='./assets')