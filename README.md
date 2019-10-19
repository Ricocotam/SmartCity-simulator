# SmartCity-simulator
Smart City Simulator designed for hackathons !

## Package installation
`pip3 install --user smartcity`

Python > 3.7

## Env Instantiation
In the package, 3 envs are available :

- SmartCity-v0 : small env
- SmartCity-v1 : medium env
- SmartCity-v2 : big env

```python
import smartcity
import gym

env = gym.make("SmartCity-v0")

obs, info = env.reset()
```

## Actions
To send action, you have to send a dictionnary instead of the usual vectors. There's 3 keys to send : energies, heaters and lights. Energies defines how much of each type of energy you buy. Lights define whether each light is on or off (a threshold at 0.5 is set). Heaters define the temperature of each heater. To have the size and the type of each parameter, they are available in the `obs` variable. `obs` is a dictionnary you can use to predict your actions. Keys `lights`, `heaters` and `energies_amount` have the exact format requested for actions, you can just copy them.

## Observations and informations
There's 5 keys in the obs dictionnary :

- `lights` : numpy array of size #light. Each light is either 0 (off) or 1 (on)
- `heaters` : numpy array of size #heater. Each heater is defined by its temperature
- `energies_cost` : cost of each quantity. This cost is defined for each point of each energy
- `energies_amount` : available amount for energy
- `needed_energy` : the total amount of energy needed. If you don't send enough energy, an exception is raised. During Hackathon submission, it will be an elimination criteria. If you buy more energy that needed, it is stored indefinitely so you can use it.

There's 2 keys in `info` dictionnary :

- `light_interraction` : a matrix of shape (#people, #lights). If there's a 1 at `[i, j]`, the citizen `i` is connected to light `light`
- `heaters_interraction` : same as lights but for heaters