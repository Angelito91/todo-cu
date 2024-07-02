from flet import *


class Forms(Column):
    def __init__(self, page, notes):
        super().__init__()

        self.page = page
        self.notes = notes

        self.height = self.page.window.height * 3.8 / 4
        self.width = self.page.window.width * 3 / 4

        self.title = TextField(
            label='Titulo',
            hint_text="Escriba un titulo... Ej: Primera nota",
            prefix_icon=icons.ADD_TASK,
            width=self.page.window.width * 2.86 / 4,
            border=InputBorder.NONE,
            fill_color=colors.with_opacity(0.05, 'white'),
            filled=True,
            autocorrect=True,
            autofocus=True,
            max_length=50
        )

        self.content = TextField(
            label='Contenido',
            hint_text="Escriba de que trata la nota..",
            prefix_icon=icons.BOOKMARKS_SHARP,
            width=self.page.window.width * 2.86 / 4,
            border=InputBorder.NONE,
            fill_color=colors.with_opacity(0.05, 'white'),
            filled=True,
            multiline=True,
            autocorrect=True,
            min_lines=4,
            max_lines=6,
            max_length=200
        )

        self.button_add = ElevatedButton(
            text='Guardar',
            icon=icons.ADD,
            color=colors.GREEN_ACCENT,
            width=self.page.window.width * 1.50 / 4,
            height=40,
            on_click=self.add_notes
        )

        self.button_cancel = ElevatedButton(
            text='Descartar',
            icon=icons.CANCEL,
            width=self.page.window.width * 1.25 / 4,
            height=40,
            on_click=self.cancel
        )

        self.controls = [
            Text(
                "En que piensas 🧠?",
                text_align=TextAlign.CENTER,
                size=20,
                weight=FontWeight.BOLD,
                font_family='monospace'),
            self.title,
            self.content,
            Row([
                self.button_add,
                self.button_cancel
            ])
        ]

    def add_notes(self, e):
        if not len(self.title.value.strip()) > 0:
            self.title.error_text = 'No haz escrito nada'
            self.title.update()
            return

        if not len(self.content.value.strip()) > 0:
            self.content.error_text = 'No haz escrito nada'
            self.content.update()
            return

        self.notes.append({'title': self.title.value,
                          'content': self.content.value})
        self.title.value = ''
        self.content.value = ''
        self.update()

    def cancel(self, e):
        self.page.go('/')

    def build(self):
        return super().build()
