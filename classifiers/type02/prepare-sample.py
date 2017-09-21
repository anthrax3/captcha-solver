import os
import glob
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy import misc

chars = os.listdir("./sample")

print chars
labels = []
values = []

for i,char in enumerate(chars):
    print i,"==="
    for img in glob.glob("./sample/" + char + "/*.png"):
        im0 = misc.imread(img, mode="L")
        values.append(np.array(im0.ravel()))
        labels.append(np.array(i))
df = pd.DataFrame([], columns=["label"] + range(40 * 40))
df.label = labels
df.values[:, 1:] = values
# print df.info

print len(chars)

print df.values.shape

im1 = df.values[200, 1:].reshape((40, 40)).astype(int)
plt.imshow(im1, cmap=plt.cm.gray)
plt.show()

df.to_csv("sample.csv",index=False)
