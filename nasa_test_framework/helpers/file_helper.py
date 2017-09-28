import os


__author__ = 'anton.skomarovskyi@gmail.com'


class FileHelper:
    @staticmethod
    def create_folder(directory):
        path = os.getcwd()
        if not os.path.exists('%s/%s' % (directory, path)):
            os.makedirs(directory)
