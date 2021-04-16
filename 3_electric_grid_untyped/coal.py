from power_source import PowerSource


class Coal:
    def __init__(self, amount):
        self.amount = amount

    def has_coal(self):
        return self.amount > 0.0

    def simulate_time(self, time, consumption_rate):
        self.amount -= consumption_rate * time
        if self.amount < 0.0:
            self.amount = 0.0


class CoalPowerPlant(PowerSource):
    def __init__(
            self,
            power,
            coal,
            efficiency
    ):
        self.__operating_power = power
        self.__coal = coal
        self.__consumption_rate = power / efficiency
        self.__power = self.__calculate_power()

    def get_id(self):
        return 'A'

    @property
    def power(self):
        return self.__power

    def simulate_time(self, time):
        self.__coal.simulate_time(time, self.__consumption_rate)
        self.__update_power()

    def __calculate_power(self):
        return self.__operating_power if self.__coal.has_coal() else 0.0

    def __update_power(self):
        self.__power = self.__calculate_power()

    def add_fuel(self, coal):
        self.__coal = Coal(self.__coal.amount + coal.amount)


class OldCoalPowerPlant(CoalPowerPlant):
    def __init__(self):
        super().__init__(100.0, Coal(200.0), 0.3)

    def get_id(self):
        return 'AA'


class NewCoalPowerPlant(CoalPowerPlant):
    def __init__(self):
        super().__init__(200.0, Coal(300.0), 0.5)

    def get_id(self):
        return 'AB'
