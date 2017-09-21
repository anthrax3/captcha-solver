import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy import misc,ndimage
from detect_peaks import detect_peaks
import skimage
import collections
from skimage.filters import threshold_adaptive
from skimage.restoration import denoise_bilateral,denoise_nl_means
from skimage.morphology import opening
from scipy.signal import argrelextrema

def get_block_s(a):
    for i,x in enumerate(a):
        if i>2:
            if a[i]!=0 & a[i-1]==0 & a[i-2]==0 & a[i-1]==0:
                return i
def get_block_e(a):
    for i, x in enumerate(a):
        if -i < - 2:
            if a[-i] != 0 & a[-i + 1] == 0 & a[-i + 1] == 0 & a[-i + 2] == 0:
                return -i+1
def get_block(a):
    return get_block_s(a),get_block_e(a)
def crop_tb(im):  # crop top and bottom
    hs = im.sum(1)
    s, e = get_block(hs)
    return im[s:e, :]
def crop_hist(img_src):
    try:
        im0 = misc.imread(img_src, mode="L")
    except Exception as e:
        return [], [], [], []
    im0 = np.invert(im0)
    selem = np.array([[0,1,0],
                 [1,1,1],
                   [0, 1, 0]])
    im0 = opening(im0, selem)
    ys = (im0.sum(0))
    indexes = detect_peaks(ys, mpd=25, mph=3200, valley=True)
    if (len(indexes) == 5):
        im1 = im0[:, indexes[0]:indexes[1]]
        im2 = im0[:, indexes[1]:indexes[2]]
        im3 = im0[:, indexes[2]:indexes[3]]
        im4 = im0[:, indexes[3]:indexes[4]]
    elif (len(indexes) == 4 and indexes[0] >= 25):
        im1 = im0[:, 0:indexes[0]]
        im2 = im0[:, indexes[0]:indexes[1]]
        im3 = im0[:, indexes[1]:indexes[2]]
        im4 = im0[:, indexes[2]:indexes[3]]
    elif (len(indexes) == 4 and indexes[0] < 10):
        im1 = im0[:, indexes[0]:indexes[1]]
        im2 = im0[:, indexes[1]:indexes[2]]
        im3 = im0[:, indexes[2]:indexes[3]]
        im4 = im0[:, indexes[3]:]
    else:
        return [],[],[],[],
    im1 = crop_tb(im1)
    im2 = crop_tb(im2)
    im3 = crop_tb(im3)
    im4 = crop_tb(im4)
    return im1,im2,im3,im4
# img_src = "23.png"
# im1,im2,im3,im4 = crop_hist(img_src)
#
#
# plt.figure()
#
# plt.subplot(411)
# plt.imshow(im1,cmap=plt.cm.gray)
#
# plt.subplot(412)
# plt.imshow(im2,cmap=plt.cm.gray)
#
# plt.subplot(413)
# plt.imshow(im3,cmap=plt.cm.gray)
#
# plt.subplot(414)
# plt.imshow(im4,cmap=plt.cm.gray)
#
# plt.show()