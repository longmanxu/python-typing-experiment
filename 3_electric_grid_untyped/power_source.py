import abc


class PowerSource(abc.ABC):
    @property
    @abc.abstractmethod
    def power(self):
        ...

    @abc.abstractmethod
    def simulate_time(self, time):
        ...

    @abc.abstractmethod
    def get_id(self):
        ...
