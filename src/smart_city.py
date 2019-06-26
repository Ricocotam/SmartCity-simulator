""" This module contains all simulation functions for the entire city. Those
are called at each tick.
"""
from .scores import compute_scores


class SmartCity:
    def __init__(self, people, energies, lights, heatings):
        self.people = people
        self.energies = energies
        self.lights = lights
        self.heatings = heatings

    def step(self):
        scores = compute_scores(people=self.people, energies=self.energies,
                                lights=self.lights, heatings=self.heatings)
        self.energies_step()
        # self.lights_step()
        # self.heatings_step()
        return scores

    def energies_step(self):
        cost_factors = self.energies.sample_cost_factors()
        amount_factors = self.energies.sample_amount_factors()

        self.energies.costs *= cost_factors
        self.energies.amounts *= amount_factors

    def lights_step(self):
        pass

    def heatings_step(self):
        pass

    def light_up(self, lights_on):
        pass

    def heat_up(self, heats, temperatures):
        pass

    def buy_energies(self, energies, amounts):
        cost = self.energies.buy(amounts)
        return cost


if __name__ == '__main__':
    pass
