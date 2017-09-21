import base64
import re
import io
from scipy import misc
import classifiers
from classifiers import type01, type02


def model(v):
    return v


class Classifier(object):
    def __init__(self):
        pass

    def readImage(self, img_base64, mode):
        sub = re.sub(r"data:image/.*?;base64,", '', img_base64)
        img_bytes = base64.b64decode(sub)
        image = misc.imread(io.BytesIO(img_bytes), mode=mode)
        return image

    def resizeImage(self, image, size):
        if not size:
            return image
        resized = misc.imread(image, size)
        return resized

    def predict(self, x):
        y = model(x)
        return y + "  parent"


class ClassifierType01(Classifier):
    def __init__(self):
        super().__init__()

    def predict(self, x):
        y = type01.predict(x)
        print("predict type1")
        return y


class ClassifierType02(Classifier):
    def __init__(self):
        super().__init__()

    def predict(self, x):
        y = model(x)
        return y + "  child type2"


operator = {
    "type01": ClassifierType01(),
    "type02": ClassifierType02(),
    "type03": ClassifierType01(),
    "type04": ClassifierType01(),
    "type05": ClassifierType01(),
    "type06": ClassifierType01(),
}

####################################
# imread
# prepare
# predict
#####################################

def predict(type, img_base64, mode='L', resize=False, proba=False):
    classifier = operator[type]
    im0 = classifier.readImage(img_base64, mode)
    im1 = classifier.resizeImage(im0, resize)
    return classifier.predict(im1)


if __name__ == '__main__':
    y = predict("type02", "a")
    print(y)
