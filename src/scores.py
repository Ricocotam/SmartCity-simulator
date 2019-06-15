"""Score functions.

This module is used to compute different scores once the simulation is done.
"""

def compute_scores(people, energies, lights, heatings):
    spent = spendings(energies)
    pollutes = pollution(energies)
    satisfied = satisfaction(people, energies, lights, heatings)
    
    return {"spendings": spent,
            "pollution": pollutes,
            "happiness": satisfied}


def pollution(energies):
    score = (energies.pollution_factors * energies.amounts).mean()
    return score


def satisfaction(people, energies, lights, heatings):
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
    return sum(map(lambda e: e.amount * e.cost, energies))
