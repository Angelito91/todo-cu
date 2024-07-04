from flet import *
from .Note import Note


class List(Column):
    def __init__(self, page: Page, notes: list):
        super().__init__()

        self.page = page
        self.notes = notes
        self.category = ['Ninguna', 'Casa', 'Trabajo', 'Personal']

        self.scroll = ScrollMode.ADAPTIVE
        self.height = self.page.window.height * 3.8 / 4
        self.width = self.page.window.width * 2.8 / 4

        self.select_category = CupertinoSlidingSegmentedButton(
            selected_index=0,
            on_change=self.change_category,
            controls=[
                Icon(icons.ALL_INCLUSIVE),
                Icon(icons.HOME),
                Icon(icons.WORK),
                Icon(icons.PERSON_2)
            ]
        )

        self.controls = [
            Row([
                IconButton(
                    icon=icons.ADD,
                    on_click=lambda e: self.page.go('/create'),
                ),
                self.select_category
            ]),
            Text(f'Tu tienes {len(self.notes)} notas'),
        ]

    def change_category(self, e):
        option = int(e.data)

        if option == 0:
            self.category = ['Ninguna', 'Casa', 'Trabajo', 'Personal']

        if option == 1:
            self.category = ['Casa']

        if option == 2:
            self.category = ['Trabajo']

        if option == 3:
            self.category = ['Personal']

        self.update()

    def delete_note(self, note):
        self.notes.remove(note)
        self.update()

    def before_update(self):
        del self.controls[2:]

        for note in self.notes:
            if note['category'] in self.category:
                self.controls.append(Note(note, delete_note=self.delete_note))

        return super().before_update()

    def build(self):
        return super().build()
