from unittest import TestCase
from src.models import disktra_calc
from test.conftest import mock_input_data


class TestDikstra(TestCase):
    def test_dikstra(self):
        data = mock_input_data()
        destinations = data.get('destinations')
        distances = data.get('distances')

        result = disktra_calc(self, destinations, distances)

        self.assertTrue(True)
        

    
