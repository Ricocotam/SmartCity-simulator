""" This module is used to compute different scores once one step of the
simulation is done.

The city is evaluated wrt the following criteria :
* Pollution, How much the energies have poluted for this tick globally (ie.
  the mean of the pollution produced).
* Spendings, Sum of energy cost.
* Citizens' satisfaction (or happiness), Sum of satisfactions of all citizen
  weighted by the importance each citizen give to each criteria (eather,
  lighting).
"""


def compute_scores(people, energies, lights, heaters):
    return {
        "spendings": spendings(energies),
        "pollution": pollution(energies),
        "happiness": satisfaction(people, lights, heaters)
    }


def pollution(energies):
    return (energies.pollution_factors * energies.bought_amounts).mean()


def satisfaction(people, lights, heatings):
    """
    # shape : nb_citizens, nb_opinions
    #log_probas = ...

    scaled = log_probas * preferences
    citizen_satisfaction = scaled.sum(1)
    city_satisfaction = citizen_satisfaction.sum()

    return city_satisfaction
    """
    return 1


def spendings(energies):
    return (energies.bought_amounts * energies.costs).sum()


if __name__ == '__main__':
    pass
