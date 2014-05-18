#-*- coding: utf-8 -*-
import os
import numpy as np
from PIL import Image
from sklearn.multiclass import OneVsRestClassifier
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import LinearSVC
import pandas as pd

STANDARD_SIZE = (300, 167)


def img_to_matrix(filename, verbose=False):
    """
    Load image as array

    Returns
    -------
    imgArray : numpy array
        Image is resized to STANDARD_SIZE
    """
    img = Image.open(filename)
    if verbose:
        print 'changing size from %s to %s' % (str(img.size),
                                               str(STANDARD_SIZE))
    img = img.resize(STANDARD_SIZE)
    imgArray = np.asarray(img)
    return imgArray


def flatten_image(img):
    """
    Flatten image array

    Parameters
    ----------
    img : numpy array
        Image array

    Returns
    -------
        img_wide : numpy array
    """
    img_wide = img.reshape(1, img.size)
    return img_wide[0]


def main():
    img_dir = 'images/'
    images = [img_dir + f for f in os.listdir(img_dir)]
    labels = [f.split('/')[-1].split('_')[0] for f in images]
    label2ids = {v: i for i, v in enumerate(sorted(set(labels),
                                                   key=labels.index))}
    y = np.array([label2ids[l] for l in labels])

    data = []
    for image_file in images:
        img = img_to_matrix(image_file)
        img = flatten_image(img)
        data.append(img)
    data = np.array(data)

    # training samples
    is_train = np.random.uniform(0, 1, len(data)) <= 0.7
    train_X, train_y = data[is_train], y[is_train]

    # training a classifier
    pca = RandomizedPCA(n_components=5)
    train_X = pca.fit_transform(train_X)
    multi_svm = OneVsRestClassifier(LinearSVC())
    multi_svm.fit(train_X, train_y)

    # evaluating the model
    test_X, test_y = data[is_train == False], y[is_train == False]
    test_X = pca.transform(test_X)
    print pd.crosstab(test_y, multi_svm.predict(test_X),
                      rownames=['Actual'], colnames=['Predicted'])

if __name__ == '__main__':
    main()
