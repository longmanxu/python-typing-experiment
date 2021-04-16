from power_source import PowerSource
from typing import List


class ElectricGrid:
    def __init__(self, power_sources: List[PowerSource]):
        self.power_sources = power_sources

    def total_power(self) -> float:
        return sum(power_source.power for power_source in self.power_sources)

    def can_fulfill_demand(self, demand: float) -> bool:
        return self.total_power() >= demand

    def simulate_time(self, time: float) -> None:
        for power_source in self.power_sources:
            power_source.simulate_time(time)
