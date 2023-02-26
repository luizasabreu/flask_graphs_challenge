from unittest import TestCase

import pytest
from src.services.penguin_travel_access import get_penguin_travels

from src.services.travel_statistics import get_most_visited_places, get_penguins_with_most_trips, get_total_business_trips


class TestTravelStatistics(TestCase):
    def test_get_penguins_with_most_trips(self):
        # Arrange
        penguin_travels = self.__mock_penguin_travels()
        expected = ["Luiza"]

        # Act
        result = get_penguins_with_most_trips(penguin_travels)        

        # Assert
        self.assertEqual(result, expected)

    def test_get_most_visited_places(self):
        # Arrange
        penguin_travels = self.__mock_penguin_travels()
        expected = ["Brazil"]

        # Act
        result = get_most_visited_places(penguin_travels)        

        # Assert
        self.assertEqual(result, expected)

    def test_get_total_business_trips(self):
        # Arrange
        penguin_travels = self.__mock_penguin_travels()
        expected = 1

        # Act
        result = get_total_business_trips(penguin_travels)        

        # Assert
        self.assertEqual(result, expected)

    def __mock_penguin_travels(self):
        class MockedPenguinTravel():
            def __init__(self) -> None:
                self.name = "Luiza"
                self.destinations = ["Brazil"]
                self.is_business_trip = True
        return [MockedPenguinTravel()]
        
