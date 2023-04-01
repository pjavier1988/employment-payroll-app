from repositories.repository import Repository
from connection.file_data_source import FileDataSource


class EmployeeScheduleRepository(Repository):
    def __init__(self, source) -> None:
        self.source = source

    def read_data(self) -> dict:
        employees_data = {}
        file_data_source = FileDataSource(self.source)
        employees_data = file_data_source.read_data()
        return employees_data
