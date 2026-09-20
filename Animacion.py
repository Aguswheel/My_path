from graphics import graphics

def main():
    canvas = graphics(500, 350, "ball drop")

    coord = -100
    while True:
        canvas.clear()
        canvas.rectangle(0, 0, 500, 350, "orange")
        canvas.ellipse(250, coord, 75, 75, "gray")
        canvas.ellipse(coord, 175, 75, 75, "blue")
        
        coord += 4

        # Reiniciamos la coordenada si sale de los límites del canvas (500)
        if coord > 500:
            coord = -100
            
        canvas.update_frame(1000) # jugando aca con el numero q le pase como argumento las pelotas 
                                  # van a ir mas lento o mas rapido... yeah!

main()