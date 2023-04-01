from datetime import datetime
from typing import List


class Rate:
    def __init__(self, day: str, start_time: datetime, end_time: datetime,
                 amount: int):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.amount = amount


class Schedule:
    def __init__(self, day: str, start_time: datetime, end_time: datetime):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time


class Employee:
    def __init__(self, name: str, schedules: List[Schedule]):
        self.name = name
        self.schedules = schedules
