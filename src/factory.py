import numpy as np
import random

from .energy import Energies
from .people import People
from .utils import BetaDistributions

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

    new_cost = lambda costs, bought: costs
    new_amount = lambda amount, bought: amount

    return Energies(
        initial_costs=costs,
        initial_amounts=amounts,
        pollution_factors=pollution_factors,
        new_cost=new_cost,
        new_amount=new_amount
    )

# TODO : get the max from distribution to normalize
def mean_var(low, high, size, mini, maxi):
    means = np.random.uniform(low=low, high=high, size=size)
    variances = np.random.uniform(low=0.1*means, high=0.3*means, size=size)
    return BetaDistributions(means, variances, mini, maxi)

distributions = {"mean_var": mean_var,
                 }
def draw_from_dist(distribution_name, **kwparameters):
    return distributions[distribution_name](**kwparameters)

def random_β_distribution(α_range, β_range):
    α, β = np.random.rand(2)
    α = α * α_range[1] + α_range[0]
    β = β * β_range[1] + β_range[0]
    return α, β


interractions = {"random": 
                    lambda peo, ligh, heat: (np.random.choice([0, 1], size=(peo, ligh), p=[0.8, 0.2]),
                                             np.random.choice([0, 1], size=(peo, heat), p=[0.9, 0.1])),
                }

def draw_interraction(nb_people, nb_lights, nb_heaters, style="random"):
    return interractions[style](nb_people, nb_lights, nb_heaters)

def build_people(config, nb_lights, nb_heaters):
    pollution_pref_params = config["pollution_pref"]
    nuclear_pref_params = config["nuclear_pref"]
    lights_pref_params = config["lights_pref"]
    heat_pref_params = config["heat_pref"]
    nb_people = config["nb_people"]

    print("Pollution")
    pollution_pref = draw_from_dist(size=nb_people, **pollution_pref_params)
    print("Nuclear")
    nuclear_pref = draw_from_dist(size=nb_people, **nuclear_pref_params)
    print("Lights")
    lights_pref = draw_from_dist(size=nb_people, **lights_pref_params)
    print("Heat")
    heat_pref = draw_from_dist(size=nb_people, **heat_pref_params)
    light_inter, heat_inter = draw_interraction(nb_people, nb_lights, nb_heaters, config["interraction"])

    return People(
        pollution_pref=pollution_pref,
        nuclear_pref=nuclear_pref,
        lights_pref=lights_pref,
        heater_pref=heat_pref,
        lights_interraction=light_inter,
        heaters_interraction=heat_inter
    )


def build_lights(config):
    return np.ones(config["nb_lights"])


def build_heaters(config):
    heaters = np.random.randn(config["nb_heaters"])
    heaters = (config["mean_temperature"] + heaters) * config["std_temperature"]
    return heaters

