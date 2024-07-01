from flet import *
from components.Sidebar import Sidebar
from components.Forms import Forms
from components.List import List

from getpass import getuser


def main(page: Page):
    page.title = f"💻 ToDo CU🇨🇺 - {getuser()}"
    page.adaptive = True
    page.theme = Theme(color_scheme_seed=colors.RED_700)

    page.window.width = 800
    page.window.min_width = 800
    page.window.max_width = 800

    page.window.height = 600
    page.window.min_height = 600
    page.window.max_height = 600

    page.scroll = ScrollMode.ADAPTIVE
    page.padding = 10

    def window_event(e):
        if e.data == 'close':
            page.client_storage.set('notes', notes)
            page.window.destroy()

    page.window.prevent_close = True
    page.on_window_event = window_event

    if page.client_storage.contains_key('notes'):
        notes = page.client_storage.get('notes')
    else:
        notes = []

    sidebar = Sidebar(page)
    forms = Forms(page, notes)
    list = List(page, notes)

    def route_change(route):
        page.clean()

        if page.route == '/':
            page.add(
                Row([
                    sidebar,
                    list
                ])
            )

        if page.route == '/create':
            page.add(
                Row([
                    sidebar,
                    forms
                ])
            )

        page.update()

    page.on_route_change = route_change
    page.go('/')


app(main, assets_dir='./assets')
