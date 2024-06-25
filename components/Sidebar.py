from flet import *
from getpass import getuser


def Sidebar(page: Page):

    def close(e):
        page.window.close()

    avatar = CircleAvatar(
        foreground_image_src='https://avatars.githubusercontent.com/u/111069220',
        width=100,
        height=100
    )

    username = Text(
        '👋 ' + getuser().capitalize(),
        size=18,
        weight=FontWeight.BOLD,
    )

    category_button = TextButton(
        text='Categorias',
        icon=icons.LIST
    )

    config_button = TextButton(
        text='Configuracion',
        icon=icons.SETTINGS,
    )

    exit_button = TextButton(
        text='Salir', icon=icons.EXIT_TO_APP, on_click=close)

    return Container(
        ListView([
            Column([
                avatar,
                username,
            ],horizontal_alignment=CrossAxisAlignment.CENTER),
            Divider(color=colors.with_opacity(0.1, colors.WHITE30)),
            Column([
                category_button,
            ]),
            Divider(color=colors.with_opacity(0.1, colors.WHITE30)),
            Column([
                config_button,
                exit_button
            ])
        ]),
        col=3,
        height=page.window.height,
        padding=padding.symmetric(horizontal=5, vertical=8),
        border=border.only(right=border.BorderSide(0.5, colors.WHITE30)),
        bgcolor=colors.with_opacity(0.05, color='red')
    )
