from ascii_utils import *
import numpy as np
import cv2
import matplotlib.pyplot as plt
import scipy

import time

class AsciiArtist:
    def __init__(self):
        self._img = None
        self._max_x = 50
        self._max_y = 50
        self._threshhold = 100

    def set_max_x(self, x):
        self._max_x = x

    def set_max_y(self, y):
        self._max_y = y

    def set_threshold(self, t):
        self._threshhold = t

    def set_threshold_auto(self):
        self._threshhold = self._img.mean()

    def load_image(self, path_to_image):
        img = cv2.imread(path_to_image, 0) 
        self._img = np.asarray(img)

    def create_ascii(self):
        y, x = self._img.shape
        dot_size = 1
        while x//(2*dot_size) > self._max_x or y//(4*dot_size) > self._max_y:
            dot_size += 1

        width, height = x//(2*dot_size), y//(4*dot_size)

        time.sleep(1)
        
        for j in range(height):
            for i in range(width):
                img_slice = self._img[4*dot_size*j:4*dot_size*(j+1), 2*dot_size*i:2*dot_size*(i+1)]
                slice_bin = ""
                for ii in range(2):
                    for jj in range(4):
                        if img_slice[jj*dot_size:(jj+1)*dot_size, ii*dot_size:(ii+1)*dot_size].size == 0:
                            print(i, j, ii, jj, img_slice[jj*dot_size:(jj+1)*dot_size, ii*dot_size:(ii+1)*dot_size].shape)

                        if img_slice[jj*dot_size:(jj+1)*dot_size, ii*dot_size:(ii+1)*dot_size].mean() < self._threshhold:
                            slice_bin = "1" + slice_bin
                        else:
                            slice_bin = "0" + slice_bin
                print(dots(bin2dec(slice_bin)), end='')
            print()


    def create_histogram(self):
        tresholds = np.linspace(0, 255, 21)
        plt.hist(self._img.flatten(), bins = tresholds)
        plt.show()

# Example usage
if __name__ == "__main__":
    aa = AsciiArtist()
    aa.load_image('img2.jpg')
    aa.set_max_x = 50
    aa.set_max_y = 50

    for i in range(20):
        aa.set_threshold(10*i)
        print(f"\n--- {i*10} ---")
        aa.create_ascii()


    