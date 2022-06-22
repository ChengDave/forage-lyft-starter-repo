import unittest
from tire.octoprime_tire import OctoprimeTire

class Test_Octoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear_sensors = [1,1,1,0.1]
        tire = OctoprimeTire(tire_wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear_sensors = [0.5,0.5,0.5,0.5]
        tire = OctoprimeTire(tire_wear_sensors)
        self.assertFalse(tire.needs_service())

if __name__ == "__main__":
    unittest.main()
    
