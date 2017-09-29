from wheel.signatures import assertTrue


from nasa_test_framework.resources.mars_rover_photo_resource import MarsRoverPhotoResource


__author__ = 'anton.skomarovskyi@gmail.com'

ROVER_CAMERAS_ABBREVIATION = \
    ['FHAZ', 'RHAZ', 'MAST', 'CHEMCAM', 'MAHLI', 'MARDI', 'NAVCAM', 'PANCAM', 'MINITES']


class TestComparingCameraTakenPhotos:

    def test_check_photos_count_of_each_camera(self):
        boundary_to_check = 10

        mars_photo_resource = MarsRoverPhotoResource()
        photos_taken_per_camera = []

        for camera in ROVER_CAMERAS_ABBREVIATION:
            response = mars_photo_resource.get_by_martian_sol(1000, camera)
            amount_of_photos = len(response['photos'])
            photos_taken_per_camera.append(amount_of_photos)

        for initial_item in photos_taken_per_camera:
            for item_to_compare in photos_taken_per_camera:
                assertTrue(initial_item * boundary_to_check > item_to_compare,
                           'One of the camera made 10 times more images than any other. '
                           '(%s vs %s)' % (initial_item, item_to_compare))
