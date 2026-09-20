from graphics import graphics

def plus(canvas, x, y, w, h, color, thickness):
    """
    Esta funcion dibuja un signo de + centrado en x, y.
    Informacion de los Parametros:
        * canvas: El objeto grafico en el q vamos a dibujar el signo mas.
        * x and y: Las coordenadas para el centro del signo.
        * w and h: Width & Height.
        * color: El color del relleno.
        * thickness: El grosor del signo.
    """

    canvas.line(x-(w/2), y, x+(w/2), y, color, thickness)
    canvas.line(x, y-(h/2), x, y+(h/2), color, thickness)

def main():
    gui = graphics(500, 500, "plusses")
    gui.rectangle(0, 0, 500, 500, "white")
    plus(gui, 250, 250, 400, 400, "green", 50)
    plus(gui, 100, 100, 50, 50, "red", 10)
    gui.draw()

main()