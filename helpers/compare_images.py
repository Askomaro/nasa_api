from PIL import ImageChops


__author__ = 'anton.skomarovskyi@gmail.com'


class CompareImages:
    @staticmethod
    def equal(img1, img2):
        return ImageChops.difference(img1, img2).getbbox() is None
