import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy import misc, ndimage
import glob
from detect_peaks import detect_peaks
import skimage
import collections
from skimage.filters import threshold_adaptive
from skimage.restoration import denoise_bilateral, denoise_nl_means
from skimage import morphology
from scipy.signal import argrelextrema
from crop_hist import crop_hist

n = 0
for img_src in glob.glob("./imgs/*.png"):
    im1, im2, im3, im4 = crop_hist(img_src)
    if im1 != []:
        for i, im in enumerate([im1, im2, im3, im4]):
            im = misc.imresize(im, (40, 40))
            misc.imsave(
                "./imgs-crop/" + img_src.replace("./imgs\\", "").replace(".png", "") + "_" + str(i + 1) + ".png",
                im)
    else:
        n += 1
        print "failed to crop", img_src
print n
