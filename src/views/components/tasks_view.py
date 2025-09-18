import flet as ft

class TaskView(ft.Column):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

        self.checkbox = ft.Checkbox(
            label=self.task_name,
            value=False,
            on_change=self.status_changed,
            expand=True,
        )

        self.delete_btn = ft.IconButton(
            icon=ft.icons.DELETE_OUTLINE,
            icon_color=ft.colors.RED,
            tooltip="Excluir tarefa",
            on_click=self.delete_clicked,
        )

        self.controls = [self.checkbox, self.delete_btn]
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

    def status_changed(self, e):
        self.completed = self.checkbox.value
        if self.completed:
            self.checkbox.label_style = ft.TextStyle(
                decoration=ft.TextDecoration.LINE_THROUGH,
                color=ft.colors.GREY,
            )
        else:
            self.checkbox.label_style = ft.TextStyle(decoration=None, color=None)
        self.task_status_change(self)

    def delete_clicked(self, e):
        self.task_delete(self)
