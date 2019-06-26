def buil_all(configs):
    energies = build_energies(configs["energies"])
    people = build_people(configs["people"])
    transports = build_transports(configs["transports"])
    lights = build_lights(configs["lights"])
    heaters = build_heaters(configs["heaters"])

    return {
        "energies": energies,
        "people": people,
        "transports": transports,
        "lights": lights,
        "heaters": heaters
    }


def build_energies(config):
    raise NotImplementedError


def build_people(config):
    raise NotImplementedError


def build_transports(config):
    raise NotImplementedError


def build_lights(config):
    raise NotImplementedError


def build_heaters(config):
    raise NotImplementedError


if __name__ == '__main__':
    pass
