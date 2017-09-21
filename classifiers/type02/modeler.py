import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Convolution2D,MaxPooling2D
from keras.utils import np_utils
# from keras.utils.visualize_util import plot
from keras.optimizers import SGD

from sklearn.cross_validation import train_test_split

batch_size = 20
nb_classes = 14
nb_epoch = 50

img_rows,img_cols = 40,40

nb_filters = 64
pool_size = (2,2)
kernel_size = (3,3)

data = pd.read_csv("sample.csv").values

X_data = data[:,1:]
y_data = data[:,0]

X_data = X_data.astype(np.float32)
X_data /= 255.0
X_data = X_data.reshape(X_data.shape[0],1,40,40)

y_data = np_utils.to_categorical(y_data)

X_train,X_test,y_train,y_test = train_test_split(X_data,y_data,test_size=0.2,random_state=2017)


# X_train = train[:,1:]#.reshape(train.shape[0],1,40,40)
# y_train = train[:,0]
# X_train = X_train.astype(np.float32)
# X_train /= 255.0
# X_test /= 255.0
# y_train = np_utils.to_categorical(y_train)
# y_test = np_utils.to_categorical(y_test)

print(X_train.shape)
print(y_train.shape)

input_dim = X_train.shape[1]
# ================= MLP ==================
# model = Sequential()
# model.add(Dense(800, input_dim=input_dim))
# model.add(Activation('relu'))
# model.add(Dropout(0.15))
# model.add(Dense(400))
# model.add(Activation('relu'))
# model.add(Dropout(0.15))
# model.add(Dense(nb_classes))
# model.add(Activation('softmax'))

# ================= CNN ==================
model = Sequential()
model.add(Convolution2D(80,4,4,
                        activation='relu',
                        input_shape=(1,40,40),
                        init='he_normal'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Convolution2D(160,4,4,
                        activation='relu',
                        init='he_normal'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(280,activation='relu',init='he_normal'))
model.add(Dropout(0.3))
model.add(Dense(140,activation='relu',init='he_normal'))
model.add(Dropout(0.3))
model.add(Dense(nb_classes,activation='softmax',init='he_normal'))


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


model.fit(X_train,y_train,
          batch_size=batch_size,
          nb_epoch=nb_epoch,
          verbose=1,validation_data=(X_test,y_test))

scores = model.evaluate(X_test, y_test)
print("\n====", scores)

# plot(model,"cnn.png")

import os,glob
from scipy import misc
chars = os.listdir("./sample")
print(chars)

model.save("model-cnn.h5")


# plt.figure(figsize=(10,12))
# idx = 1
#
# for i,img in enumerate(glob.glob("./unsorted/*.png")):
#     if  20<= i <40:
#         x = misc.imread(img,mode='L')
#         x = np.array(x.ravel()).astype(np.float32)
#         x /= 255.0
#         y = model.predict_classes(x.reshape(1,1,40,40),batch_size=batch_size)
#         ax = plt.subplot(20,4,idx)
#         ax.set_title(chars[y[0]],color='r')
#         ax.imshow(misc.imread(img,mode='L'),cmap=plt.cm.gray)
#         idx+=1
#
# plt.show()


# X_test0 = misc.imread("./unsorted/735_1.png",mode='L')
# X_test0 = np.array(X_test0.ravel()).astype(np.float32)
# X_test0 /= 255.0
# y_test0 = model.predict_classes(X_test0.reshape(1,1,40,40),batch_size=batch_size)
#
# print y_test0,chars[y_test0[0]]

