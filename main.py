from repositories.employee_schedule_repository \
    import EmployeeScheduleRepository
from services.employee_schedule_service import EmployeeScheduleService
from repositories.rates_repository import RatesRepository
from collections import defaultdict


class PayrollSystem:
    def __init__(self,
                 employee_schedule_repository: EmployeeScheduleRepository,
                 rates_repository: RatesRepository,
                 employee_service: EmployeeScheduleService):
        self.employee_pay = defaultdict(float)
        self.employee_schedule_repository = employee_schedule_repository
        self.rates_repository = rates_repository
        self.employee_service = employee_service

    def calculate_payroll(self):
        names = self.employee_schedule_repository.read_data().keys()
        for name in names:
            amount = self.employee_service.calculate_payment_by_employee(name)

            self.employee_pay[name] = amount

    def print_payrll(self):
        for name, total_pay in self.employee_pay.items():
            print(f"The amount to pay {name} is {total_pay:.2f} USD")


def main():
    employee_schedule_repository = EmployeeScheduleRepository("employee_schedule.txt")

    rates = [
            ('MO', '00:01-09:00', 25),
            ('MO', '09:01-18:00', 15),
            ('MO', '18:01-00:00', 20),
            ('TU', '00:01-09:00', 25),
            ('TU', '09:01-18:00', 15),
            ('TU', '18:01-00:00', 20),
            ('WE', '00:01-09:00', 25),
            ('WE', '09:01-18:00', 15),
            ('WE', '18:01-00:00', 20),
            ('TH', '00:01-09:00', 25),
            ('TH', '09:01-18:00', 15),
            ('TH', '18:01-00:00', 20),
            ('FR', '00:01-09:00', 25),
            ('FR', '09:01-18:00', 15),
            ('FR', '18:01-00:00', 20),
            ('SA', '00:01-09:00', 30),
            ('SA', '09:01-18:00', 20),
            ('SA', '18:01-00:00', 25),
            ('SU', '00:01-09:00', 30),
            ('SU', '09:01-18:00', 20),
            ('SU', '18:01-00:00', 25)
        ]
    rates_repository = RatesRepository(rates)
    employee_service = EmployeeScheduleService(employee_schedule_repository,
                                               rates_repository)
    payroll = PayrollSystem(employee_schedule_repository,
                            rates_repository,
                            employee_service)
    payroll.calculate_payroll()
    payroll.print_payrll()


if __name__ == '__main__':
    main()
