'''
    Diana Ximena de León Figueroa
    Carne 18607
    Lab 1 Filling any polygon
    Graficas por Computadora
    21 de julio de 2020
'''

from utils import color, char, word, dword

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)


class Render(object):
    def __init__(self):
        self.framebuffer = []
        self.color = WHITE

    def createWindow(self, width, height):
        self.width = width
        self.height = height

    def point(self, x, y):
        self.framebuffer[y][x] = self.color

    def viewport(self, x, y, width, height):
        self.xViewPort = x
        self.yViewPort = y
        self.viewPortWidth = width
        self.viewPortHeight = height

    def clear(self):
        self.framebuffer = [
            [BLACK for x in range(self.width)]
            for y in range(self.height)
        ]

    def clearColor(self, r, g, b):
        newColor = color(r, g, b)
        self.framebuffer = [
            [newColor for x in range(self.width)]
            for y in range(self.height)
        ]

    def setColor(self, r, g, b):
        self.color = color(r, g, b)

    def getCordX(self, x):
        return round((x+1) * (self.viewPortWidth/2) + self.xViewPort)

    def getCordY(self, y):
        return round((y+1) * (self.viewPortHeight/2) + self.yViewPort)

    def vertex(self, x, y):
        self.point(x, y)

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

    def draw(self, vertex):
        self.puntos = {}
        i = 0
        while i <= (len(vertex) - 2):
            self.line(vertex[i][0], vertex[i][1],
                      vertex[i+1][0], vertex[i+1][1])
            i += 1
        self.line(vertex[i][0], vertex[i][1], vertex[0][0], vertex[0][1])
        self.fill()

    def fill(self):
        for j in self.puntos:
            l = self.puntos.get(j)
            mi = min(l)
            ma = max(l)
            if len(l) > 3:
                pin = True
                for r in range(0, (len(l)-2)):
                    if (l[r]+1) != l[r + 1]:
                        pin = False
                        m1 = l[r]
                        m2 = l[r+1]
                        if m1 != mi and m2 != ma:
                            for i in range(mi, m1):
                                self.point(i, j)
                            for i in range(m2, ma):
                                self.point(i, j)
                if pin:
                    for i in range(mi, ma):
                        self.point(i, j)
            else:
                for i in range(mi, ma):
                    self.point(i, j)

    def write(self, filename='out.bmp'):
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
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()
