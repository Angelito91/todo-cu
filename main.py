from flet import * 

def main(page: Page):
    page.title = "ToDo CU"
    page.adaptive = True
    page.theme = Theme(color_scheme_seed=colors.RED_700)
    page.window.width = 800
    page.window.height = 600
    page.scroll = "always"
    page.padding = 0
    page.spacing = 0

    sidebar = Container(
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

    titlebox = TextField(
        label='Titulo',
        hint_text="Escriba un titulo... Ej: Primera nota",
        prefix_icon= icons.ADD_TASK,
        width=page.window.width * 2.86 / 4,
        border=InputBorder.NONE,
        fill_color=colors.with_opacity(0.05,'white'),
        filled=True,
        autocorrect=True,
        autofocus=True)
    
    contentbox = TextField(
        label='Contenido',
        hint_text="Escriba de que trata la nota..",
        prefix_icon= icons.BOOKMARKS_SHARP,
        width=page.window.width * 2.86 / 4,
        border=InputBorder.NONE,
        fill_color=colors.with_opacity(0.05,'white'),
        filled=True,
        multiline=True,
        autocorrect=True,
        min_lines=4,
        max_lines=6,
        max_length=200)
    
    button_add = ElevatedButton(
        text='Guardar',
        icon=icons.ADD,
        color=colors.GREEN_ACCENT,
        width=page.window.width * 1.50 / 4,
        height=40
        )

    button_cancel = ElevatedButton(
        text='Guardar',
        icon=icons.CANCEL,
        color=colors.RED,
        width=page.window.width * 1.25 / 4,
        height=40
        )

    content = Container(
        content=Column([
            Text(
                "En que piensas 🧠?",
                text_align= TextAlign.CENTER,
                size=20,
                weight=FontWeight.BOLD,
                font_family='monospace'),
            titlebox,
            contentbox,
            Row([
                button_add,
                button_cancel
            ])
        ]),
        height=page.window.height,
        width=page.window.width * 3 / 4,
        padding=padding.all(5),
    )

    layout = Row([
        sidebar,
        content,
    ])
    page.add(layout)


app(main,assets_dir='./assets')