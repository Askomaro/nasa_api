from datetime import date

from nasa_test_framework.Resources.mars_rover_photo_resource import MarsRoverPhotoResource
from nasa_test_framework.helpers.file_downloader import FileDownloader
from nasa_test_framework.helpers.file_helper import FileHelper


__author__ = 'anton.skomarovskyi@gmail.com'


class TestComparingPhotos:
    # folder names
    _TEST_DATA_FOLDER_NAME = 'test_data'
    _MARTIAN_SOL_FOLDER_NAME = 'martian_sol'
    _EARTH_DATE_FOLDER_NAME = 'earth_date'

    def test_getting_by_martian_sol_vs_earth_date(self):
        amount_of_photos_for_verification = 10
        img_names_to_compare = []

        FileHelper.create_folder(self._TEST_DATA_FOLDER_NAME)
        FileHelper.create_folder(self._MARTIAN_SOL_FOLDER_NAME)
        FileHelper.create_folder(self._EARTH_DATE_FOLDER_NAME)

        # arrange
        mars_photo_resource = MarsRoverPhotoResource()

        response_by_martian_sol = mars_photo_resource.get_by_martian_sol(1000)
        martian_sol_data = response_by_martian_sol['photos'][:amount_of_photos_for_verification]

        response_by_earth_date = mars_photo_resource.get_by_earth_date(date(2015, 5, 30))
        earth_date_data = response_by_earth_date['photos'][:amount_of_photos_for_verification]

        for idx, image_url in enumerate(response_by_martian_sol['photos']):
            image_name = 'test_img_%s.jpg' % idx
            path_to_save_file = '%s/%s/%s' % \
                                (
                                    self._TEST_DATA_FOLDER_NAME,
                                    self._MARTIAN_SOL_FOLDER_NAME,
                                    image_name
                                )

            FileDownloader.download_img(image_url['img_src'], path_to_save_file)
            img_names_to_compare.append(image_name)
