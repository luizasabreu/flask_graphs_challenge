from unittest import TestCase

from mongoengine import connect, disconnect
from flask import Flask

from src.routes import add_routes
from test.conftest import mock_input_data


class TestRouteCalculate(TestCase):
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

    def test_dikstra(self):
        data = mock_input_data()
        destinations = data.get('destinations')
        distances = data.get('distances')
        

        

    def test_calculate(self):
        """Test trip calculate"""
        with self.app.test_client() as test_client:                        
            response = test_client.post('/calculate', data=mock_input_data())            

            waited = {"places_to_travel": 
                      ["Munich", 
                       "Mitling", 
                       "Kinganru", 
                       "Facenianorth", 
                       "Kinganru", 
                       "SantaTiesrie"]}

            self.assertDictEqual(waited, response.json)
