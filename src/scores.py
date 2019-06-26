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


def compute_scores(people, energies, lights, heatings):
    return {
        "spendings": spendings(energies),
        "pollution": pollution(energies),
        "happiness": satisfaction(people, lights, heatings)
    }


def pollution(energies):
    score = (energies.pollution_factors * energies.amounts).mean()
    return score


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
    return sum(map(lambda energy: energy.amount * energy.cost, energies))


if __name__ == '__main__':
    pass
