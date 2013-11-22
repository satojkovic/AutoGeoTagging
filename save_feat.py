#-*- coding: utf-8 -*-

from local_feature import LocalFeature
import os


def main():
    sift = LocalFeature(feat_type='SIFT')

    image_dir = 'photos'
    for file_name in os.listdir(image_dir):
        image = os.path.join(image_dir, file_name)
        sift.extract(image)

if __name__ == '__main__':
    main()
