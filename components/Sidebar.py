from flet import *

def Sidebar(page: Page):
    category_button = TextButton(text = 'Categorias', icon = icons.LIST)
    config_button = TextButton(text = 'Configuracion', icon = icons.SETTINGS)
    exit_button = TextButton(text = 'Salir', icon = icons.EXIT_TO_APP)
    return Container(
        content=Column(controls=[
            category_button,
            config_button,
            exit_button
            ]),
        height=page.window.height,
        width=page.window.width * 1 / 4,
        padding=padding.all(5),
        border=border.only(right=border.BorderSide(0.1,colors.WHITE30)),
        )

