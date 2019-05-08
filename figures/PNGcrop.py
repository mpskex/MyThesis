# coding: utf-8
import os
import cv2
import sys
import numpy as np
from argparse import ArgumentError

def crop(img, bgcolor=[255,255,255]):
    y, x, _ = np.split(np.transpose(np.array(np.where(img!=bgcolor)), axes=[1,0]), 3, axis=-1)
    y, x = np.squeeze(y), np.squeeze(x)
    ty, lx = np.min(y), np.min(x)
    by, rx = np.max(y), np.max(x)
    return img[ty:by, lx:rx]

def crop_dir(dir, out_dir):
    for name in os.listdir(dir):
        if '.PNG' in name or '.png' in name:
            print("[*]\tcropped image `" + name + "`!")
            cv2.imwrite(out_dir + name, crop(cv2.imread(dir+name)))
    print("Finished..")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: PNGcrop.py <dir> <out_dir>")
    else:
        crop_dir(sys.argv[1], sys.argv[2])