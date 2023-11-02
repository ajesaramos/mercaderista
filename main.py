# imports
import imutils
import cv2

"""
cargar la imagen y mostrar sus dimensiones
las imagenes se representan como arrays Numpy multidimensionales
con filas, columnas y profundidad (numero de canales en este caso bgr)
"""
image = cv2.imread("fechas/fecha1.jpg")
h, w, c = image.shape
print("width= {}, height={}, channels={}.".format(w, h, c))

## nuevas dimensiones
w = 800
h = 600

## aplicar dimensiones
image_res = cv2.resize(image, (w, h))

# mouse tracking & position display
def get_cursor_position(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"Cursor position: x={x}, y={y}")

cv2.namedWindow('Mercaderista')
cv2.setMouseCallback('Mercaderista', get_cursor_position)

# acceder el pixel RGB localizado en x50 y y100
# recordar que OpenCV almacena los pixeles en BGR
B, G, R = image[100, 50]
print(f"B{B}, G{G}, R{R}")

# Extraer ROI's es un paso importante en el procesado de imagenes
# Array slicing permite extraer los cuadros de un ROI a mano
roi = image_res[207:445, 59:736] #esto debe especificarse siempre tal que el delta de posiciones sea >0
cv2.imshow('Mercaderista', roi)
cv2.waitKey(0)

# mostrar imagen y esperar cualquier tecla para cerrar
cv2.imshow("Mercaderista", image_res)
cv2.waitKey(0)