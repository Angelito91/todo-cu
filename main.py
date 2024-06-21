from flet import * 
from components.Sidebar import Sidebar
from components.Forms import Forms

def main(page: Page):
    page.title = "ToDo CU"
    page.adaptive = True
    page.theme = Theme(color_scheme_seed=colors.RED_700)
    page.window.width = 800
    page.window.height = 600
    page.scroll = "always"
    page.padding = 0
    page.spacing = 0

    sidebar = Sidebar(page)
    forms = Forms(page)


    page.add(
        Row([
            sidebar,
            forms
        ])
    )


app(main,assets_dir='./assets')