
def estimate_beta_parameters(means, stds, low, high):
    loc = low
    scale = high

    # print("\t\t BEFORE", means, stds)
    means = (means - loc) / scale
    variances = (stds / scale) ** 2
    # print("\t\t AFTER", means, stds / scale)

    temp = means * (1 - means) / variances - 1
    α = means * temp
    β = (1 - means) * temp

    print(f"""
        Estimation of Beta Parameters
            α = {α}
            β = {β}
            loc = {loc}
            scale = {scale}

        Computed using :
            means : {means}
            vars : {variances}
            loc : {loc}
            scale : {scale}
    """)

    return α, β, loc, scale


class BetaDistributions(object):
    def __init__(self, means, stds, low, high):
        self.alphas, self.betas, self.locs, self.scales = estimate_beta_parameters(means, stds, low, high)
        self.means = means
        self.stds = stds
        assert (self.alphas < 0).sum() == 0
        assert (self.betas < 0).sum() == 0

    def __iter__(self):
        return iter((self.alphas, self.betas, self.means, self.stds))
