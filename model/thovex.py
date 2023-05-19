from datetime import datetime, timedelta
 import car

 class Thovex(Car):
    def __init__(self, last_service_date, engine, battery, tire):
        super().__init__(last_service_date)
        self.add_part(engine)
        self.add_part(battery)
        self.add_part(tire)