from unittest import TestCase
from src.services import get_optimal_path
from test.conftest import mock_input_data



class TestPathOtimization(TestCase):
    destinations = ["Kinganru", "Facenianorth", "SantaTiesrie"]
    distances = [
        "Munich - Munich: 0",
        "Munich - Kinganru: 3",
        "Munich - Facenianorth: 7",
        "Munich - SantaTiesrie: 4",
        "Munich - Mitling: 1",
        "Kinganru - Facenianorth: 2",
        "Kinganru - SantaTiesrie: 1",
        "Kinganru - Mitling: 1",
        "Facenianorth - SantaTiesrie: 5",
        "Facenianorth - Mitling:  3",
        "SantaTiesrie - Mitling: 2"]

    def test_get_optimal_path_without_destinations(self):
        # Arrange
        destinations = []
        distances = self.distances
        expected = ['Munich']

        # Act
        result = get_optimal_path(destinations, distances)

        # Assert
        self.assertEqual(result, expected)

    def test_get_optimal_path(self):
        # Arrange
        destinations = self.destinations
        distances = self.distances        
        expected = ['Munich', 'Mitling', 'Kinganru', 'Facenianorth', 'Kinganru', 'SantaTiesrie']

        # Act
        result = get_optimal_path(destinations, distances)        

        # Assert
        self.assertEqual(result, expected)
        

    
