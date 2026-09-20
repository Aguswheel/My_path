from graphics import graphics

def smiley(canvas, x, y, size, color):
    """ 
    Dibuja una cara sonrriente cuando quieras!
    """
    
    canvas.ellipse(x, y, size, size, color)
    
    eye_size = size / 7
    offset = size / 5
    canvas.ellipse(x + offset, y - offset, eye_size, eye_size, "black")
    canvas.ellipse(x - offset, y - offset, eye_size, eye_size, "black")

    canvas.ellipse(x, y+(size/10), (size/2), (size/2), "black")
    canvas.rectangle(x-(size/3), y-(size/4), (size/1.5), (size/3), color)

def main():
    gui = graphics(500, 500, "smiley")
    gui.rectangle(0, 0, 500, 500, "white")
    smiley(gui, 125, 125, 200, "orange")
    smiley(gui, 125, 375, 200, "light green")
    smiley(gui, 375, 125, 200, "light blue")
    smiley(gui, 375, 375, 200, "purple")
    gui.draw()

if __name__ == "__main__":
    main()