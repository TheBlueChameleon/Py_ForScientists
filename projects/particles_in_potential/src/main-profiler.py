import cProfile

import numpy as np

from Constants import Constants
from Particle import Particle
from Potential import Potential
from Simulation import Simulation


def decaying_oscillation_potential(x, y):
    r = np.sqrt(x * x + y * y)
    mag = np.exp(-Constants.decay * (r * r))
    return 2 * mag * np.cos(Constants.frequency * r)

def setup_simulation():
    potential = Potential(decaying_oscillation_potential)

    sim = Simulation(potential)
    sim.set_dt(0.005)
    sim.set_t_max(10.0)

    sim.add_particle(
        Particle(position=(+0.90, +0.10),
                 velocity=(-0.10, +0.10),
                 mass=1)
    )
    sim.add_particle(
        Particle(position=(-0.90, +0.10),
                 velocity=(-0.10, +0.10),
                 mass=1)
    )

    return sim

def run_full():
    sim = setup_simulation()
    run_without_precompute(sim)
    run_with_precompute(sim)

def run_without_precompute(sim):
    sim.autorun()
    compact_table = sim.get_compact_table()
    # no showing the plot, since this adds the human component of "when do they click on close"
    # still, computing the table which is used to inform the plots

def run_with_precompute(sim):
    sim.potential.precompute(
        (-1.5, +1.5, .01),
        (-0.2, +1.2, .01)
    )
    sim.autorun()
    compact_table = sim.get_compact_table()
    # same rationale as before

if __name__ == '__main__':
    cProfile.run('run_full()', sort='tottime')