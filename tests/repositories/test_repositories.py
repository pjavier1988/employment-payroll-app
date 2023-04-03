import sys
import os
import unittest
from unittest.mock import (
    MagicMock,
    patch
    )

from src.repositories.employee_schedule_repository import EmployeeScheduleRepository


class TestRepositories(unittest.TestCase):
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
        self.mock_file_contents = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
        self.mock_file = MagicMock(return_value=self.mock_file_contents.
                                   splitlines())

    def test_when_read_file_returns_dict(self):
        with patch("src.repositories.employee_schedule_repository.EmployeeScheduleRepository.connect") as mock_get_data:
            expected_name = "RENE"
            payroll_system = EmployeeScheduleRepository(self.mock_file)
            mock_get_data.return_value = self.mock_file.return_value
            res = payroll_system.read_data()

            mock_get_data.assert_called_once()
            self.assertIsInstance(res, dict)
            self.assertIn(expected_name, res.keys())


if __name__ == '__main__':
    unittest.main()
