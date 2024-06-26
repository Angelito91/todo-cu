from flet import *
from getpass import getuser


class Sidebar(Container):
    def __init__(self, page: Page):
        super().__init__()

        self.page = page

        self.height = self.page.window.height * 3.8 / 4 
        self.width = self.page.window.width * 1 / 4
        self.padding = padding.symmetric(horizontal=5, vertical=8)
        self.border_radius = border_radius.all(20)
        self.bgcolor = colors.with_opacity(0.05, color='red')

        self.avatar = CircleAvatar(
            foreground_image_src='https://avatars.githubusercontent.com/u/111069220',
            width=100,
            height=100
        )

        self.username = Text(
            getuser().capitalize() + ' 👋',
            size=18,
            weight=FontWeight.BOLD,
            font_family='helvetica'
        )

        self.category_button = TextButton(
            text='Categorias',
            icon=icons.LIST
        )

        self.config_button = TextButton(
            text='Configuracion',
            icon=icons.SETTINGS,
        )

        self.exit_button = TextButton(
            text='Salir', icon=icons.EXIT_TO_APP, on_click=self.close)

        self.content = ListView([
            Column([
                self.avatar,
                self.username,
            ], horizontal_alignment=CrossAxisAlignment.CENTER),
            Divider(color=colors.with_opacity(0.1, colors.WHITE30)),
            Column([
                self.category_button,
            ],height=self.height * 2 / 4),
            Divider(color=colors.with_opacity(0.1, colors.WHITE30)),
            Column([
                self.config_button,
                self.exit_button
            ])
        ])

    def close(self, e):
        self.page.window.close()

    def build(self):
        return super().build()
