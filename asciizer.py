import sys, getopt
import Image

chars = " .-*O#"[::-1]
im = Image.open('c:\\Users\\anon\\Downloads\\IMAG0801-1-1.jpg')

def get_pixel(img, coords):
   return img.convert('RGB').getpixel(coords)

def run(char_x, char_y):
   incx = 0 if im.size[0] % char_x == 0 else 1
   incy = 0 if im.size[1] % char_y == 0 else 1
   ar = [[0 for i in range(im.size[0]/char_x + incx)] for j in range(im.size[1]/char_y + incy)]
   #ar = [[0] *(im.size[0]/char_x + 1)] * (im.size[1]/char_y + 1)

   for j in range(im.size[1]):
      for i in range(im.size[0]):

         ar[j / char_y][i / char_x] += sum(get_pixel(im, (i,j)))

         #print j, i, ':',j / char_y, i / char_x, '|',
      #print

   return ar


#!/usr/bin/python

def minmax(mtrx):
   minim = 999999999
   maxim = 0

   for j in mtrx:
      for i in j:
         minim = i if i < minim else minim
         maxim = i if i > maxim else maxim
   return minim, maxim

def build (matrix):
    mn = minmax(matrix)[0]
    mx = minmax(matrix)[1]
    span = mx - mn
    piece_size = span / len(chars)

    #print mn, mx, span, piece_size, len(chars)

    ret = ""
    for j in matrix:
        for i in j:
            cur = (i - mn) / piece_size
            cur = cur if cur < len(chars) else len(chars) - 1
            ret += chars[cur]

        ret += "\n"
    return ret


#print run(4,2)
print build(run(10,20))
