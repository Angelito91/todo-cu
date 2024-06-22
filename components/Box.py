from flet import *
from .Forms import Forms

def Box(page: Page):
    forms = Forms(page)
    
    return GridView(
        controls=[
           forms
        ],
        height=page.window.height,
        width=page.window.width * 3 / 4,
    )