""" Simulation functions.

This module contains all simulation functions for the entire city.
Those are called at each tick with the previous one.
"""
from scores import compute_scores


class Simulator:
    def __init__(self, energies, transports, lights, heatings, people):
        self.energies = energies
        self.transports = transports
        self.lights = lights
        self.heatings = heatings
        self.people = people

    def step(self):
        scores = compute_scores(self.people, self.energies, self.lights, self.heatings)
        # self.lights_step()
        # self.heatings_step()
        self.energies_step()
        # self.transports_step()
        return scores

    def lights_step(self):
        pass

    def heatings_step(self):
        pass

    def energies_step(self):
        cost_factors = self.energies.sample_cost_factors()
        amount_factors = self.energies.sample_amount_factors()

        self.energies.costs *= cost_factors
        self.energies.amounts *= amount_factors

    def transports_step(self):
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
