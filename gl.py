'''
    Diana Ximena de León Figueroa
    Carne 18607
    Lab1
    Graficas por Computadora
    21 de julio de 2020
'''

import struct


def char(c):
    return struct.pack('=c', c.encode('ascii'))


def word(c):
    return struct.pack('=h', c)


def dword(c):
    return struct.pack('=l', c)


def color(r, g, b):
    return bytes([b, g, r])


class Render(object):
    def __init__(self):
        self.framebuffer = []
        self.puntos = {}

    def point(self, x, y):
        self.framebuffer[y][x] = self.color

    def glInit(self):
        pass

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height

    def glViewport(self, x, y, width, height):
        self.xViewPort = x
        self.yViewPort = y
        self.viewPortWidth = width
        self.viewPortHeight = height

    def glClear(self):
        self.framebuffer = [
            [color(0, 0, 0) for x in range(self.width)]
            for y in range(self.height)
        ]

    def glClearColor(self, r=1, g=1, b=1):
        r = round(r*255)
        g = round(g*255)
        b = round(b*255)

        self.framebuffer = [
            [color(r, g, b) for x in range(self.width)]
            for y in range(self.height)
        ]

    def glColor(self, r=0.5, g=0.5, b=0.5):
        r = round(r*255)
        g = round(g*255)
        b = round(b*255)
        self.color = color(r, g, b)

    def glCordX(self, x):
        return round((x+1)*(self.viewPortWidth/2)+self.xViewPort)

    def glCordY(self, y):
        return round((y+1)*(self.viewPortHeight/2)+self.yViewPort)

    def glVertex(self, x, y):
        X = self.glCordX(x)
        Y = self.glCordY(y)
        self.point(X, Y)

    def glPoint(self, x, y):
        X = self.glCordX(x)
        Y = self.glCordY(y)
        self.point(X, Y)

    def glLine(self, x0, y0, x1, y1):
        '''
        x0 = self.glCordX(x0)
        y0 = self.glCordY(y0)
        x1 = self.glCordX(x1)
        y1 = self.glCordY(y1)
        '''
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        threshold = dx
        y = y0
        inc = 1 if y1 > y0 else -1
        for x in range(x0, x1):
            if steep:
                self.point(y, x)
            else:
                self.point(x, y)

            offset += 2 * dy
            if offset >= threshold:
                y += inc
                threshold += 2 * dx

    def line(self, x0, y0, x1, y1):
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        threshold = dx
        y = y0
        inc = 1 if y1 > y0 else -1
        for x in range(x0, x1):
            if steep:
                self.point(y, x)
                if self.puntos.get(x) == None:
                    self.puntos[x] = []
                
                self.puntos[x] += [y]
            else:
                self.point(x, y)
                if self.puntos.get(y) == None:
                    self.puntos[y] = []
                
                self.puntos[y] += [x]


            offset += 2 * dy
            if offset >= threshold:
                y += inc
                threshold += 2 * dx


    def prueba(self, vertex):
        self.puntos = {}
        i = 0
        while i <= (len(vertex) - 2):
            self.line(vertex[i][0], vertex[i][1], vertex[i+1][0], vertex[i+1][1])
            i += 1
        self.line(vertex[i][0], vertex[i][1], vertex[0][0], vertex[0][1])
        self.relleno()
        
    def relleno(self):
        print(self.puntos)
        for j in self.puntos:
            mi = min(self.puntos.get(j))
            ma = max(self.puntos.get(j))
            for i in range(mi, ma):
                self.point(i, j)
        
    def glFinish(self, filename='out.bmp'):
        f = open(filename, 'bw')

        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # image header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        for x in range(self.width):
            for y in range(self.height):
                f.write(self.framebuffer[y][x])

        f.close()


bitmap = Render()
bitmap.glCreateWindow(800, 800)
bitmap.glClearColor(0.45, 0.06, 0.87)
bitmap.glColor(0.2, 0.70, 0.36)
vertex = [(321, 335), (288, 286), (339, 251), (374, 302)]
vertex = [(377, 249), (411, 197), (436, 249)]
vertex = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
(750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
(597, 215), (552, 214), (517, 144), (466, 180)]
vertex = [(682, 175), (708, 120), (735, 148), (739, 170)]
vertex = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]
bitmap.prueba(vertex)
bitmap.glFinish()
