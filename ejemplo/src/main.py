import flet as ft


def main(page: ft.Page):
    page.title = 'Titulo 1 '
    texto = ft.Text("Hello world")
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def cambiarTexto(e):
        texto.value = "Hello world 2"
        page.update()

    boton = ft.FilledButton(text = "Boton", on_click = cambiarTexto)
    page.add(texto,boton)

ft.app(target = main)