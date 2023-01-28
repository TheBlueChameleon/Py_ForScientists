import copy

import numpy as np


class Particle:
    N_dimensions = 2
    N_columns = 2 * N_dimensions + 1  # position, velocity, mass
    default_mass = 1.0
    inner_type = np.float64

    # ---------------------------------------------------------------------------------------------------------------- #

    def __init__(self, position=None, velocity=None, mass=None):
        self.data = np.zeros(shape=(self.N_columns,), dtype=self.inner_type)

        if not position is None:
            self["position"] = self._handle_vector(position, "position")
        if not velocity is None:
            self["velocity"] = self._handle_vector(velocity, "velocity")

        if mass is None:
            self.set_mass(self.default_mass)
        else:
            try:
                self.data[-1] = float(mass)
            except ValueError:
                raise TypeError(f"mass is not a number value! Got {mass}")

    def _handle_vector(self, vector, description):
        try:
            result = np.array(vector, dtype=self.inner_type)
            length = result.shape
        except ValueError:
            raise TypeError(f"{description} is not a vector-like object! Got {vector}")

        if length != (self.N_dimensions,):
            raise ValueError(f"{description} is not a {self.N_dimensions} dimensional vector! Got {vector}")

        return np.array(vector, dtype=self.inner_type)

    # ---------------------------------------------------------------------------------------------------------------- #

    def get_mass(self):
        return self.data[-1]

    def set_mass(self, mass):
        self.data[-1] = mass

    def get_position(self):
        return self.data[:self.N_dimensions]

    def set_position(self, position):
        self.data[:self.N_dimensions] = position

    def get_velocity(self):
        return self.data[self.N_dimensions:2 * self.N_dimensions]

    def set_velocity(self, velocity):
        self.data[self.N_dimensions:2 * self.N_dimensions] = velocity

    # ---------------------------------------------------------------------------------------------------------------- #

    def __getitem__(self, key):
        t = type(key)
        if t == int:
            return self.data[key]
        elif t == str:
            if key == "mass":
                return self.get_mass()
            elif key == "position":
                return self.get_position()
            elif key == "velocity":
                return self.get_velocity()

        raise KeyError(f"'{key}' is not a recognized property of class Particle")

    def __setitem__(self, key, value):
        t = type(key)
        if t == int:
            return self.data[key]
        elif t == str:
            if key == "mass":
                return self.set_mass(value)
            elif key == "position":
                return self.set_position(value)
            elif key == "velocity":
                return self.set_velocity(value)

        raise KeyError(f"'{key}' is not a recognized property of class Particle")

    # ---------------------------------------------------------------------------------------------------------------- #

    def __add__(self, other):
        # self._handle_typecheck(other) -- already called by +=
        result = copy.deepcopy(self)
        result += other
        return result

    def __iadd__(self, other):
        self._handle_typecheck(other)
        self.data[:-1] += other
        return self

    def _handle_typecheck(self, other):
        if type(other) != np.ndarray:
            raise TypeError("Addition is only defined with numpy ndarrays.")
        if other.shape != (2 * self.N_dimensions,):
            raise ValueError(f"operand has wrong dimension (got {other.shape}).")

    # ---------------------------------------------------------------------------------------------------------------- #

    def __str__(self):
        return f"Particle at {self.get_position()}, velocity = {self.get_velocity()}, mass = {self.get_mass()}"
