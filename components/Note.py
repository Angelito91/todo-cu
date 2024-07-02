from flet import *


class Note(Card):
    def __init__(self, note, delete_note):
        super().__init__()

        self.content = Column([
            CupertinoListTile(
                title=Text(note['title'].capitalize(), weight=FontWeight.BOLD),
                subtitle=Text(note['content']),
                additional_info=Text(note['created']),
                leading=self.icon_category(note['category']),
                trailing=Row([
                    Icon(icons.ALARM),
                    IconButton(
                        icons.REMOVE,
                        icon_color='red',
                        on_click=lambda e: delete_note(note)
                    )]),
                # on_click=lambda e: print('ads'),
            )
        ])

    def icon_category(self, category):
        if category == 'Ninguna':
            return Icon(icons.ALL_INCLUSIVE)

        if category == 'Casa':
            return Icon(icons.HOME)

        if category == 'Trabajo':
            return Icon(icons.WORK)

        if category == 'Personal':
            return Icon(icons.PERSON_2)

    def build(self):
        return super().build()
