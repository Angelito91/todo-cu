from flet import *
from datetime import date
from uuid import uuid4


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

        self.category = Dropdown(
            label='Categorías',
            width=self.page.window.width * 2.86 / 4,
            border=InputBorder.NONE,
            fill_color=colors.with_opacity(0.05, 'white'),
            value='Ninguna',
            options=[
                dropdown.Option('Ninguna'),
                dropdown.Option('Casa'),
                dropdown.Option('Trabajo'),
                dropdown.Option('Personal'),
            ]
        )

        self.button_add = ElevatedButton(
            text='Guardar',
            icon=icons.ADD,
            color=colors.GREEN_ACCENT,
            width=self.page.window.width * 1.50 / 4,
            height=40,
            on_click=self.add_notes
        )

        self.button_edit = ElevatedButton(
            text='Guardar los cambios',
            icon=icons.ADD,
            color=colors.GREEN_ACCENT,
            width=self.page.window.width * 1.50 / 4,
            height=40,
            on_click=self.edit_note
        )

        self.button_cancel = ElevatedButton(
            text='Descartar',
            icon=icons.CANCEL,
            width=self.page.window.width * 1.25 / 4,
            height=40,
            on_click=self.cancel
        )

    def add_notes(self, e):
        if not len(self.title.value.strip()) > 0:
            self.title.error_text = 'No haz escrito nada'
            self.title.update()
            return

        if not len(self.content.value.strip()) > 0:
            self.content.error_text = 'No haz escrito nada'
            self.content.update()
            return

        self.notes.append({
            'id': uuid4(),
            'title': self.title.value,
            'content': self.content.value,
            'category': self.category.value,
            'created': date.today().strftime('%d de %b de %Y')
        })

        self.title.value = ''
        self.content.value = ''
        self.category.value = 'Ninguna'
        self.update()

    def edit_note(self, e):
        if not len(self.title.value.strip()) > 0:
            self.title.error_text = 'No haz escrito nada'
            self.title.update()
            return

        if not len(self.content.value.strip()) > 0:
            self.content.error_text = 'No haz escrito nada'
            self.content.update()
            return

        troute = TemplateRoute(self.page.route)

        if troute.match('/edit/:id'):
            for index, note in enumerate(self.notes):
                if str(note['id']) == troute.id:
                    self.notes[index] = {
                        'id': self.notes[index]['id'],
                        'title': self.title.value,
                        'content': self.content.value,
                        'category': self.category.value,
                        'created': self.notes[index]['created']
                    }

            self.title.value = ''
            self.content.value = ''
            self.category.value = 'Ninguna'
            self.page.go('/')

    def cancel(self, e):
        self.page.go('/')

    def before_update(self):
        troute = TemplateRoute(self.page.route)

        if troute.match('/edit/:id'):
            for note in self.notes:
                if str(note['id']) == troute.id:
                    self.title.value = note['title']
                    self.content.value = note['content']
                    self.category.value = note['category']

            self.controls = [
                Text(
                    "En que piensas 🧠?",
                    text_align=TextAlign.CENTER,
                    size=20,
                    weight=FontWeight.BOLD,
                    font_family='monospace'),
                self.title,
                self.content,
                self.category,
                Row([
                    self.button_edit,
                    self.button_cancel
                ])
            ]

        else:
            self.controls = [
                Text(
                    "En que piensas 🧠?",
                    text_align=TextAlign.CENTER,
                    size=20,
                    weight=FontWeight.BOLD,
                    font_family='monospace'),
                self.title,
                self.content,
                self.category,
                Row([
                    self.button_add,
                    self.button_cancel
                ])
            ]

        return super().before_update()

    def build(self):
        return super().build()
