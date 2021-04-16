import coal
import nuclear
import electric_grid


def test_add_coal():
    c = coal.CoalPowerPlant(100.0, coal.Coal(30.0), 0.5)
    c.add_fuel(coal.Coal(21.0))


def test_add_fuel():
    n = nuclear.NuclearReactor(100.0, nuclear.NuclearFuel(20.0), 0.9)
    n.add_fuel(nuclear.NuclearFuel(30.0))


def make_power_source():
    return electric_grid.ElectricGrid([
        coal.OldCoalPowerPlant(),
        coal.NewCoalPowerPlant(),
        nuclear.OldNuclearReactor(),
        nuclear.NewNuclearReactor(),
        nuclear.OldNuclearPowerPlant(),
        nuclear.NewNuclearPowerPlant(),
    ])


def test_grid_power():
    e = make_power_source()
    assert e.total_power() == 450.0
    assert e.can_fulfill_demand(450.0)
    assert not e.can_fulfill_demand(450.1)


def test_simulate():
    e = make_power_source()
    e.simulate_time(3.14)


def create_power_source(source_type):
    if source_type == 'old coal':
        return coal.OldCoalPowerPlant()
    elif source_type == 'new coal':
        return coal.NewCoalPowerPlant()
    elif source_type == 'old nuclear reactor':
        return nuclear.OldNuclearReactor()
    elif source_type == 'new nuclear reactor':
        return nuclear.NewNuclearReactor()
    elif source_type == 'old nuclear plant':
        return nuclear.OldNuclearPowerPlant()
    elif source_type == 'new nuclear plant':
        return nuclear.NewNuclearPowerPlant()

    raise ValueError(f'Unknown power source type: {source_type}')


def test_old_nuclear_power_plant_id():
    with open('old_nuclear_plant_type.txt') as f:
        plant_type = f.readline().rstrip()

    plant = create_power_source(plant_type)
    assert plant.get_id() == 'CA'


if __name__ == '__main__':
    test_add_coal()
    test_add_fuel()
    test_grid_power()
    test_simulate()
    test_old_nuclear_power_plant_id()
