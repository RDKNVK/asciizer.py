#!/usr/bin/python

import sys, getopt
import Image

if len(sys.argv) != 4:
  print '\nUsage: \n\n asciilizer.py path/to/file char_width char_height'
  exit()

im = Image.open(sys.argv[1])
w, h = int(sys.argv[2]), int(sys.argv[3])

chars = ''

with open('asciizer.chars', 'r') as f: 
  chars = f.readlines()[0][::-1]

#chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

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
   return ar

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
    ret = ""
    for j in matrix:
        for i in j:
            cur = (i - mn) / piece_size
            cur = cur if cur < len(chars) else len(chars) - 1
            ret += chars[cur]

        ret += "\n"
    return ret

#print run(4,2)
print build(run(w,h))
