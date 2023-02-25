from unittest import TestCase
from src.services import get_optimal_path
from test.conftest import mock_input_data


class TestMinPath(TestCase):
    def test_min_path_calc(self):
        data = mock_input_data()
        destinations = data.get('destinations')
        distances = data.get('distances')

        result = get_optimal_path(destinations, distances)
        waited = ['Munich', 'Mitling', 'Kinganru', 'Facenianorth', 'Kinganru', 'SantaTiesrie']

        self.assertEqual(waited, result)
        

    
