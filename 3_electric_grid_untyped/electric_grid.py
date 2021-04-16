class ElectricGrid:
    def __init__(self, power_sources):
        self.power_sources = power_sources

    def total_power(self):
        return sum(power_source.power for power_source in self.power_sources)

    def can_fulfill_demand(self, demand):
        return self.total_power() >= demand

    def simulate_time(self, time):
        for power_source in self.power_sources:
            power_source.simulate_time(time)
