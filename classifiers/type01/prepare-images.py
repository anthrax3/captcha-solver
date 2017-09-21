import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import glob
from scipy import misc,ndimage

from threshold import threshold_L
from denoise import denoise_R
from crop import crop_proj

i,skip=0,0
for img in glob.glob('./imgs/*.gif'):
    im0 = misc.imread(img,'L')
    im0[:,0] = 255
    im0[:, -1] = 255
    im0[0, :] = 255
    im0[-1, :] = 255
    im1 = threshold_L(im0)
    # im2 = denoise_R(im1, 1, 3)
    im2 = im1
    # print im2
    crop = crop_proj(im2)
    print crop
    for a,b,c,d in zip(crop[0],crop[1],crop[2],crop[3]) :
        i+=1
        try:
            misc.imsave('./crop/%i.png' % i,misc.imresize(im2[a:b,c:d],(12,12)))
        except Exception,e:
            skip+=1
    if i % 100 ==0:
        print i,".."
print "done",i,"skip",skip



# test
# im0 = misc.imread('./imgs/1.gif','L')
# im00 = misc.imread('./imgs/1.gif')
# im0 = im0[1:im0.shape[0]-1,1:im0.shape[1]-1]
#
# im1 = threshold_L(im0)
# im2 = denoise_R(im1)
#
#
# plt.figure(figsize=(8,8))
# plt.subplot(311)
# plt.title('original')
# plt.imshow(im00)
#
# plt.subplot(312)
# plt.title('threshold')
# plt.imshow(im1,cmap=plt.cm.gray)
#
# plt.subplot(313)
# plt.title('denoise')
# plt.imshow(im2,cmap=plt.cm.gray)
#
# plt.subplots_adjust(hspace=.4)
# plt.show()


