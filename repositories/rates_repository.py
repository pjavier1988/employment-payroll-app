from repositories.repository import Repository
from connections.file_data_source import FileDataSource
from domain.models import Rate

from datetime import datetime, timedelta


class RatesRepository(Repository):
    def __init__(self, source):
        self.source = source

    def read_data(self) -> dict:
        rate_objects = []
        rate_objects = [Rate(day, datetime.strptime(start_time, '%H:%M'),
                        datetime.strptime(end_time, '%H:%M'), amount)
                        for day, time_range, amount in self.source
                        for start_time, end_time in [time_range.split('-')]]

        return rate_objects

    def get_rate(self, day_of_week: str, time: datetime, rates) -> float:

        for rate in rates:

            if (rate.day.strip() == day_of_week.strip()
                and rate.start_time.time() <= rate.end_time.time()):
                if (rate.day.strip() == day_of_week.strip()
                    and rate.start_time.time() <= time.time()
                    <= rate.end_time.time()):
                    return rate.amount
            else:
                if (rate.day.strip() == day_of_week.strip()
                    and (rate.start_time.time() <= time.time() or time.time()
                         <= rate.end_time.time())):
                    return rate.amount
        return 0.0


