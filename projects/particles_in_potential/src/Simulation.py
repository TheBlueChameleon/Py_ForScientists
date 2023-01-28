import numpy as np
from matplotlib import pyplot as plt

from Particle import Particle
from Potential import Potential
from State import State


class Simulation:
    def __init__(self, potential, particles=None, t_max=None, dt=None):
        if not type(potential) == Potential:
            raise TypeError(f"{potential} is not a Potential!")

        if particles is None:
            pass
        else:
            error = False
            if type(particles) == Particle:
                particles = [particles]
            elif type(particles) == list:
                error = any(type(particle) != Particle for particle in particles)

            if error:
                raise TypeError("particles must be of type list<Particle>!")

        self.potential = potential
        self.current_state = State(self.potential, particles)

        self.t = 0.
        self.dt = dt
        self.t_max = t_max

        self.timeline = [self.current_state]
        self.timestamps = [self.t]

    # ---------------------------------------------------------------------------------------------------------------- #

    def set_t_max(self, t_max):
        self.t_max = t_max

    def set_dt(self, dt):
        self.dt = dt

    def set_potential(self, new_potential):
        self.potential = new_potential
        self.current_state.potential = new_potential

    def add_particle(self, new_particle):
        if len(self.timeline) > 1:
            raise RuntimeError("Cannot change particle count in running simulation")
        else:
            self.current_state.add_particle(new_particle)

    def reset(self):
        self.t = 0.
        self.timestamps = [self.t]

        self.timeline = [self.timeline[0]]
        self.current_state = self.timeline[0]

    # ---------------------------------------------------------------------------------------------------------------- #

    def _is_ready(self):
        try:
            float(self.dt)
            float(self.t_max)
        except TypeError:
            return False

        return True

    def advance(self):
        if self._is_ready():
            self.timeline.append(self.current_state.copy().evolve(self.dt))
            self.current_state = self.timeline[-1]
            self.t += self.dt
            self.timestamps.append(self.t)
        else:
            raise RuntimeError("Not all required parameters have been defined")

    def autorun(self):
        while self.t < self.t_max:
            self.advance()

    # ---------------------------------------------------------------------------------------------------------------- #

    def get_compact_table(self):
        n_timesteps = len(self.timeline)
        n_columns, n_particles = self.timeline[-1].get_compact_table_size()
        result = np.zeros(shape=(n_timesteps, n_columns, n_particles))

        for i, state in enumerate(self.timeline):
            result[i] = state.get_compact_table()

        result = np.insert(result, 0, None, axis=2)

        for i, t in enumerate(self.timestamps):
            result[i, :, 0] = t
        return result

    # ---------------------------------------------------------------------------------------------------------------- #

    def show_plot(self):
        if Particle.N_dimensions != 2:
            raise RuntimeError("Plotting only in 2D available.")

        fig, axs = plt.subplots(2, 2)
        fig.set_size_inches(12, 10)

        tab = self.get_compact_table()

        column_x = 1
        column_y = 2
        if not self.potential.discrete:
            x_max = tab[:, :, column_x].max()
            x_min = tab[:, :, column_x].min()
            x_res = (x_max - x_min) / 100

            y_max = tab[:, :, column_y].max()
            y_min = tab[:, :, column_y].min()
            y_res = (y_max - y_min) / 100

            self.potential.precompute(
                (x_min, x_max, x_res),
                (y_min, y_max, y_res)
            )
            self.potential.discrete = False

        ax = axs[0, 0]
        ax.set_title("Potential Landscape")
        self.potential.draw_potential_on(ax)
        fig.colorbar(ax.collections[0])
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        ax = axs[0, 1]
        ax.set_title("Force Field")
        self.potential.draw_force_on(ax)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        ax = axs[1, 0]
        ax.set_title("Trajectory")
        self.draw_trajectory_on(tab, ax)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        ax = axs[1, 1]
        ax.set_title("Speed vs. Time")
        ax.set_xlabel("time")
        ax.set_ylabel("speed")
        self.draw_speed_on(tab, ax)

        plt.show()

    def draw_trajectory_on(self, tab, ax):
        N_timesteps, N_particles, N_columns = tab.shape
        column_x = 1
        column_y = 2

        for particle_id in range(N_particles):
            xs = tab[:, particle_id, column_x]
            ys = tab[:, particle_id, column_y]

            ax.plot(xs, ys)

    def draw_speed_on(self, tab, ax):
        N_timesteps, N_particles, N_columns = tab.shape
        column_t = 0
        column_vx = 4
        column_vy = 4

        speed = lambda partice_id: np.sqrt(tab[:, particle_id, column_vx] ** 2 + tab[:, particle_id, column_vy] ** 2)

        for particle_id in range(N_particles):
            times = tab[:, particle_id, column_t]
            speeds = speed(particle_id)

            ax.plot(times, speeds)
