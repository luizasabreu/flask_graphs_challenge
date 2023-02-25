from unittest import TestCase
from src.services import min_path_calc
from test.conftest import mock_input_data


class TestMinPath(TestCase):
    def test_min_path_calc(self):
        data = mock_input_data()
        destinations = data.get('destinations')
        distances = data.get('distances')

        result = min_path_calc(destinations, distances)
        waited = ['Munich', 'Mitling', 'Kinganru', 'Facenianorth', 'Kinganru', 'SantaTiesrie']

        self.assertEqual(waited, result)
        

    
