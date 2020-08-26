from skimage import io
import numpy as np
from sklearn.cluster import KMeans, MiniBatchKMeans
import os
from PIL import Image
def segmentation(imageDir, k, saveDir):

    img = Image.open(imageDir)
    if img.mode != 'RGB':
        rgb = img.convert('RGB')
        rgb.save(imageDir)

    img = io.imread(imageDir)
    dim = {
        'height': img.shape[0],
        'width': img.shape[1],
        'channels': img.shape[2],
        'pixels': img.shape[0]*img.shape[1],
    }
    dataMat = (img/255.0).reshape(dim['pixels'],3)
    kmeans = MiniBatchKMeans(k).fit(dataMat)
    kColors = kmeans.cluster_centers_[kmeans.predict(dataMat)]

    k_img = np.reshape(kColors, (img.shape))
    io.imsave(saveDir,k_img)
