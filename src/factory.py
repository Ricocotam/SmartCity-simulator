import numpy as np

from .energy import Energies
from .people import People

def build_all(configs):
    energies = build_energies(configs["energies"])
    people = build_people(configs["people"], configs["lights"]["nb_lights"], configs["heaters"]["nb_heaters"])
    lights = build_lights(configs["lights"])
    heaters = build_heaters(configs["heaters"])

    return {
        "energies": energies,
        "people": people,
        "lights": lights,
        "heaters": heaters
    }


def build_energies(config):
    costs = np.array([e["cost"] for e in config["energies"]], dtype=np.float64)
    amounts = np.array([e["amount"] for e in config["energies"]], dtype=np.float64)
    pollution_factors = np.array([e["pollution_factor"] for e in config["energies"]], dtype=np.float64)

    new_cost = lambda x: x
    new_amount = lambda x: 1.3 * x

    return Energies(
        initial_costs=costs,
        initial_amounts=amounts,
        pollution_factors=pollution_factors,
        new_cost=new_cost,
        new_amount=new_amount
    )


distributions = {"uniform": np.random.uniform}
def draw_from_dist(distribution_name, **kwparameters):
    return distributions[distribution_name](**kwparameters)

interractions = {"random": 
                    lambda peo, ligh, heat: (np.random.choice([0, 1], size=(peo, ligh), p=[.9, .1]),
                                             np.random.choice([0, 1], size=(peo, heat), p=[.9, .1]))}
def draw_interraction(nb_people, nb_lights, nb_heaters, style="random"):
    return interractions[style](nb_people, nb_lights, nb_heaters)

def build_people(config, nb_lights, nb_heaters):
    pollution_pref_params = config["pollution_pref"]
    nuclear_pref_params = config["nuclear_pref"]
    lights_pref_params = config["lights_pref"]
    heat_pref_params = config["heat_pref"]

    pollution_pref = draw_from_dist(**pollution_pref_params)
    nuclear_pref = draw_from_dist(**nuclear_pref_params)
    lights_pref = draw_from_dist(**lights_pref_params)
    heat_pref = draw_from_dist(**heat_pref_params)
    light_inter, heat_inter = draw_interraction(config["nb_people"], nb_lights, nb_heaters, config["interraction"])

    return People(
        pollution_pref=pollution_pref,
        nuclear_pref=nuclear_pref,
        lights_pref=lights_pref,
        heater_pref=heat_pref,
        lights_interraction=light_inter,
        heaters_interration=heat_inter
    )


def build_lights(config):
    return np.ones(config["nb_lights"])


def build_heaters(config):
    heaters = np.random.randn(config["nb_heaters"])
    heaters = (config["mean_temperature"] + heaters) * config["std_temperature"]
    return heaters

