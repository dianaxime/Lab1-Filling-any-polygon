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


    def prueba(self):
        print(self.puntos)
        '''for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.line(x, y, x2, y2)

        for y in range(y0, y2 + 1):
            for x in range(x0, x2 + 1):
                self.line(x, y, x1, y1)

        for y in range(y2, y1 + 1):
            for x in range(x2, x1 + 1):
                self.line(x, y, x0, y0)'''
        
        '''for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.line(y2, x2, y, x)'''

        '''for y in range(y0, y2 + 1):
            for x in range(x0, x2 + 1):
                self.line(y1, x1, y, x)

        for y in range(y2, y1 + 1):
            for x in range(x2, x1 + 1):
                self.line(y0, x0, y, x)'''

        for j in self.puntos:
            mi = min(self.puntos.get(j))
            ma = max(self.puntos.get(j))
            for i in range(mi, ma):
                #print(i, j)
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

bitmap.glCreateWindow(500, 500)
bitmap.glClearColor(0.45, 0.06, 0.87)
#bitmap.glViewport(25, 25, 400, 300)
#bitmap.glColor(1, 0.28, 0)
#bitmap.glPoint(-0.5, 1)
bitmap.glColor(0.2, 0.70, 0.36)

# aca abajo prueba
#bitmap.prueba(180, 330, 207, 345, 233, 330)
'''
PINTA AFUERA
bitmap.prueba(205, 410, 193, 383, 165, 380)
bitmap.prueba(233, 330, 230, 360, 250, 380)
bitmap.prueba(180, 330, 207, 345, 233, 330)
bitmap.prueba(165, 380, 185, 360, 180, 330)
'''
'''
PINTA DENTRO
bitmap.prueba(207, 345, 233, 330, 230, 360)
'''

'''
NO SIRVEN
bitmap.prueba(185, 360, 180, 330, 180, 330)
bitmap.prueba(250, 380, 220, 385, 205, 410)
'''

# Aca nueva idea
bitmap.line(165, 380, 185, 360)
bitmap.line(185, 360, 180, 330)
bitmap.line(180, 330, 207, 345)
#bitmap.prueba()
#bitmap.puntos = {}
bitmap.line(207, 345, 233, 330)
bitmap.line(233, 330, 230, 360)
bitmap.line(230, 360, 250, 380)
#bitmap.prueba()
#bitmap.puntos = {}
bitmap.line(250, 380, 220, 385)
bitmap.line(220, 385, 205, 410)
bitmap.line(205, 410, 193, 383)
#bitmap.prueba()
#bitmap.puntos = {}
bitmap.line(193, 383, 165, 380)
bitmap.prueba()
# linea diagonal
#bitmap.glLine(-0.75, -1, 0.25, 1)
# linea horizontal
#bitmap.glLine(0.25, -1, 0.25, 1)
# linea vertical
#bitmap.glLine(-0.75, -1, 0.25, -1)
bitmap.glFinish()
