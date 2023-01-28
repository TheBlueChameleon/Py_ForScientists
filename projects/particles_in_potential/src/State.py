import copy

import numpy as np

from Particle import Particle
from Potential import Potential


class State:
    def __init__(self, potential: Potential, particles: list = None):
        self.potential = potential
        self.particles = (particles if particles else [])

    # ---------------------------------------------------------------------------------------------------------------- #

    def add_particle(self, particle: Particle):
        self.particles.append(particle)

    def evolve(self, dt: float):
        if self.potential.discrete:
            get_force = self.potential.get_force_near
        else:
            get_force = self.potential.get_force_at

        for particle in self.particles:
            position = particle.get_position()
            velocity = particle.get_velocity()

            force = get_force(position)
            acceleration = force / particle.get_mass()

            delta = np.concatenate((velocity, acceleration)) * dt
            particle += delta

        return self

    # ---------------------------------------------------------------------------------------------------------------- #

    def copy(self):
        return self.__copy__()

    def __copy__(self):
        result = State(self.potential)
        for particle in self.particles:
            result.add_particle(copy.deepcopy(particle))

        return result

    # ---------------------------------------------------------------------------------------------------------------- #

    def get_compact_table(self):
        result = np.zeros(shape=self.get_compact_table_size())
        for i, particle in enumerate(self.particles):
            result[i] = particle.data
        return result

    def get_compact_table_size(self):
        N_particles = len(self.particles)
        return (N_particles, Particle.N_columns)