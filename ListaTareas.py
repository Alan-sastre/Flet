from flet import *


def main(page: Page):
    page.title = "Lista de Tareas"
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    texto1 = Text("LISTA DE TAREAS", size=30,
                  color=colors.BLUE_100, text_align=TextAlign.CENTER)

    lista_tareas = Column()  # Aquí se almacenarán las tareas

    def seleccionarTarea(e):
        e.control.text_style = TextStyle(
            decoration=TextDecoration.LINE_THROUGH)
        page.update()

    def añadir(e):
        if campoTarea.value:
            nueva_tarea = ListTile(
                title=Text(campoTarea.value),
                leading=Checkbox(on_change=seleccionarTarea)
            )
            lista_tareas.controls.append(nueva_tarea)
            campoTarea.value = ""  # Limpiar el campo
            page.update()

    campoTarea = TextField(label="Nueva tarea")
    botonAñadir = FilledButton(text="Añadir", on_click=añadir)

    page.add(texto1, campoTarea, botonAñadir, lista_tareas)


app(target=main)
