import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import glob,os
from scipy import misc
from .threshold import threshold_L
# from denoise import denoise_R
from .crop import crop_proj


def predict(im0):
    # im0 = misc.imread(file,'L')
    p=''
    im0[:, 0] = 255
    im0[:, -1] = 255
    im0[0, :] = 255
    im0[-1, :] = 255
    im1 = threshold_L(im0)

    # plt.imshow(im1,cmap=plt.cm.gray)
    # plt.show()
    
    crop = crop_proj(im1)
    input, charArr, char = [], [], []

    for img1 in glob.glob(os.path.abspath(os.path.dirname(__file__))+'/crop/*.png'):
        charArr.append(misc.imread(img1, 'L'))
        char.append(img1[-5:-4])
    
    for a, b, c, d in zip(crop[0], crop[1], crop[2], crop[3]):
        try:
            input.append(misc.imresize(im1[a:b, c:d], (12, 12)))
        except Exception as e:
            print(e)
    pred = ''
    for i in input:
        min = 1000
        for n, c in zip(charArr, char):
            b = np.linalg.norm(n - i)

            if b < min:

                min = b
                p = c

        pred += p
    return pred

if __name__ == '__main__':
    im0 = misc.imread("./imgs/10.gif", 'L')
    result = predict(im0)
    print(result)
