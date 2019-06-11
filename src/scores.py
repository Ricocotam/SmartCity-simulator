"""Score functions.

This module is used to compute different scores once the simulation is done.
"""
import torch

def pollution(energies):
    score = 0
    total_quantity = 0
    for energy in energies:
        total_quantity += energy.quantity
        score += energy.pollution_factor * energy.quantity
    score /= total_quantity

    return score


def satisfaction(citizens,  # shape : nb_citizens, nb_opinions , mean, std
                 preferences,  # shape : nb_citizens, nb_opinions
                ):
    return 1
    """
    # shape : nb_citizens, nb_opinions
    #log_probas = ...
    
    scaled = log_probas * preferences
    citizen_satisfaction = scaled.sum(1)
    city_satisfaction = citizen_satisfaction.sum()

    return city_satisfaction
    """


def spendings(energies):
    return sum(map(lambda e: e.amount, energies))
