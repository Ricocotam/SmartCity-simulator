class Energies:
    def __init__(self, initial_costs, initial_amounts, pollution_factors,
                 sampler_cost_factors, sampler_amount_factors):
        self.costs = initial_costs
        self.amounts = initial_amounts
        self.pollution_factors = pollution_factors

        self.sampler_cost_factors = sampler_cost_factors
        self.sampler_amount_factors = sampler_amount_factors

    def __str__(self):
        pass

    def buy(self, amounts):
        assert all(map(lambda e, a: e >= a, zip(self.amounts, amounts)))

        self.amounts -= amounts

    def to_json(self):
        pass


def identity_sample(x):
    return x

if __name__ == '__main__':
    pass
