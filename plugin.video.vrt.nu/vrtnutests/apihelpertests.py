import unittest
from resources.lib.vrtplayer import vrtapihelper

class ApiHelperTests(unittest.TestCase):

    def test_get_api_data_single_season(self):
        api_helper = vrtapihelper.VRTApiHelper()
        title_items = api_helper.get_video_items('/vrtnu/a-z/animal-babies.relevant/', None)
        self.assertEqual(3, len(title_items))

    def test_get_api_data_multiple_seasons(self):
        api_helper = vrtapihelper.VRTApiHelper()
        title_items = api_helper.get_video_items('/vrtnu/a-z/thuis.relevant/', None)
        self.assertTrue(len(title_items) < 5)
    
    def test_get_api_data_specific_season(self):
        api_helper = vrtapihelper.VRTApiHelper()
        title_items = api_helper.get_video_items('/vrtnu/a-z/thuis.relevant/', '24')
        self.assertTrue(len(title_items) > 5)
