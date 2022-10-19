import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery

class Testing_Splindler_Battery (unittest.TestCase):
    def tst_needs_service_True (self):
        current_date = date.fromisoformat ("2022-08-08")
        last_service_date = date.fromisoformat ("2019-02-08")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue (battery.needs_service())
    
    def tst_needs_service_False (self):
        current_date = date.fromisoformat ("2022-08-08")
        last_service_date = date.fromisoformat ("2021-02-08")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())