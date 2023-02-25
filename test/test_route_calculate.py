from unittest import TestCase

from mongoengine import connect, disconnect
from flask import Flask
import requests

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

    def test_example(self):
        res = requests.post('http://127.0.0.1:8001/calculate', json=mock_input_data())
        waited = ["Munich", 
                       "Mitling", 
                       "Kinganru", 
                       "Facenianorth", 
                       "Kinganru", 
                       "SantaTiesrie"]
        
        self.assertEqual(waited, res.json())


    def test_calculate(self):
        """Test trip calculate"""
        with self.app.test_client() as test_client:                        
            response = test_client.post('/calculate', json=mock_input_data())            

            waited = ["Munich", 
                       "Mitling", 
                       "Kinganru", 
                       "Facenianorth", 
                       "Kinganru", 
                       "SantaTiesrie"]

            self.assertEqual(waited, response.json)
