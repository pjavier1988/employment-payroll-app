import sys
import os

import unittest
from datetime import datetime
from unittest.mock import MagicMock
from src.repositories.employee_schedule_repository import EmployeeScheduleRepository
from src.repositories.rates_repository import RatesRepository
from src.services.employee_schedule_service import EmployeeScheduleService
from src.domain.models import Schedule
from unittest.mock import patch


class TestServices(unittest.TestCase):
    def setUp(self) -> None:
        self.rates = [
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
        self.employee_data = {
            'RENE': [
                Schedule("MO", datetime(2023, 3, 28, 10),
                         datetime(2023, 3, 28, 12)),
                Schedule("TU", datetime(2023, 3, 29, 10),
                         datetime(2023, 3, 29, 12)),
                Schedule("TH", datetime(2023, 3, 31, 1),
                         datetime(2023, 3, 31, 3)),
                Schedule("SA", datetime(2023, 4, 1, 14),
                         datetime(2023, 4, 1, 18)),
                Schedule("SU", datetime(2023, 4, 2, 20),
                         datetime(2023, 4, 2, 21))
            ],
            'ASTRID': [
                Schedule("MO", datetime(2023, 3, 28, 10),
                         datetime(2023, 3, 28, 12)),
                Schedule("TH", datetime(2023, 3, 31, 12),
                         datetime(2023, 3, 31, 14)),
                Schedule("SU", datetime(2023, 4, 2, 20),
                         datetime(2023, 4, 2, 21))
            ],

        }

        self.mock_data = MagicMock(return_value=self.employee_data)
        self.mock_file_contents = 'RENE=MO10:00-12:00,TU10:00-12:00,\
        TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
        self.mock_file = MagicMock(return_value=self.mock_file_contents
                                   .splitlines())

    def test_when_hours_worked_on_monday_betwwen_10_and_12_return30_dollars(self):
        schedule = Schedule("MO", datetime(2023, 3, 28, 10),
                            datetime(2023, 3, 28, 12))
        expected_payment_value = 30.0
        rate_repository = RatesRepository(self.rates)
        payroll_repository = EmployeeScheduleRepository(self.mock_file)
        employee_service = EmployeeScheduleService(payroll_repository,
                                                   rate_repository)
        payment_value = employee_service.calculate_pay(rate_repository,
                                                       schedule)
        self.assertEqual(payment_value, expected_payment_value)

    def test_when_input_employee_is_rene_pyament_value_is215(self):
        with patch('src.repositories.employee_schedule_repository.EmployeeScheduleRepository.read_data') as mock_get_data:
            expected_name = "RENE"
            expected_payment_value = 215.0
            payroll_repository = EmployeeScheduleRepository(self.mock_file)
            rate_repository = RatesRepository(self.rates)

            mock_get_data.return_value = self.mock_data.return_value

            employee_service = EmployeeScheduleService(payroll_repository,
                                                       rate_repository)
            payment_value = employee_service.\
                            calculate_payment_by_employee(expected_name)

            mock_get_data.assert_called_once()
            self.assertEqual(payment_value, expected_payment_value)

    def test_when_input_employee_is_astrid_pyament_value_is85(self):
        with patch('src.repositories.employee_schedule_repository.EmployeeScheduleRepository.read_data') as mock_get_data:
            expected_name = "ASTRID"
            expected_payment_value = 85.0
            payroll_repository = EmployeeScheduleRepository(self.mock_file)
            rate_repository = RatesRepository(self.rates)

            mock_get_data.return_value = self.mock_data.return_value

            employee_service = EmployeeScheduleService(payroll_repository,
                                                       rate_repository)
            payment_value = employee_service\
                            .calculate_payment_by_employee(expected_name)
            mock_get_data.assert_called_once()
            self.assertEqual(payment_value, expected_payment_value)


if __name__ == '__main__':
    unittest.main()
