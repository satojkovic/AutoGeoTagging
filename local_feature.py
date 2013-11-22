#-*- coding: utf-8 -*-

import cv2
import sys


class LocalFeature:
    def __init__(self, feat_type='SIFT'):
        self.feat_type = feat_type

    def extract(self, image):
        if image.split('.')[1] != 'jpg':
            print "skip: %s" % image
            return
        else:
            print "--- %s ---" % image

        try:
            img = cv2.imread(image)
        except:
            print "failed to load %s" % image
            sys.exit()

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detector = cv2.FeatureDetector_create(self.feat_type)
        kpts = detector.detect(img)
        print "[%s] num of keypoints: %d" % (self.feat_type, len(kpts))
