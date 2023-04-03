from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def read_data(self) -> dict:
        pass
