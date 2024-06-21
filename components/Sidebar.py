from flet import *

def Sidebar(page: Page):
    return Container(
        content=Column([
            Text(
                "Hola, como estas?",
                text_align= TextAlign.CENTER,
                size=20,
                weight=FontWeight.BOLD,
                font_family='monospace',
                italic=True)
        ]),
        height=page.window.height,
        width=page.window.width * 1 / 4,
        padding=padding.all(5),
        border=border.only(right=border.BorderSide(0.1,colors.WHITE30)),
        )

