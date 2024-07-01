from flet import *


class Note(Row):
    def __init__(self, note, delete_note):
        super().__init__()

        self.controls = [
            Checkbox(note['title']),
            IconButton(
                icons.CREATE_OUTLINED,
                icon_color='green',
            ),
            IconButton(
                icons.DELETE_OUTLINE,
                icon_color='red',
                on_click=lambda e: delete_note(note)
            )
        ]

    def build(self):
        return super().build()
