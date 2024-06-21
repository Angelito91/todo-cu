from flet import *

def Sidebar(page: Page):
    
    category_button = TextButton(text = 'Categorias', icon = icons.LIST)
    config_button = TextButton(text = 'Configuracion', icon = icons.SETTINGS)
    
    def close(e):
        page.window.close()
        
    exit_button = TextButton(text = 'Salir', icon = icons.EXIT_TO_APP, on_click = close)
    return Container(
        content=Column(controls=[
            category_button,
            config_button,
            exit_button
            ]),
        height=page.window.height,
        width=page.window.width * 1 / 4,
        padding=padding.all(5),
        border=border.only(right=border.BorderSide(0.5,colors.WHITE30)),
        bgcolor=colors.with_opacity(0.08,color='red')
        )

