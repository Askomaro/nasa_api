import os

import requests


__author__ = 'anton.skomarovskyi@gmail.com'


class FileDownloader:
    def __init__(self, path_to_set_working_directory):
        os.chdir('%s/%s' % (os.getcwd(), path_to_set_working_directory))

    def download_img(self, url, file_name):
        r = requests.get(url, stream=True)

        if r.status_code == 200:
            with open(file_name, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
