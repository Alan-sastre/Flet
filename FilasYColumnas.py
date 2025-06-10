from flet import *

def main(page: Page):
    page.title = "Filas y Columnas"
    page.window.height = 600
    page.window.width = 600
    page.bgcolor = ('#110240')
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    titulo1 = Text("FILAS Y COLMUNAS EN FLET ", size = 20)
    titulo1.color = colors.BLUE_100


    page.add(titulo1)

app(target = main)