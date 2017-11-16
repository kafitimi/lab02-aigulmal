# -*- coding: utf-8 -*-

from PIL import Image
from math import pi, log, exp
import numpy as np
import sys

def main(filename, r):
    # должна обрабатывать файл filename гауссовым размытием в квадрате [-r, +r] x [-r, +r]
    # и записывать результат в <filename>.gaussblurred.png
    img = Image.open(filename)
    img.load()

    r = 3
    dx, dy = np.meshgrid(np.arange(-r, +r+1, 1.), np.arange(-r, +r+1, 1.0))
    sigma = 0.38*r
    gauss_dist = np.exp( -(dx*dx+dy*dy)/(2*sigma**2) ) / (2*pi*sigma**2)
    coeff = gauss_dist / np.sum(gauss_dist)

    # код сюда ....
    def gauss_blur(img, r):
        w, h = img.size
        a = np.array(img.getdata(), dtype=np.uint8)\
        .reshape(h,w)
        b= np.zeros((h, w), dtype=np.uint8)
        for i in range(h):
            for j in range(w):
                s=0.
                up, bt = max(i - r, 0), min(i + r + 1, h)
                lf, rt = max(j - r, 0), min(j + r + 1, w)
                b[i, j] += a[up:bt, lf:rt]*coeff
            return Image.fromarray(b)
    newimg = img
    newimg.show()
    newimg.save(filename+'.gaussblurred.png')



if __name__=='__main__':
    # Запускать с командной строки с аргументом <имя файла>, например: python gauss.py darwin.png
    if len(sys.argv) > 1:
        main(sys.argv[1], r=3)
    else:
        print("Must give filename.\n")



