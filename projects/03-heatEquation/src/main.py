import matplotlib.pyplot as plt
import numpy as np
import scipy as sci

from Simulation import Simulation


def f(t, x):
    return x  # np.cos(x)


def showcase_solve_ivp():
    f = lambda t, x: .5 * x

    t_min = 0
    t_max = 10
    t_res = .5
    y0 = np.pi / 4

    t_eval = np.arange(t_min, t_max, t_res)

    result = sci.integrate.solve_ivp(f, t_span=(t_min, t_max), y0=np.array([y0]), t_eval=t_eval, vectorized=True)

    print(result)
    plt.plot(result.t, result.y[0], "o", label="integration results")
    plt.plot(result.t, y0 * np.exp(.5 * result.t), label="analytical solution")
    plt.legend()
    plt.show()


def showcase_laplacian_convolution_matrix():
    laplacian_1D = np.ones((3,))
    laplacian_1D[1] = -2

    print("1D Laplace Convolution Operator")
    print(laplacian_1D)

    quadratic_1D = np.arange(10) ** 2

    print("Dataset f_i = i**2")
    print(quadratic_1D)

    print("Second derivative of data (note the nonsensical boundary values")
    second_derivative_1D = sci.signal.convolve(quadratic_1D, laplacian_1D, mode='same')
    print(second_derivative_1D)
    print()

    laplacian_2D = np.zeros((3, 3))
    laplacian_2D[1, :] = 1
    laplacian_2D[:, 1] = 1
    laplacian_2D[1, 1] = -4

    print("2D Laplace Convolution Operator")
    print(laplacian_2D)

    gridpoints = np.arange(0, 10, 1)
    X, Y = np.meshgrid(gridpoints, gridpoints)
    quadratic_2D = X * X + 2 * Y * Y

    print("Dataset f_{i,j} = i**2 + 2*j**2")
    print(quadratic_2D)

    second_derivative_2D = sci.signal.convolve(quadratic_2D, laplacian_2D, mode='same')

    print("Second derivative of data (note the nonsensical boundary values")
    print(second_derivative_2D)


def simulation_1D():
    sim = Simulation()
    sim.set_t_max(100) \
        .set_t_res(.1) \
        .set_shape((500,)) \
        .set_alpha(5)

    initial_state = sim.get_initial_state()
    initial_state[200:300] = 1

    fixed = sim.get_fixed_gridpoints()
    fixed[200:250] = True

    sim.run()
    sim.show_plot()
    sim.show_plot_final_state()

def simulation_2D():
    size_x = 100
    size_y = 100

    sim = Simulation()
    sim.set_t_max(50) \
        .set_t_res(.05) \
        .set_shape((size_x, size_y)) \
        .set_alpha(5)

    # set up a central hot disk
    Y, X = np.indices((size_x, size_y))     # sic: Y, X = ...(x, y)
    mask_circle = ((X - size_x//2) ** 2 + (Y - size_y//2)**2) < (min(size_x, size_y) // 4)**2
    initial_state = sim.get_initial_state()
    initial_state[mask_circle] = 1

    # set up a semicircle as fixed temperature points
    mask_semicircle = mask_circle.copy()
    mask_semicircle[:size_y//2, :] = 0
    fixed = sim.get_fixed_gridpoints()
    fixed[mask_semicircle] = True

    sim.run()
    sim.show_plot_final_state()

if __name__ == '__main__':
    showcase_solve_ivp()
    showcase_laplacian_convolution_matrix()

    simulation_1D()
    simulation_2D()
