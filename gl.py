'''
    Diana Ximena de León Figueroa
    Carne 18607
    Lab 1 Filling any polygon
    Graficas por Computadora
    21 de julio de 2020
'''

from lib import Render

bitmap = Render()


def glInit(self):
    pass


def glCreateWindow(width, height):
    bitmap.createWindow(width, height)


def glViewport(x, y, width, height):
    bitmap.viewport(x, y, width, height)


def glClear():
    bitmap.clear()


def glClearColor(r, g, b):
    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)
    bitmap.clearColor(r, g, b)


def glColor(r, g, b):
    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)
    bitmap.setColor(r, g, b)


def glVertex(x, y):
    X = bitmap.getCordX(x)
    Y = bitmap.getCordY(y)
    bitmap.vertex(X, Y)


def glPoint(x, y):
    X = bitmap.getCordX(x)
    Y = bitmap.getCordY(y)
    bitmap.point(X, Y)


def glLine(x0, y0, x1, y1):
    x0 = bitmap.getCordX(x0)
    y0 = bitmap.getCordY(y0)
    x1 = bitmap.getCordX(x1)
    y1 = bitmap.getCordY(y1)
    bitmap.line(x0, y0, x1, y1)


def glDraw(cord):
    bitmap.draw(cord)


def glFinish(filename='out.bmp'):
    bitmap.write(filename)


glCreateWindow(800, 800)
glClearColor(0.45, 0.06, 0.87)

# Poligono 1
glColor(0.2, 0.70, 0.36)
cord = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330),
        (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]
glDraw(cord)

# Poligono 2
glColor(0.75, 0.75, 0.75)
cord = [(321, 335), (288, 286), (339, 251), (374, 302)]
glDraw(cord)

# Poligono 3
glColor(0.2, 0.2, 0.2)
cord = [(377, 249), (411, 197), (436, 249)]
glDraw(cord)

# Poligono 4
glColor(0.9, 0.9, 0.9)
cord = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179),
        (672, 192), (659, 214), (615, 214), (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180)]
glDraw(cord)

# Poligono 5
glColor(0.5, 0.5, 0.5)
''' Sumar 100 porque quedaba debajo de otra figura '''
cord = [(682, 175 + 100), (708, 120 + 100), (735, 148 + 100), (739, 170 + 100)]
glDraw(cord)

glFinish()
