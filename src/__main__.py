from .smart_city import SmartCity
from .engine import Engine


def main():
    people = None
    energies = None
    transports = None
    lights = None
    heatings = None

    smart_city = SmartCity(people=people, energies=energies,
                           transports=transports, lights=lights,
                           heatings=heatings)
    engine = Engine(smart_city)


if __name__ == '__main__':
    main()
