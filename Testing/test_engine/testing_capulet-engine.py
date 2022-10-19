import unittest
from engine.capulet_engine import CapuletEngine

class Test_Capulet_Engine (unittest.TestCase):
    def tst_needs_service_True (self):
        current_mileage = 30005
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    def tst_needs_service_False (self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())