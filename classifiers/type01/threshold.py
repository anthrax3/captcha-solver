import numpy as np
import scipy as sp
from scipy import misc
from skimage import data,util


def threshold_L(im, threshold=150):
    im_ = im.copy()
    im_[im_ > threshold] = 255
    im_[im_ <= threshold] = 0
    return im_

def threshold_RGB(im, threshold=150, r=0.33, g=0.33, b=0.33):
    im_ = im[:,:,0]*r + im[:,:,1]*g + im[:,:,2]*b
    im_[im_ > threshold] = 255
    im_[im_ <= threshold] = 0
    return im_

if __name__ == '__main__':
    print("hello")

# def threshold_RGB(im, threshold=150, r=0.3, g=0.3, b=0.3):
#     table = []
#     for row in im:
#         for rgb in row:
#             v = rgb[0] * r + rgb[1] * g + rgb[2] * b
#             table.append(0) if v < threshold else table.append(255)
#     table = np.array(table).reshape(im.shape[0], im.shape[1])
#     return table

# def threshold_L(im,threshold=150):
#     table = []
#     for row in im:
#         for l in row:
#             v = l
#             table.append(0) if v < threshold else table.append(255)
#     table = np.array(table).reshape(im.shape)
#     return table

# def threshold_RGB(im,threshold=150,r=0.3,g=0.3,b=0.3):
#     table = []
#     for row in im:
#         for rgb in row:
#             v = rgb[0]*r+rgb[1]*g+rgb[2]*b
#             table.append(0) if v < threshold else table.append(255)
#     table = np.array(table).reshape(im.shape[0], im.shape[1])
#     return table