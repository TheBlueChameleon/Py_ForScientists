import time

import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as sla

# ==================================================================================================================== #

resolutions = [10, 100, 500]
max_excitation = 4


# ==================================================================================================================== #

def minimal_fail():
    resolution = 200

    principal_diagonal = -2 * np.ones(resolution, dtype=np.float64)
    secondary_diagonal = +1 * np.ones(resolution - 1, dtype=np.float64)
    matrix = np.diag(principal_diagonal) + \
             np.diag(secondary_diagonal, -1) + \
             np.diag(secondary_diagonal, +1)

    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    # eigenvalues, eigenvectors = sla.eigh_tridiagonal(principal_diagonal, secondary_diagonal)

    xs = np.linspace(0, 2 * np.pi, resolution)
    for excitation in range(4):
        plt.plot(xs, eigenvectors.T[excitation], lw=1, label=f"excitation #{excitation}")
    plt.legend(loc="lower left")
    plt.show()


def minimal_success():
    resolution = 200

    principal_diagonal = -2 * np.ones(resolution, dtype=np.float64)
    secondary_diagonal = +1 * np.ones(resolution - 1, dtype=np.float64)
    matrix = np.diag(principal_diagonal) + \
             np.diag(secondary_diagonal, -1) + \
             np.diag(secondary_diagonal, +1)

    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    # eigenvalues, eigenvectors = sla.eigh_tridiagonal(principal_diagonal, secondary_diagonal)

    # the crucial part
    order = np.abs(eigenvalues).argsort()
    eigenvectors = eigenvectors[:, order]

    xs = np.linspace(0, 2 * np.pi, resolution)
    for excitation in range(4):
        plt.plot(xs, eigenvectors.T[excitation], lw=1, label=f"excitation #{excitation}")
    plt.legend(loc="lower left")
    plt.show()


# -------------------------------------------------------------------------------------------------------------------- #

def construct_operator_objects(resolution):
    principal_diagonal = -2 * np.ones(resolution, dtype=np.float64)
    secondary_diagonal = +1 * np.ones(resolution - 1, dtype=np.float64)

    prefactor_2pi = (resolution / (2 * np.pi)) ** 2

    matrix = np.diag(principal_diagonal) + np.diag(secondary_diagonal, -1) + np.diag(secondary_diagonal, +1)

    # uncomment these two for the forward/backward declaration in the first and last line
    matrix[+0, 0:3] = [1, -2, 1]
    matrix[-1, -3:] = [1, -2, 1]

    # uncomment these two for the cyclical boundary conditions
    # matrix[0, -1] = 1
    # matrix[-1, 0] = 1

    matrix *= prefactor_2pi

    return matrix, principal_diagonal, secondary_diagonal


def show_derivative_works(matrix, resolution, ax):
    sine = np.sin(np.linspace(0, 2 * np.pi, resolution))
    sine_two_prime = matrix @ sine
    expected = -sine

    xs = np.linspace(0, 2 * np.pi, resolution)

    ax.set_title(f"Differentiation by MatMul, res. = {resolution}")
    ax.plot(xs, sine, label="f(x)", linewidth=1)
    ax.plot(xs, expected, label="f''(x) (analytical)", color="green")
    ax.plot(xs, sine_two_prime, label="f''(x) (numerical)", color="red")
    ax.set_ylim(-1.1, 1.1)
    ax.legend(loc="lower left")


def show_eigencomputation_full_matrix(matrix, resolution, ax):
    tic = time.perf_counter()
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    toc = time.perf_counter()

    # sign of eigenvalue is not fixed.
    # Av = lambda v  => A(-v) = -lambda v
    # force all eigenvalues to be treated as positive and sort accordingly
    idxs = np.abs(eigenvalues).argsort()
    eigenvectors = eigenvectors[:, idxs]

    xs = np.linspace(0, 2 * np.pi, resolution)
    ax.set_title(f"Eigenvectors (eig), res. = {resolution}")
    for excitation in range(max_excitation):
        ax.plot(xs, eigenvectors.T[excitation], lw=1, label=f"excitation #{excitation}")
    ax.legend(loc="lower left")

    return toc - tic


