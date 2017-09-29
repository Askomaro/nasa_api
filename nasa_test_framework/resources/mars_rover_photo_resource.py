import json
from datetime import date

import requests

from nasa_test_framework.resources.base_resource import BaseResource


__author__ = 'anton.skomarovskyi@gmail.com'

DEFAULT_API_KEY = 'VE9TyFhe0CITgrkfsb6pr89uPlTHwNsDvGQJkXx4'


class MarsRoverPhotoResource(BaseResource):
    _URL_API_PATH = '/mars-photos/api/v1/rovers/curiosity/photos?'

    def __init__(self):
        self.__url_path = "%s%s%s" % (self._SCHEMA,
                                      self._HOST,
                                      self._URL_API_PATH)

    def get_by_martian_sol(self, sol, camera=None, page=1, api_key=DEFAULT_API_KEY):
        """
        QUERYING BY MARTIAN SOL
        :type sol: int
        :type camera: str
        :type page: int
        :type api_key: str
        """

        params = {
            'sol': sol,
            'camera': camera,
            'page': page,
            'api_key': api_key
        }

        return self.__get_response(params)

    def get_by_earth_date(self, earth_date, camera=None, page=1, api_key=DEFAULT_API_KEY):
        """
        QUERYING BY EARTH DATE
        :type earth_date: date
        :type camera: str
        :type page: int
        :type api_key: str
        """

        params = {
            'earth_date': earth_date,
            'camera': camera,
            'page': page,
            'api_key': api_key
        }

        return self.__get_response(params)

    def __get_response(self, params):
        r = requests.get(self.__url_path, params=params)

        return json.loads(r.text)
