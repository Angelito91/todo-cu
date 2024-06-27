from flet import *

class List(Column):
    def __init__(self,page: Page):
        super().__init__()

        self.page = page

        self.height = self.page.window.height * 3.8 / 4
        self.width = self.page.window.width * 3 / 4

        self.controls = [
            TextButton('crear',on_click=self.go_create)
        ]
    
    def go_create(self,e):
        self.page.go('/create')

    def before_update(self):
        if self.page.client_storage.contains_key('notes'):
            notes = self.page.client_storage.get('notes')
            for note in notes:
                self.controls.append(
                    Row([
                        Checkbox(note['title']),
                        IconButton(icons.CREATE_OUTLINED),
                        IconButton(icons.DELETE_OUTLINE),
                    ])
                )

        return super().before_update()   
    

    def build(self):
        return super().build()