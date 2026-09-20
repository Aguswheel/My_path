from PIL import Image
image = open("test_image.ppm", "w")
# write the first three lines of content for a 256 x 256 image
image.write("P3\n256 256\n255\n")
# put the pixels in for a black-to-white gradient
for i in range(256):
    # create one pixel, using the value of the i variable to determine what shade of grey to make the line
    one_pixel = str(i) + " " + str(i) + " " + str(i) + " "
    # repeat the pixel 256 times (for the entire row) and then write the row to the file
    image.write(one_pixel * 256 + "\n")
image.show()
image.close()
