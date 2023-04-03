from .datasource import DataSource


class StaticDataSource(DataSource):
    def __init__(self, data):
        self.data = data

    def read_data(self):

        return self.data
