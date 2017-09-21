import numpy as np
import scipy as sp
from scipy import misc,ndimage

def crop_proj(im):
    im_ = im.copy()
    sumX = np.sum(im_,axis=0)
    cropX1,cropX2 = [],[]
    for r in range(im_.shape[1]):
        if sumX[r]<255*im_.shape[0] and sumX[r-1]==255*im_.shape[0]:
            cropX1.append(r)
        if sumX[r-1]<255*im_.shape[0] and sumX[r]==255*im_.shape[0]:
            cropX2.append(r)

    cropY1,cropY2 = [],[]
    for a,b in zip(cropX1,cropX2):
        sumY = np.sum(im_[:,a:b],axis=1)
        for r in range(im_.shape[0]):
            if sumY[r] < 255 * (b-a) and sumY[r - 1] == 255 * (b-a):
                cropY1.append(r)
            if sumY[r - 1] < 255 * (b-a) and sumY[r] == 255 * (b-a):
                cropY2.append(r)
    return cropY1,cropY2,cropX1,cropX2
