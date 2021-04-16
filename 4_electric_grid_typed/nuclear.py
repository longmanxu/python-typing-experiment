from power_source import PowerSource
from typing import Iterable


class NuclearFuel:
    def __init__(self, mass: float):
        self.mass = mass

    def has_fuel(self) -> bool:
        return self.mass > 0.0

    def simulate_time(self, time: float, consumption_rate: float) -> None:
        self.mass -= consumption_rate * time
        if self.mass < 0.0:
            self.mass = 0.0

    def __add__(self, other: 'NuclearFuel') -> 'NuclearFuel':
        return NuclearFuel(self.mass + other.mass)


class NuclearReactor(PowerSource):
    def __init__(
            self,
            power: float,
            fuel: NuclearFuel,
            efficiency: float
    ) -> None:
        self.__operating_power = power
        self.__fuel = fuel
        self.__consumption_rate = power / efficiency
        self.__power = self.__calculate_power()

    def get_id(self) -> str:
        return 'B'

    @property
    def power(self) -> float:
        return self.__power

    def simulate_time(self, time: float) -> None:
        self.__fuel.simulate_time(time, self.__consumption_rate)
        self.__update_power()

    def __calculate_power(self) -> float:
        return self.__operating_power if self.__fuel.has_fuel() else 0

    def __update_power(self) -> None:
        self.__power = self.__calculate_power()

    def add_fuel(self, fuel: NuclearFuel) -> None:
        self.__fuel += fuel


class OldNuclearReactor(NuclearReactor):
    def __init__(self) -> None:
        super().__init__(10.0, NuclearFuel(1000.0), 0.8)

    def get_id(self) -> str:
        return 'BA'


class NewNuclearReactor(NuclearReactor):
    def __init__(self) -> None:
        super().__init__(20.0, NuclearFuel(2000.0), 0.95)

    def get_id(self) -> str:
        return 'BB'


class NuclearPowerPlant(PowerSource):
    def __init__(self, reactors: Iterable[NuclearReactor]) -> None:
        self.reactors = list(reactors)

    def get_id(self) -> str:
        return 'C'

    @property
    def power(self) -> float:
        return sum(reactor.power for reactor in self.reactors)

    def simulate_time(self, time: float) -> None:
        for reactor in self.reactors:
            reactor.simulate_time(time)

    def add_fuels(self, reactor_number: int, fuel: NuclearFuel) -> None:
        self.reactors[reactor_number].add_fuel(fuel)


class OldNuclearPowerPlant(NuclearPowerPlant):
    def __init__(self) -> None:
        super().__init__(OldNuclearReactor() for _ in range(4))

    def get_id(self) -> str:
        return 'CAa'


class NewNuclearPowerPlant(NuclearPowerPlant):
    def __init__(self) -> None:
        super().__init__(NewNuclearReactor() for _ in range(4))

    def get_id(self) -> str:
        return 'CB'
