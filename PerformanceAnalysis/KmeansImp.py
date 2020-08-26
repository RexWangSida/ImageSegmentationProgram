import numpy as np
import random
import math
from skimage import io
import os
from PIL import Image
def compDist(centers, pixel):

    dists = []
    for i in centers:
        dists.append(math.sqrt((pixel[0]-i[0])**2+(pixel[1]-i[1])**2+(pixel[2]-i[2])**2))
    return dists

def kmeans(centers, k, data):
    assign = []
    """
    assign item to closest center
    """
    for i in data:
        dists = compDist(centers, i)
        index = dists.index(min(dists))
        assign.append(index)
    """
    compute new centers and update data center
    """
    newCenters = []
    for i in range(len(centers)):
        allPixels = []
        for j in range(len(assign)):
            if i == assign[j]:
                allPixels.append(data[j])
        allPixels = np.array(allPixels)
        newCenters.append(allPixels.mean(axis=0))
    """
    check convergence
    """
    flag = 1
    for i in range(len(centers)):
        if (np.array_equal(centers[i], newCenters[i]) == False):
            flag = 0
    """
    if not converge do recursion
    """
    if flag == 0:
        return kmeans(newCenters, k, data)
    """
    if converge return final data
    """
    finalData = []
    for i in assign:
        finalData.append(newCenters[i])

    return np.array(finalData)




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

    centers = []
    centerIndex = []
    for i in range(k):
        Index = random.randint(0,9)
        while Index in centerIndex:
            Index = random.randint(0,9)
        centerIndex.append(Index)
        center = dataMat[Index]
        centers.append(center)

    result = kmeans(centers, k, dataMat)

    k_img = np.reshape(result, (img.shape))
    io.imsave(saveDir,k_img)
