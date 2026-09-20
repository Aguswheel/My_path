image = open("chessboard.ppm", "w")
image.write("P3\n800 800\n255\n")
for row in range(800):
    for col in range(800):
        if col % 200 > 100 and row % 200 > 100:
            image.write(" 220 190 150 ")
        elif col % 200 < 100 and row % 200 < 100:
            image.write(" 220 190 150 ")
        else: 
            image.write(" 100 70 40 ")
    image.write("\n")
image.close()            