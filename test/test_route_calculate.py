from unittest import TestCase

from mongoengine import connect, disconnect
from flask import Flask, jsonify
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

    

    def test_calculate(self, mock_input_data=mock_input_data()):
        """Test trip calculate"""
        with self.app.test_client() as test_client:   
            import pdb;pdb.set_trace()                       
            response = test_client.post('/calculate', data=mock_input_data)
            

            waited = {"places_to_travel": ["Munich", "Mitling", "Kinganru", "Facenianorth", "Kinganru", "SantaTiesrie"]}

            self.assertDictEqual(waited, response.json)
