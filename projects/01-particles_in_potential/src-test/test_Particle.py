import unittest

import numpy as np

from Particle import Particle


class Particle_Test(unittest.TestCase):
    def test_init_empty(self):
        default_state = np.zeros(shape=Particle.N_columns)
        default_state[-1] = Particle.default_mass

        p = Particle()
        self.assertTrue(np.array_equal(p.data, default_state))

    def test_init_custom(self):
        position = (1, 2)
        velocity = (3, 4)
        mass = 5
        custom_state = np.array([*position, *velocity, mass], dtype=Particle.inner_type)
        p = Particle(position=position, velocity=velocity, mass=mass)

        self.assertTrue(np.array_equal(p.data, custom_state))

    def test_init_malformed(self):
        with self.assertRaises(TypeError):
            p = Particle(mass="string")

        with self.assertRaises(TypeError):
            p = Particle(position="string")

        with self.assertRaises(ValueError):
            p = Particle(position=(1, 2, 3))

    def test_getter(self):
        position = (1, 2)
        velocity = (3, 4)
        mass = 5
        p = Particle(position=position, velocity=velocity, mass=mass)

        self.assertTrue(np.array_equal(p["position"], position))
        self.assertTrue(np.array_equal(p["velocity"], velocity))
        self.assertEqual(p["mass"], mass)

    def test_addition(self):
        position = (1, 2)
        velocity = (3, 4)
        mass = 5
        p = Particle(position=position, velocity=velocity, mass=mass)

        valid = np.array([1, 2, 3, 4], dtype=Particle.inner_type)
        invalid = np.array([1, 2, 3, 4, 5])

        expected = 2 * valid
        expected.resize((5,))
        expected[-1] = 5

        actual = p + valid

        self.assertTrue(np.array_equal(actual.data, expected))

        with self.assertRaises(TypeError):
            p + "invalid"

        with self.assertRaises(ValueError):
            p + invalid
