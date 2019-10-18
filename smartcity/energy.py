import numpy as np

from . import scores


class Energies:
    def __init__(self, initial_costs, initial_amounts, pollution_factors,
                 new_cost, new_amount):
        self.costs = initial_costs
        self.amounts = initial_amounts
        self.pollution_factors = pollution_factors

        self.bought_amounts = np.zeros_like(self.amounts)

        self.new_cost = new_cost
        self.new_amount = new_amount

    def __str__(self):
        return f"Energies :\n\tcosts {self.costs}\n\tamounts {self.amounts}\n\tpollution {self.pollution_factors}"

    def buy(self, amounts):
        assert all(map(lambda e, a: e >= a, self.amounts, amounts))

        self.bought_amounts = amounts
        return scores.spendings(self), amounts.sum()

    def to_json(self):
        pass
