from unittest import TestCase

from mongoengine import connect, disconnect
from flask import Flask
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

    def create_trips_mock(self, input_data = mock_input_data() ):
         
         penguin_travel = PenguinTravel(name=input_data["name"], 
                                   is_business_trip=input_data["business"], 
                                   places_to_travel=["Munich", "Mitling"])   
         penguin_travel.save()       
         return penguin_travel

    def test_trips_info(self):
        """Test business trip information"""
        with self.app.test_client() as test_client:           
            input_data = mock_input_data() 

            penguin_travel = self.create_trips_mock()
            penguin_travel = self.create_trips_mock()
            penguin_travel = self.create_trips_mock()                      

            response = test_client.get('/business-trips')

            waited = {'penguins_with_most_trips': ["Alanto"],
              'most_visited_place': ["Munich", "Mitling"],
              'total_business_trips': 3}
                        
            penguin_travel.delete()            
            self.assertDictEqual(waited, response.json)
