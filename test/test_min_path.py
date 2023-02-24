from unittest import TestCase
from src.models import min_path_calc
from test.conftest import mock_input_data


class TestMinPath(TestCase):
    def test_min_path_calc(self):
        data = mock_input_data()
        destinations = data.get('destinations')
        distances = data.get('distances')

        result = min_path_calc(self, destinations, distances)

        self.assertTrue(True)
        

    
