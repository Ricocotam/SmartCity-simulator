"""Any entity is defined here.

This module defines citizens, city, ... objects.
"""

class Energies:
    
    def __init__(self, initial_costs, initial_amounts, pollution_factors, 
                       sampler_cost_factors, sampler_amount_factors):
        self.costs = initial_costs
        self.amounts = initial_amounts
        self.pollution_factors = pollution_factors

        self.sampler_cost_factors = sampler_cost_factors
        self.sampler_amount_factors = sampler_amount_factors

    def buy(self, amounts):
        assert all(map(lambda e, a: e >= a, 
                zip(self.amounts, amounts)
            ))
        self.amounts -= amounts

    def __str__(self):
        pass
    
    def json(self):
        pass


class Lights:
    def __init__(self):
        pass

    def __str__(self):
        pass
    
    def json(self):
        pass


class Heaters:
    def __init__(self):
        pass

    def __str__(self):
        pass
    
    def json(self):
        pass
