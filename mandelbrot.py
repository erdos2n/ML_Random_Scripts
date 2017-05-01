from PIL import Image

max_iteration = 200
x_center = -1.0
y_center =  0.0
size = 500

im = Image.new("RGB", (size,size))
for i in range(size):
    for j in range(size):
        x , y = ( x_center + 4.0 * float(i-size/2)/size,
                  y_center + 4.0 * float(j-size/2)/size
                )

        a,b = (0.0, 0.0)
        iteration = 0

        while (a**2 + b**2 <= 4.0 and iteration < max_iteration):
            a,b = a**2 - b**2 + x, 2*a*b + y
            iteration += 1
        if iteration == max_iteration:
            color_value = 255
            im.putpixel
        else:
            color_value = iteration*15 % 255
        im.putpixel( (i,j), (color_value, 2*color_value, 3*color_value))

im.save("mandelbrot.png", "PNG")
im.show()