import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery

class Testing_Nubbin_Battery (unittest.TestCase):
    def tst_needs_service_True (self):
        current_date = date.fromisoformat ("2022-08-08")
        last_service_date = date.fromisoformat ("2015-02-08")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue (battery.needs_service())
    
    def tst_needs_service_False (self):
        current_date = date.fromisoformat ("2022-08-08")
        last_service_date = date.fromisoformat ("2021-02-08")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse (battery.needs_service())