from unittest import TestCase

from mongoengine import connect, disconnect
from flask import Flask
import pytest
import requests

from src.routes import add_routes


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

    def test_route_calculate(self):
        """Test trip calculate"""
        with self.app.test_client() as test_client:                                   
            # Arrange
            waited = ["Munich", 
                       "Mitling", 
                       "Kinganru", 
                       "Facenianorth", 
                       "Kinganru", 
                       "SantaTiesrie"]
            # Act
            response = test_client.post('/calculate', json=self.input_data) 

            # Assert
            self.assertEqual(waited, response.json)

        
    def test_route_calculate_from_example(self):
        # Arrange
        waited = ["Munich", 
                 "Mitling", 
                 "Kinganru", 
                 "Facenianorth", 
                 "Kinganru", 
                 "SantaTiesrie"]
        
        # Act
        res = requests.post('http://127.0.0.1:8001/calculate', json=self.input_data)

        # Assert        
        self.assertEqual(waited, res.json())

    @pytest.fixture(autouse=True)
    def __mock_input_data(self, mock_input_data_fixture):
        self.input_data =  mock_input_data_fixture