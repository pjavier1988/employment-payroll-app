from .datasource import DataSource


class FileDataSource(DataSource):
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as f:
            data = f.read()
        return data
