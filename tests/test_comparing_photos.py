import os
from datetime import date
from wheel.signatures import assertTrue

from PIL import Image

from helpers.file_downloader import FileDownloader
from helpers.file_helper import FileHelper
from helpers.compare_images import CompareImages
from nasa_test_framework.resources.mars_rover_photo_resource import MarsRoverPhotoResource

__author__ = 'anton.skomarovskyi@gmail.com'


class TestComparingPhotos:
    # folder names & paths
    _TEST_DATA_FOLDER_NAME = 'test_data'
    _MARTIAN_SOL_FOLDER_NAME = 'martian_sol'
    _EARTH_DATE_FOLDER_NAME = 'earth_date'

    @classmethod
    def setup_class(cls):
        FileHelper.create_folder(cls._TEST_DATA_FOLDER_NAME, '/..')
        os.chdir('%s/../%s' % (os.getcwd(), cls._TEST_DATA_FOLDER_NAME))

        FileHelper.create_folder(cls._MARTIAN_SOL_FOLDER_NAME)
        FileHelper.create_folder(cls._EARTH_DATE_FOLDER_NAME)

    @classmethod
    def teardown_class(cls):
        pass

    def test_getting_by_martian_sol_vs_earth_date(self):
        amount_of_photos_for_verification = 10

        # arrange
        mars_photo_resource = MarsRoverPhotoResource()
        response_by_martian_sol = mars_photo_resource.get_by_martian_sol(1000)
        response_by_earth_date = mars_photo_resource.get_by_earth_date(date(2015, 5, 30))

        # act
        martian_sol_metadata = response_by_martian_sol['photos'][:amount_of_photos_for_verification]
        earth_date_metadata = response_by_earth_date['photos'][:amount_of_photos_for_verification]

        self._download_photos_from_api(self._MARTIAN_SOL_FOLDER_NAME, martian_sol_metadata)
        self._download_photos_from_api(self._EARTH_DATE_FOLDER_NAME, earth_date_metadata)

        first_folder_images = FileHelper.get_folder_files('%s/%s' % (os.getcwd(), self._MARTIAN_SOL_FOLDER_NAME))
        second_folder_images = FileHelper.get_folder_files('%s/../%s' % (os.getcwd(), self._EARTH_DATE_FOLDER_NAME))

        # assert
        for i in range(amount_of_photos_for_verification):
            image1 = Image.open(first_folder_images[i])
            image1_id = os.path.basename(first_folder_images[i]).split('.')[0]
            image1_metadata = self._get_photo_metadata_by_id(martian_sol_metadata, image1_id)

            image2 = Image.open(second_folder_images[i])
            image2_id = os.path.basename(second_folder_images[i]).split('.')[0]
            image2_metadata = self._get_photo_metadata_by_id(earth_date_metadata, image2_id)

            assertTrue(CompareImages.equal(image1, image2) and
                       image1_metadata == image2_metadata,
                       'Images are different!')

    def _download_photos_from_api(self, folder, photos_data):
        file_downloader = FileDownloader(folder)
        for photo in photos_data:
            image_name = '%s.jpg' % photo['id']
            image_url = photo['img_src']

            file_downloader.download_img(
                image_url,
                image_name)

        os.chdir('%s/..' % os.getcwd())

    def _get_photo_metadata_by_id(self, data_source, photo_id):
        for photo in data_source:
            if photo['id'] == int(photo_id):
                return photo
