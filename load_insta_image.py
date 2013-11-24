#-*- encoding: utf-8 -*-

"""
Usage:
    load_insta_image.py <Image_Directory>
    load_insta_image.py -h | --help
    load_insta_image.py --version

Options:
    -h --help    show this screen
    --version    show version
"""


from docopt import docopt
from insta_imageset import InstaImageSet


def main():
    options = docopt(__doc__, version='1.0')
    img_dir = options['<Image_Directory>']

    insta_img_set = InstaImageSet(img_dir)
    for img in insta_img_set.iterator():
        print img.get_filename()

if __name__ == '__main__':
    main()
