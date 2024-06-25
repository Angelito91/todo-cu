from flet import *

def Forms(page: Page):

    def cancel(e):
        title.value = ''
        content.value = ''
        page.update()
        
    title = TextField(
        label='Titulo',
        hint_text="Escriba un titulo... Ej: Primera nota",
        prefix_icon= icons.ADD_TASK,
        width=page.window.width * 2.86 / 4,
        border=InputBorder.NONE,
        fill_color=colors.with_opacity(0.05,'white'),
        filled=True,
        autocorrect=True,
        autofocus=True
    )
    
    content = TextField(
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
        max_length=200
    )
    
    button_add = ElevatedButton(
        text='Guardar',
        icon=icons.ADD,
        color=colors.GREEN_ACCENT,
        width=page.window.width * 1.50 / 4,
        height=40
    )


    button_cancel = ElevatedButton(
        text='Descartar',
        icon=icons.CANCEL,
        color=colors.RED,
        width=page.window.width * 1.25 / 4,
        height=40,
        on_click = cancel
    )

    return Column([
        Text(
            "En que piensas 🧠?",
            text_align= TextAlign.CENTER,
            size=20,
            weight=FontWeight.BOLD,
            font_family='monospace'),
        title,
        content,
        Row([
            button_add,
            button_cancel
        ])
    ],
    col=9,
    height=page.window.height,
    width=page.window.width * 3 / 4,
    )