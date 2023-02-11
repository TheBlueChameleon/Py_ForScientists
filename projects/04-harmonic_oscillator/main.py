import matplotlib.pyplot as plt
import numpy as np
import scipy as sci


# ==================================================================================================================== #

def first_order_ODE_independent_variable():
    print("# y' = alpha * t")

    y_0 = 1
    alpha = -0.2
    f_prime = lambda t, y: alpha * t

    t_min = 0
    t_max = 10
    t_eval = np.linspace(0, 10, 50)

    result = sci.integrate.solve_ivp(f_prime, [t_min, t_max], [y_0])
    # alternative form: use this to get more data points from the solver
    # result = sci.integrate.solve_ivp(f_prime, [t_min, t_max], [y_0], t_eval=t_eval)

    print(result)
    plt.title("Solution to $f'(t) = -\\alpha t$")
    plt.plot(result.t, result.y[0], "o", label="numerical result")

    t_analytic = np.linspace(t_min, t_max, 50)
    y_analytic = y_0 + 0.5 * alpha * t_analytic ** 2

    plt.xlabel("t")
    plt.ylabel("y = f(t)")
    plt.plot(t_analytic, y_analytic, label="analytic result")

    plt.legend()
    plt.show()


def first_order_ODE_state_variable():
    print("# y' = alpha * y")

    y_0 = 1
    alpha = -0.2
    f_prime = lambda t, y: alpha * y

    t_min = 0
    t_max = 10

    result = sci.integrate.solve_ivp(f_prime, [t_min, t_max], [y_0])
    print(result)

    plt.title("Solution to $f'(t) = -\\alpha f(t)$")
    plt.plot(result.t, result.y[0], "o", label="numerical result")

    t_analytic = np.linspace(t_min, t_max, 50)
    y_analytic = np.exp(alpha * t_analytic)

    plt.xlabel("t")
    plt.ylabel("y = f(t)")
    plt.plot(t_analytic, y_analytic, label="analytic result")

    plt.legend()
    plt.show()


def first_order_ODE_mixed():
    print("# y' = alpha * y * t")

    y_0 = 1
    alpha = -0.2
    f_prime = lambda t, y: alpha * t * y

    t_min = 0
    t_max = 10
    times = np.linspace(t_min, t_max, 51)

    result = sci.integrate.solve_ivp(f_prime, [t_min, t_max], [1], t_eval=times)
    print(result)

    positions = result.y[0]
    analytic_y = y_0 * np.exp(alpha * times ** 2 * 0.5)

    plt.figure(figsize=(16, 8))
    plt.suptitle(r"$f'(t) = -\alpha \cdot f(t) \cdot t$")

    ax1 = plt.subplot(121)
    ax1.set_xlabel("t")
    ax1.set_ylabel("f(x, t)")
    ax1.set_title("Flat Projection of the Solution")
    ax1.plot(times, positions, "o", label="numerical result")
    ax1.plot(times, analytic_y, "-", label="analytical result")
    ax1.legend()

    ax2 = plt.subplot(122, projection="3d")
    ax2.set_xlabel("t")
    ax2.set_ylabel("x")
    ax2.set_zlabel("f(x, t)")
    ax2.set_title("Time Resolved Projection")

    ax2.plot(times, positions, positions)

    plt.show()


# -------------------------------------------------------------------------------------------------------------------- #

def second_order_ODE():
    print("# y'' = cos(t)")
    y_0 = -1
    v_0 = +0
    f_prime = lambda t, y: (y[-1], np.cos(t))

    t_min = 0
    t_max = 10
    times = np.linspace(t_min, t_max, 51)

    result = sci.integrate.solve_ivp(f_prime, [t_min, t_max], [y_0, v_0], t_eval=times)
    print(result)

    positions = result.y[0, :]
    velocities = result.y[1, :]

    plt.title("$y''(t) = cos(t)$")
    plt.plot(times, positions, label="y(t): positions")
    plt.plot(times, velocities, label="y'(t): velocities")
    plt.legend()

    plt.show()


def driven_dampened_harmonic_oscillator_1D():
    print("# m*y''(t) + b*y'(t) + k*y(t) = A * sin(omega*t)")

    mass = 1.0
    dampening = 0.5
    spring_constant = 4.0
    omega = 1.5
    amplitude = .5

    driver_func = lambda t : -amplitude * np.sin(omega * t)

    y_0 = 0
    v_0 = 1

    def f_prime(t, y):
        # m*y''(t) + b*y'(t) + k*y(t) = A * sin(omega*t)
        # y'' = (1/m) * (A*sin(omega*t) - b*y' - k*y)

        velocity = y[-1]
        position = y[0]

        return (
            velocity, (1 / mass) * (driver_func(t) - dampening * velocity - spring_constant * position))

    t_min = 0
    t_max = 20
    t_N = 201
    times = np.linspace(t_min, t_max, t_N)

    result = sci.integrate.solve_ivp(f_prime, [t_min, t_max], [y_0, v_0], t_eval=times)
    print(result)

    positions = result.y[0, :]
    velocities = result.y[1, :]
    driver = driver_func(times)

    plt.plot(times, positions, label="positions")
    plt.plot(times, velocities, "--", label="velocities")
    plt.plot(times, driver, label="driver")
    plt.title("driven dampened harmonic oscillator".title())
    plt.legend()

    plt.show()


