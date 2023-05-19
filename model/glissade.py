from datetime import datetime, timedelta
 import car

 class Glissade(Car):
    def __init__(self, last_service_date, engine, tire):
        super().__init__(last_service_date)
        self.add_part(engine)
        self.add_part(tire)
