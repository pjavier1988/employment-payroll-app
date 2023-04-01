from repositories.employee_schedule_repository \
    import EmployeeScheduleRepository


def main():
    employee_repository = EmployeeScheduleRepository("employee_schedule.txt")
    print(employee_repository.read_data())


if __name__ == '__main__':
    main()
