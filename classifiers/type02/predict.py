import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy import misc,ndimage
import glob
from detect_peaks import detect_peaks
import skimage
import collections
from skimage.filters import threshold_adaptive
from skimage.restoration import denoise_bilateral,denoise_nl_means
from skimage import morphology
from scipy.signal import argrelextrema
from crop_hist import crop_hist

from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Convolution2D,MaxPooling2D
from keras.utils import np_utils
from keras.optimizers import SGD

from sklearn.cross_validation import train_test_split

batch_size = 40

import os
from scipy import misc
chars = os.listdir("./sample")
print(chars)

img_src = "./imgs/5.png"

from keras.models import load_model
model = load_model("model-cnn.h5") # Accuracy 98%

# im1,im2,im3,im4 = crop_hist(img_src)
# plt.figure()
# plt.subplot(5,1,1)
# plt.imshow(misc.imread(img_src),cmap=plt.cm.gray)
# idx = 2
# if im1 != []:
#     for i, im in enumerate([im1, im2, im3, im4]):
#         im = misc.imresize(im, (40, 40))
#         x = np.array(im.ravel()).astype(np.float32)
#         x /= 255.0
#         y = model.predict_classes(x.reshape(1, 1, 40, 40))
#         ax = plt.subplot(5, 1, idx)
#         ax.set_title(chars[y[0]], color='r')
#         ax.imshow(im, cmap=plt.cm.gray)
#         idx += 1
# else:
#     print "failed to crop",img_src
# plt.show()

def predict(img_src):
    im1, im2, im3, im4 = crop_hist(img_src)
    result = ''
    plt.figure()
    plt.subplot(5, 1, 1)
    plt.imshow(misc.imread(img_src), cmap=plt.cm.gray)
    idx = 2
    if im1 != []:
        for i, im in enumerate([im1, im2, im3, im4]):
            im = misc.imresize(im, (40, 40))
            x = np.array(im.ravel()).astype(np.float32)
            x /= 255.0
            y = model.predict_classes(x.reshape(1, 1, 40, 40))
            ax = plt.subplot(5, 1, idx)
            ax.set_title(chars[y[0]], color='r')
            result += chars[y[0]][0]
            ax.imshow(im, cmap=plt.cm.gray)
            idx += 1
        plt.show()
        return result
    else:
        print("failed to crop", img_src)
        return ""


print(predict(img_src))