# -------------------------------------------------------------------------------------------------------------------- #

def orbit():
    m_sun = 10
    r_planet = [1., 0.]
    v_planet = [0., .1]
    G = 1e-3

    def f_prime(t, y):
        # F = G * m_1 * m_2 / r**2
        # a = F/m
        # => a = G * m_1 * / r**2
        # but the acceleration points toward the center, so, we get a scalar distance factor of:
        # -G / r**3
        # which is then multiplied with the current position.

        position = y[:2]
        distance_factor = np.sum(position ** 2) ** (3 / 2)
        accelereation = -(G * m_sun / distance_factor) * position

        result = np.roll(y, -2)
        result[2:] = accelereation

        return result

    t_min = 0
    t_max = 100
    t_N = 1001
    times = np.linspace(t_min, t_max, t_N)

    result = sci.integrate.solve_ivp(f_prime, [t_min, t_max], [*r_planet, *v_planet], t_eval=times)
    print(result)

    positions = result.y[:2]
    velocities = result.y[2:]

    distances = np.sqrt(np.sum(positions ** 2, axis=0))
    speeds = np.sqrt(np.sum(velocities ** 2, axis=0))

    potential_energies = -G * m_sun / distances
    kinetic_energies = .5 * speeds
    total_energies = potential_energies + kinetic_energies

    fig, axs = plt.subplots(1, 2)

    fig.set_size_inches(16, 8)
    fig.suptitle("Orbit (naive integrator)")

    axs[0].set_title("Trajectory")
    axs[0].plot(positions[0], positions[1])
    axs[0].plot([0], [0], "ro")

    axs[1].set_title("Energies")
    axs[1].set_xlabel("time")
    axs[1].set_ylabel("energy per unit mass")
    axs[1].plot(times, potential_energies, label="potential energy")
    axs[1].plot(times, kinetic_energies, label="kinetic energy")
    axs[1].plot(times, total_energies, label="total energy")
    axs[1].legend()

    plt.show()


def orbit_RK23():
    m_sun = 10
    r_planet = [1., 0.]
    v_planet = [0., .1]
    G = 1e-3

    def f_prime(t, y):
        # F = G * m_1 * m_2 / r**2
        # a = F/m
        # => a = G * m_1 * / r**2
        # but the acceleration points toward the center, so, we get a scalar distance factor of:
        # -G / r**3
        # which is then multiplied with the current position.

        position = y[:2]
        distance_factor = np.sum(position ** 2) ** (3 / 2)
        accelereation = -(G * m_sun / distance_factor) * position

        result = np.roll(y, -2)
        result[2:] = accelereation

        return result

    t_min = 0
    t_max = 100
    t_N = 1001
    times = np.linspace(t_min, t_max, t_N)

    result = sci.integrate.solve_ivp(f_prime, [t_min, t_max], [*r_planet, *v_planet], t_eval=times, method='RK23')
    print(result)

    positions = result.y[:2]
    velocities = result.y[2:]

    distances = np.sqrt(np.sum(positions ** 2, axis=0))
    speeds = np.sqrt(np.sum(velocities ** 2, axis=0))

    potential_energies = -G * m_sun / distances
    kinetic_energies = .5 * speeds
    total_energies = potential_energies + kinetic_energies

    fig, axs = plt.subplots(1, 2)

    fig.set_size_inches(16, 8)
    fig.suptitle("Orbit (naive integrator)")

    axs[0].set_title("Trajectory")
    axs[0].plot(positions[0], positions[1])
    axs[0].plot([0], [0], "ro")

    axs[1].set_title("Energies")
    axs[1].set_xlabel("time")
    axs[1].set_ylabel("energy per unit mass")
    axs[1].plot(times, potential_energies, label="potential energy")
    axs[1].plot(times, kinetic_energies, label="kinetic energy")
    axs[1].plot(times, total_energies, label="total energy")
    axs[1].legend()

    plt.show()


# ==================================================================================================================== #

if __name__ == '__main__':
    # first_order_ODE_independent_variable()
    # first_order_ODE_state_variable()
    # first_order_ODE_mixed()
    # second_order_ODE()
    driven_dampened_harmonic_oscillator_1D()
    # orbit()
    # orbit_RK23()
