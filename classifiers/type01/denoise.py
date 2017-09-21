import numpy as np
import scipy as sp
from scipy import misc

def denoise_R(im,R=1,limit=3):
    im_ = im.copy()
    for x, y in zip(np.where(im_ == 0)[0], np.where(im_ == 0)[1]):
        x1 = x - R if x - R > 0 else 0
        x2 = x + R if x + R < im_.shape[0] else im_.shape[0]
        y1 = y - R if y - R > 0 else 0
        y2 = y + R if y + R < im_.shape[1] else im_.shape[1]
        sum = np.count_nonzero(im_[x1:x2+1, y1:y2+1] == 0)
        if sum <= limit:
            im_[x, y] = 255
    return im_