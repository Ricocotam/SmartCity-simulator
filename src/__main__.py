from .engine import Engine
from .factory import build_all
from .smart_city import SmartCity


def main():
    configs = {
        "energies": {
            "energies": [
                    {
                        "name": "Carbon",
                        "cost": 0.2,
                        "amount": 100,
                        "pollution_factor": 1,
                    },
                    {
                        "name": "Nuclear",
                        "cost": 0.5,
                        "amount": 40,
                        "pollution_factor": 0,
                    },
                    {
                        "name": "Renewable",
                        "cost": 1,
                        "amount": 10,
                        "pollution_factor": 0,
                    }
            ]
        },
        "people": {
            "nb_people": 500,
            "pollution_pref": {"distribution_name": "uniform", "low": 0., "high": 0.5},
            "nuclear_pref": {"distribution_name": "uniform", "low": 0.2, "high": 1.0},
            "lights_pref": {"distribution_name": "uniform", "low": 0., "high": 0.5},
            "heat_pref": {"distribution_name": "uniform", "low": 0.2, "high": 1.0},
            "interraction": "random"
        },
        "lights": {"nb_lights": 5_000},
        "heaters": {"nb_heaters": 800, "mean_temperature": 18, "std_temperature": 1}
    }

    data = build_all(configs)
    people, energies, lights, heaters = [data[k] for k in ["people", "energies", "lights", "heaters"]]
    smart_city = SmartCity(people=people, energies=energies,
                           lights=lights, heaters=heaters)
    engine = Engine(smart_city)
    engine.buy_energies(smart_city.energies.amounts / 2)
    engine.step()
    print(engine.scores, "\n", smart_city.energies)
    engine.buy_energies(smart_city.energies.amounts / 2)
    engine.step()
    print(engine.scores, "\n", smart_city.energies)


if __name__ == '__main__':
    main()
