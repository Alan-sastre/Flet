from flet import *

def main(page: Page):
    page.title = "Este es otra pruebla con flet"
    titulo = Text ("Mi Nombres es ")
    texto = Text ("0")
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.window.height = 400
    page.window.width = 400
    page.bgcolor = Colors.BLUE_100

    def CanmbioNombre(e):
        titulo.value = "Mi Nombres es Alan"
        page.update()

    def SumaNumero(e):
        texto.value = int(texto.value) + 1
        page.update()
    def RestaNumero(e):
        texto.value = int(texto.value) - 1
        page.update()

    botonN = FilledButton(text = "Cambia Nombre", on_click = CanmbioNombre)
    botonS = FilledButton(text = "Suma", on_click = SumaNumero)
    botonR = FilledButton(text = "Resta", on_click = RestaNumero)

    page.add(texto, titulo, botonS, botonR, botonN)

app(target = main)