import os


__author__ = 'anton.skomarovskyi@gmail.com'


class FileHelper:
    @staticmethod
    def create_folder(directory, path=None):
        path = os.getcwd() if path is None else '%s/%s' % (os.getcwd(), path)
        full_path = '%s/%s' % (path, directory)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

    @staticmethod
    def get_folder_files(path):
        os.chdir(path)

        return os.listdir(os.getcwd())
