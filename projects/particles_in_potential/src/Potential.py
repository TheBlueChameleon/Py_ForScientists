import matplotlib.pyplot as plt
import numpy as np

from Misc import Misc
from Particle import Particle


class Potential:
    def __init__(self, expression, epsilon=1e-6):
        self.expression_potential = self._handle_expression_potential(expression)
        self.expression_force = self._handle_expression_force()
        self.epsilon = epsilon

        self.discrete = False
        self.grid_points = None
        self.grid = None
        self.field_potential = None
        self.field_force = None

    def _handle_expression_potential(self, expression):
        if not callable(expression):
            raise TypeError(f"Expression '{self.expression_potential}' is not callable")

        number_of_arguments = expression.__code__.co_argcount
        if not (number_of_arguments == Particle.N_dimensions):
            raise ValueError(
                f"Invalid number of arguments: 'expression' requires {number_of_arguments} (expected: {Particle.N_dimensions})")

        return expression

    def _handle_expression_force(self):
        """
        Takes self.expression_potential and generates a function to compute the partial derivatives wrt. all axes.

        :return: a function computing the partial derivatives wrt. all axes
        """

        def inner(*coordinates):
            funcs = [Misc.bind_all_parameters_but_ith(self.expression_potential, i, coordinates)
                     for i in range(Particle.N_dimensions)]

            deltas = [-Misc.central_difference_quotient(func, x, self.epsilon)
                      for func, x in zip(funcs, coordinates)]

            return np.array(deltas)

        return inner

    # ---------------------------------------------------------------------------------------------------------------- #

    def precompute(self, *args):
        """
        Takes a resolution description in N dimensions and precomputes field and force with these settings.
        This method changes attributes grid, grid_points, field_potential, field_force and discrete accordingly.

        :param args: a set of N tuples of (min, max, resolution), where N is the number of spatial dimensions for the
            simulation.
            Example:
            potential.precompute( (-1, +1, 0.1), (-1, +1, 0.1) )
            prepares a grid of 20x20 points, ranging from -1 to +1 (excluded) in both, x and y direction.

        :return: None
        """
        descriptor = self._handle_size_and_resolution(args)

        self.grid_points = [np.arange(*axis) for axis in descriptor]
        self.grid = np.meshgrid(*self.grid_points, indexing='ij')

        self.field_potential = self.expression_potential(*self.grid)

        list_of_forces = self.expression_force(*self.grid)
        self.field_force = np.stack(tuple(list_of_forces))

        self.discrete = True

    def _handle_size_and_resolution(self, descriptor):
        correct = True
        expected_shape = (Particle.N_dimensions, 3)

        try:
            type_checked = np.array(descriptor, dtype=Particle.inner_type)
        except ValueError:
            correct = False

        if type_checked.shape != expected_shape:
            correct = False

        if correct:
            return type_checked
        else:
            raise ValueError(f"Expected: array-like structure of shape {expected_shape}. Got: {descriptor}")

    def clear_precomputed(self):
        self.grid_points = None
        self.grid = None

        self.field_potential = None
        self.field_force = None

        self.discrete = False

    # ================================================================================================================ #
    # field access helper

    def get_nearest_indices(self, coordinates):
        result = tuple(
            np.abs(grid_points - coordinate).argmin()
            for coordinate, grid_points in zip(coordinates, self.grid_points)
        )
        return result

    # ---------------------------------------------------------------------------------------------------------------- #
    # access to potential field

    def __getitem__(self, key):
        return self.expression_potential(*key)

    def get_expression_potential(self):
        return self.expression_potential

    def get_field_potential(self):
        return self.field_potential

    def get_potential_at(self, coordinates):
        return self.expression_potential(*coordinates)

    def get_potential_near(self, coordinates):
        nearest_indices = self.get_nearest_indices(coordinates)
        return self.field_potential[nearest_indices]

    # ---------------------------------------------------------------------------------------------------------------- #
    # access to force field

    def get_expression_force(self):
        return self.expression_force

    def get_field_force(self):
        return self.field_force

    def get_force_at(self, coordinate):
        return self.expression_force(*coordinate)

    def get_force_near(self, coordinate):
        nearest_indices = self.get_nearest_indices(coordinate)
        idx = (slice(None), *nearest_indices)
        return self.field_force[idx]

    # ================================================================================================================ #

    def show_plot(self):
        if Particle.N_dimensions == 2:
            fig, axs = plt.subplots(1, 2)
            fig.set_size_inches(12, 5)

            axs[0].set_title("Potential Landscape")
            self.draw_potential_on(axs[0])
            fig.colorbar(axs[0].collections[0])

            axs[1].set_title("Force Field")
            self.draw_force_on(axs[1])

            plt.show()
        else:
            raise RuntimeError("Plotting only in 2D available.")

    def draw_potential_on(self, axis_object):
        X, Y = self.grid
        axis_object.pcolor(X, Y, self.field_potential)

    def draw_force_on(self, axis_object):
        X, Y = self.grid
        U, V = self.field_force
        axis_object.quiver(X, Y, U, V)
