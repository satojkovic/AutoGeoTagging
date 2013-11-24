#-*- encoding: utf-8 -*-

from insta_image import InstaImage
from insta_imageset_iterator import InstaImageSetIterator
from collections import defaultdict
import dircache


class InstaImageSet(object):
    def __init__(self, img_dir):
        self.insta_images = defaultdict(InstaImage)
        self.last = 0
        self.__load_images(img_dir)

    def get_image_at(self, index):
        return self.insta_images[index]

    def append_image(self, img):
        self.insta_images[self.last] = img
        self.last += 1

    def get_length(self):
        return self.last

    def iterator(self):
        return InstaImageSetIterator(self)

    def __load_images(self, img_dir):
        for img_filename in dircache.listdir(img_dir):
            if img_filename.endswith('.jpg'):
                self.insta_images[self.last] = InstaImage(img_filename)
                self.last += 1
