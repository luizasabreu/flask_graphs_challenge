from unittest import TestCase

from mongoengine import connect, disconnect
from flask import Flask

from src.routes import add_routes
from src.models import Example


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

    def test_trips_info(self):
        """Test business trip information"""
        with self.app.test_client() as test_client:
            response = test_client.get('/business-trips')

            waited = {'penguins_with_most_trips': "luiza",
              'most_visited_place': ['teste1', 'teste2'],
              'total_business_trips': 3}
            
            self.assertDictEqual(waited, response.json)
