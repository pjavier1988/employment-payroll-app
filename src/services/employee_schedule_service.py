from src.repositories.employee_schedule_repository \
    import EmployeeScheduleRepository
from src.repositories.rates_repository import RatesRepository


class EmployeeScheduleService:
    def __init__(self,
                 employee_schedule_repository: EmployeeScheduleRepository,
                 rate_repository: RatesRepository)\
                      -> None:
        self.employee_schedule_repository = employee_schedule_repository
        self.rate_repository = rate_repository

    def calculate_payment_by_employee(self, employee_name: str) -> float:
        employee_schedules = self.employee_schedule_repository.read_data()
        employee_schedule = employee_schedules.get(employee_name)
        total_payment = 0
        for schedule in employee_schedule:
            total_payment += self.calculate_pay(self.rate_repository, schedule)
        return total_payment

    def calculate_pay(self, rate_repository, schedule) -> int:
        rate = rate_repository.get_rate(schedule.day, schedule.start_time,
                                        rate_repository.read_data())
        hours_worked = (schedule.end_time -
                        schedule.start_time).total_seconds() / 3600
        pay = hours_worked * rate
        return pay

