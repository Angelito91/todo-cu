from flet import *
from .Note import Note


class List(ListView):
    def __init__(self, page: Page, notes: list):
        super().__init__()

        self.page = page
        self.notes = notes

        # self.alignment = MainAxisAlignment.CENTER
        # self.horizontal_alignment = CrossAxisAlignment.END

        self.height = self.page.window.height * 3.8 / 4
        self.width = self.page.window.width * 2.8 / 4

        self.controls = [
            FloatingActionButton(icon=icons.ADD, on_click=self.go_create),
            Text(f'Tu tienes {len(self.notes)} notas')
        ]

    def go_create(self, e):
        self.page.go('/create')

    def delete_note(self, note):
        self.notes.remove(note)
        self.update()

    def before_update(self):
        self.controls.clear()

        self.controls = [
            Text(f'Tu tienes {len(self.notes)} notas')
        ]

        for note in self.notes:
            self.controls.append(Note(note, delete_note=self.delete_note))

        self.controls.append(
            TextButton(
                icon=icons.ADD,
                on_click=self.go_create
            )
        )

        return super().before_update()

    def build(self):
        return super().build()
