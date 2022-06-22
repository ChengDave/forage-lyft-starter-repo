import unittest
from tire.carrigan_tire import CarriganTire

class Test_Carrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear_sensors = [0,0,0,0.9]
        tire = CarriganTire(tire_wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear_sensors = [0,0,0,0.8]
        tire = CarriganTire(tire_wear_sensors)
        self.assertFalse(tire.needs_service())

if __name__ == "__main__":
    unittest.main()
    
