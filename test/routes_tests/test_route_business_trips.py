from unittest import TestCase

from mongoengine import connect, disconnect
from flask import Flask
import requests
from src.models.penguin_travel import PenguinTravel

from src.routes import add_routes
from test.conftest import mock_input_data


class TestRouteBusinessTrips(TestCase):
    @classmethod
    def setUpClass(cls):
        connect('9fe2c4e93f654fdbb24c02b15259716c',
                uuidRepresentation="standard",
                host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def setUp(self):
        self.app = Flask(__name__)
        add_routes(self.app)

    def test_route_business_trips(self):
        """Test business trip information"""
        with self.app.test_client() as test_client:
            # Arrange
            items_count = 3
            expected = {
                'penguins_with_most_trips': ["Alanto"],
                'most_visited_place': ["Munich", "Mitling"],
                'total_business_trips': items_count
                }
            penguin_travels = [self.__create_trips_mock() for _ in range(items_count)]
                    
            # Act
            response = test_client.get('/business-trips')

            for penguin in penguin_travels:
                penguin.delete()

            # Assert
            self.assertDictEqual(response.json, expected)

    
    def __create_trips_mock(self, input_data = mock_input_data() ):
         
         penguin_travel = PenguinTravel(name=input_data["name"], 
                                   is_business_trip=input_data["business"], 
                                   destinations=["Munich", "Mitling"])   
         penguin_travel.save()       
         return penguin_travel