def show_eigencomputation_tridiagonal_matrix(principal_diagonal, secondary_diagonal, resolution, ax):
    tic = time.perf_counter()
    eigenvalues, eigenvectors = sla.eigh_tridiagonal(principal_diagonal, secondary_diagonal)
    toc = time.perf_counter()

    # force sorting by absolute value of eigenvalue
    idxs = np.abs(eigenvalues).argsort()
    eigenvectors = eigenvectors[:, idxs]

    ax.set_title(f"Eigenvectors (tridiag), res. = {resolution}")
    xs = np.linspace(0, 2 * np.pi, resolution)
    for excitation in range(max_excitation):
        ax.plot(xs, eigenvectors.T[excitation], lw=1, label=f"excitation #{excitation}")
    ax.legend(loc="lower left")

    return toc - tic


def proof_of_concept():
    rows = len(resolutions)
    fig, axs = plt.subplots(rows, 3)
    fig.set_size_inches(12, rows * 4)
    fig.tight_layout(pad=5.0)

    times_full_matrix = np.zeros(rows)
    times_tridiagonal = np.zeros(rows)

    for row, resolution in enumerate(resolutions):
        print(f"computing data for resolution = {resolution} ...")
        matrix, principal_diagonal, secondary_diagonal = construct_operator_objects(resolution)
        show_derivative_works(matrix, resolution, axs[row, 0])
        times_full_matrix[row] = show_eigencomputation_full_matrix(matrix, resolution, axs[row, 1])
        times_tridiagonal[row] = show_eigencomputation_tridiagonal_matrix(principal_diagonal, secondary_diagonal,
                                                                          resolution, axs[row, 2])

    plt.show()

    fig, ax = plt.subplots(1, 1)
    ax.set_title("Runtime depending on resolution")
    ax.set_xlabel("Resolution")
    ax.set_ylabel("Runtime in s")
    ax.set_yscale('log')
    barchart_labels = [str(res) for res in resolutions]
    ax.bar(barchart_labels, times_full_matrix, label="full matrix")
    ax.bar(barchart_labels, times_tridiagonal, width=0.5, label="tridiagonal")

    ax.legend()
    plt.show()


# -------------------------------------------------------------------------------------------------------------------- #

def construct_schroedinger_operator(resolution):
    # potential term
    xs = np.linspace(-1, 1, resolution)
    V = lambda x: 100 * x ** 2
    vs = V(xs)

    # flipped sign of differential operator part, because -ħ²/2m d²/dx²
    principal_diagonal = +2 * np.ones(resolution, dtype=np.float64)
    secondary_diagonal = -1 * np.ones(resolution - 1, dtype=np.float64)

    # add rescaled potential term
    principal_diagonal += vs * resolution ** (-3 / 2)

    return principal_diagonal, secondary_diagonal, vs


def solve_and_plot_schroedinger(resolution, ax):
    principal_diagonal, secondary_diagonal, vs = construct_schroedinger_operator(resolution)
    print(vs)

    xs = np.linspace(-1, 1, resolution)

    eigenvalues, eigenvectors = sla.eigh_tridiagonal(principal_diagonal, secondary_diagonal)

    idxs = np.abs(eigenvalues).argsort()
    eigenvectors = eigenvectors[:, idxs]

    scale_factor_potential = vs[0]                  # first value is also maximum
    scale_factor_funcs = np.max(eigenvectors)       # usually excitation #0 at x=0

    ax.set_title(f"Resolution = {resolution}")
    ax.plot(xs, vs / scale_factor_potential, "k", label="potential")
    for i in range(4):
        ax.plot(xs, eigenvectors.T[i] / scale_factor_funcs, linewidth=1, label=f"excitation #{i}")
    ax.legend()


def run_schroedinger():
    columns = len(resolutions)
    fig, axs = plt.subplots(1, columns)
    fig.set_size_inches(columns * 6, 5)
    fig.tight_layout(pad=5.0)

    fig.suptitle("solutions to the Schrödinger equation with 1-dimensional harmonic potential".title())

    for i, res in enumerate(resolutions):
        solve_and_plot_schroedinger(res, axs[i])
    plt.show()


# ==================================================================================================================== #

if __name__ == '__main__':
    minimal_fail()
    minimal_success()
    proof_of_concept()
    run_schroedinger()

    # todo:
    #  accomodate potential (value) to produce equal results in form
    #  rescale PLOT of potential to cancel out value of potential
