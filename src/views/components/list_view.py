import flet as ft
from ..components.tasks_view import TaskView


class ListView(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(
            hint_text="Adicionar uma tarefa",
            on_submit=self.add_task,
            expand=True,
        )
        self.tasks_column = ft.Column(spacing=5, scroll="auto")

        add_button = ft.IconButton(
            icon=ft.icons.ADD_CIRCLE,
            icon_color=ft.colors.BLUE,
            tooltip="Adicionar tarefa",
            on_click=self.add_task,
        )

        self.controls = [
            ft.Row([self.new_task, add_button]),
            ft.Divider(),
            self.tasks_column,
        ]

    def add_task(self, e):
        if self.new_task.value.strip():
            task = TaskView(self.new_task.value, self.task_status_change, self.task_delete)
            self.tasks_column.controls.append(task)
            self.new_task.value = ""
            self.new_task.focus()
            self.update()

    def task_status_change(self, task):
        self.update()

    def task_delete(self, task):
        self.tasks_column.controls.remove(task)
        self.update()


