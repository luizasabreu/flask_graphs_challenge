from unittest import TestCase

import pytest
from src.services import get_optimal_path



class TestPathOtimization(TestCase):
    
    @pytest.fixture(autouse=True)
    def mock_destinations(self, mock_destinations_fixture):
        self.destinations =  mock_destinations_fixture

    @pytest.fixture(autouse=True)
    def mock_distances(self, mock_distances_fixture):
        self.distances = mock_distances_fixture

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
    
        

    
