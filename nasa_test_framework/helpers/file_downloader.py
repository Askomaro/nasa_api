from io import StringIO

from PIL import Image
import requests


__author__ = 'anton.skomarovskyi@gmail.com'


class FileDownloader:
    @staticmethod
    def download_img(url, path):
        r = requests.get(url)
        i = Image.open(StringIO(r.text))
        i.save(path)
