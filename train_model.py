#-*- coding: utf-8 -*-
import os
from sklearn.multiclass import OneVsRestClassifier


def main():
    img_dir = 'images/'
    images = [img_dir + f for f in os.listdir(img_dir)]
    labels = [f.split('/')[-1].split('_')[0] for f in images]
    num_labels = len(sorted(set(labels), key=labels.index))

if __name__ == '__main__':
    main()
