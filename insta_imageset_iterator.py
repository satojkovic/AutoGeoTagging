#-*- encoding: utf-8 -*-


class InstaImageSetIterator():
    def __init__(self, image_set):
        self.image_set = image_set
        self.index = 0

    def next(self):
        if self.index < self.image_set.get_length():
            img = self.image_set.get_image_at(self.index)
            self.index += 1
            return img
        else:
            raise StopIteration

    def __iter__(self):
        return self
