import time

import numpy as np

from Constants import Constants
from Particle import Particle
from Potential import Potential
from Simulation import Simulation


def decaying_oscillation_potential(x, y):
    r = np.sqrt(x * x + y * y)
    mag = np.exp(-Constants.DECAY * (r * r))
    return 2 * mag * np.cos(Constants.FREQUENCY * r)

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

if __name__ == '__main__':
    print("Running simulation... this might take some time.")

    tic = time.perf_counter()
    sim = setup_simulation()
    toc = time.perf_counter()
    t_setup = (toc - tic) * 1000

    tic = time.perf_counter()
    sim.autorun()
    toc = time.perf_counter()
    t_full_resolution = (toc - tic) * 1000

    sim.show_plot()
    sim.reset()

    tic = time.perf_counter()
    sim.potential.precompute(
        (-1.5, +1.5, .01),
        (-0.2, +1.2, .01)
    )
    toc = time.perf_counter()
    t_precompute = (toc - tic) * 1000

    tic = time.perf_counter()
    sim.autorun()
    toc = time.perf_counter()
    t_preset_resolution = (toc - tic) * 1000

    sim.show_plot()

    print("TIME REQUIREMENTS:")
    print(f"setup                 : {t_setup:6.2f} ms")
    print(f"full resolution run   : {t_full_resolution:6.2f} ms")
    print(f"precomputing potential: {t_precompute:6.2f} ms")
    print(f"precomputed run       : {t_preset_resolution:6.2f} ms")
    print(f"precomputed total     : {t_precompute + t_preset_resolution:6.2f} ms")
