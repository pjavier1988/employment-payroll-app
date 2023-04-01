from repositories.repository import Repository
from connections.file_data_source import FileDataSource
from domain.models import Schedule

from datetime import datetime, timedelta


class EmployeeScheduleRepository(Repository):
    def __init__(self, source) -> None:
        self.source = source

    def connect(self):
        file_data_source = FileDataSource(self.source)
        employees_data = file_data_source.read_data()

        return employees_data

    def read_data(self) -> dict:
        employees = {}

        employees_data = self.connect()

        for line in employees_data:

            name, shifts_str = line.strip().split('=')
            shifts = []
            for shift_str in shifts_str.split(','):
                day = shift_str[:2]
                start_time_str, end_time_str = \
                    shift_str[2:len(shift_str)].split('-')
                start_time = datetime.strptime(start_time_str, '%H:%M')
                end_time = datetime.strptime(end_time_str, '%H:%M')
                if end_time < start_time:
                    end_time += timedelta(days=1)
                shifts.append(Schedule(day, start_time, end_time))
            employees[name] = shifts
        return employees
