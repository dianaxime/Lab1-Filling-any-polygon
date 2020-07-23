'''
    Diana Ximena de León Figueroa
    Carne 18607
    Lab 1 Filling any polygon
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
