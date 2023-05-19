from abc import ABC

import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_replacement_date):
        self.last_replacement_date = last_replacement_date

    def battery_should_be_replaced(self):
        replacement_threshold_date = self.last_replacement_date.replace(year=self.last_replacement_date.year + 3)
        if replacement_threshold_date < datetime.today().date():
            return True
        else:
            return False