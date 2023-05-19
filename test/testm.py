
import unittest
from datetime import datetime, timedelta
from BET import CapuletEngine, SternmanEngine, WilloughbyEngine, NubbinBattery, SpindlerBattery, CarriganTire, OctoprimeTire

class EngineBatteryTireTestCase(unittest.TestCase):
    def setUp(self):
        self.last_service_date = datetime.now() - timedelta(days=365)

    def test_spindler_battery_should_be_replaced_true(self):
        spindler_battery = SpindlerBattery(self.last_service_date - timedelta(days=3*365))
        self.assertTrue(spindler_battery.battery_should_be_replaced())

    def test_spindler_battery_should_be_replaced_false(self):
        spindler_battery = SpindlerBattery(self.last_service_date - timedelta(days=2*365))
        self.assertFalse(spindler_battery.battery_should_be_replaced())

    def test_carrigan_tire_needs_service_true(self):
        tire_wear = [0.9, 0.8, 0.7, 0.6]
        carrigan_tire = CarriganTire(tire_wear)
        self.assertTrue(carrigan_tire.needs_service())

    def test_carrigan_tire_needs_service_false(self):
        tire_wear = [0.8, 0.7, 0.6, 0.5]
        carrigan_tire = CarriganTire(tire_wear)
        self.assertFalse(carrigan_tire.needs_service())

    def test_octoprime_tire_needs_service_true(self):
        tire_wear = [0.8, 0.9, 0.7, 0.6]
        octoprime_tire = OctoprimeTire(tire_wear)
        self.assertTrue(octoprime_tire.needs_service())

    def test_octoprime_tire_needs_service_false(self):
        tire_wear = [0.8, 0.8, 0.7, 0.6]
        octoprime_tire = OctoprimeTire(tire_wear)
        self.assertFalse(octoprime_tire.needs_service())

if __name__ == '__main__':
    unittest.main()
