import numpy as np

from .energy import Energies, identity_sample

def buil_all(configs):
    energies = build_energies(configs["energies"])
    people = build_people(configs["people"])
    lights = build_lights(configs["lights"])
    heaters = build_heaters(configs["heaters"])

    return {
        "energies": energies,
        "people": people,
        "lights": lights,
        "heaters": heaters
    }


def build_energies(config):
    costs = [e["cost"] for e in config["energies"]]
    amounts = [e["amount"] for e in config["energies"]]
    pollution_factors = [e["pollution_factor"] for e in config["energies"]]

    sampler_cost_factors = identity_sample
    sampler_amount_factors = identity_sample

    return Energies(
        initial_costs=costs,
        initial_amounts=amounts,
        pollution_factors=pollution_factors,
        sampler_cost_factors=sampler_cost_factors,
        sampler_amount_factors=sampler_amount_factors
    )


def build_people(config):
    raise NotImplementedError


def build_lights(config):
    return np.ones(config["nb_lights"])


def build_heaters(config):
    heaters = np.random.randn(config["nb_heaters"])
    heaters = (config["mean_temperature"] + heaters) * config["std_temperature"]
    return heaters


if __name__ == '__main__':
    pass
