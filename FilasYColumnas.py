from flet import *

def main(page: Page):
    page.title = "Filas y Columnas"
    page.window.height = 600
    page.window.width = 1000
    page.bgcolor = ('#110240')
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    titulo1 = Text("FILAS", size = 20)
    titulo2 = Text("COLMUNAS EN FLET ", size = 20)
    titulo1.color = colors.BLUE_100

    def CambioTitulo(e):
        titulo1.value = "Nuevo titulo"
        page.update()
    def CambioTitulo2(e):
        titulo2.value = "Otro nuevo titulo"
        page.update()

    boton = FilledButton(text = "Cambio1", on_click = CambioTitulo)
    botonN = FilledButton(text = "Cambio2", on_click = CambioTitulo2)

    filas = Row(
                controls = [titulo1, titulo2],
                alignment = MainAxisAlignment.CENTER, #Centrar las columnas
                spacing = 80
                )
    filas_Botones = Row(
                controls = [boton, botonN],
                alignment = MainAxisAlignment.CENTER, #Centrar las columnas
                spacing = 80
                )

    ###################################
    #Columnas
    ######################################

    nuevos_textos = [
        Text("python"),
        Text("java"),
        Text("c++"),
        Text("html")
    ]
    Columnas1 = Column(
        controls = [*nuevos_textos],
        alignment = MainAxisAlignment.CENTER, #Centrar las columnas
    )

    nuevos_textos2 = [
        Text("python"),
        Text("java"),
        Text("c++"),
        Text("html")
    ]

    Columnas2 = Column(
        controls = [*nuevos_textos2],
        alignment = MainAxisAlignment.CENTER, #Centrar las columnas
    )

    columnas = Row(
        controls = [Columnas1, Columnas2],
        alignment = MainAxisAlignment.CENTER, #Centrar las columnas
    )

    page.add(filas, filas_Botones, columnas)






app(target = main)