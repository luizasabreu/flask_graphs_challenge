import pytest

@pytest.fixture
def mock_destinations_fixture():
        return  ["Kinganru", "Facenianorth", "SantaTiesrie"]

@pytest.fixture
def mock_distances_fixture():
    return  ["Munich - Munich: 0",
            "Munich - Kinganru: 3",
            "Munich - Facenianorth: 7",
            "Munich - SantaTiesrie: 4",
            "Munich - Mitling: 1",
            "Kinganru - Facenianorth: 2",
            "Kinganru - SantaTiesrie: 1",
            "Kinganru - Mitling: 1",
            "Facenianorth - SantaTiesrie: 5",
            "Facenianorth - Mitling:  3",
            "SantaTiesrie - Mitling: 2"]

@pytest.fixture
def mock_penguin_travels_fixture():
    class MockedPenguinTravel():
        def __init__(self) -> None:
            self.name = "Alanto"
            self.destinations = ["Kinganru"]
            self.is_business_trip = True
            
    return [MockedPenguinTravel()]
        
