from flet import *


class Note(Card):
    def __init__(self, note, delete_note):
        super().__init__()
        
        self.content = Column([
            ListTile(
                title=Text(note['title'].capitalize(),weight=FontWeight.BOLD),
                subtitle=Text(note['content']),
                leading=Icon(icons.STAR,color='red'),
            ),
            Row([
                IconButton(
                    icons.CREATE_OUTLINED,
                    icon_color='green',
                ),
                IconButton(
                    icons.DELETE_OUTLINE,
                    icon_color='red',
                    on_click=lambda e: delete_note(note)
                )
            ],alignment=MainAxisAlignment.SPACE_BETWEEN)
        ])

    def build(self):
        return super().build()
