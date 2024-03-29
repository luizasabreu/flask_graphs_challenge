from unittest import TestCase
import pytest
from src.models.penguin_travel import PenguinTravel
from src.services.penguin_travel_access import save_penguin_travel


class TestPenguinTravelAccess(TestCase):
    
    @pytest.fixture(autouse=True)
    def monkeypatched_save_penguin_travel(self, monkeypatch):
        def save_penguin_travel(self):
            pass
        monkeypatch.setattr(PenguinTravel, "save", save_penguin_travel)

    def test_save_penguin_travel(self):
        # Arrange
        name = "Alanto"
        business = True        
        places_to_travel = ['Kinganru']

        # Act
        save_penguin_travel(name, business, places_to_travel)        

        # Assert
        self.assertTrue(True)