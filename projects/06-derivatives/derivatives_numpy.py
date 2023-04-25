import matplotlib.pyplot as plt
import numpy as np

# ==================================================================================================================== #

c = 0.02  # use this to control oscillation. Lower value means faster oscillation.
f = lambda x: np.sin(1 / (x * x + c))
df = lambda x: -2 * x * np.cos(1 / (x * x + c)) / ((x * x + c) ** 2)

epsilon = 1e-4
X = np.arange(0, 1, epsilon)
Y_f = f(X)
Y_df = df(X)


# ==================================================================================================================== #

def showcase_1D_derivative():
    numerical_derivative = np.gradient(Y_f, X)
    numerical_error = np.abs(numerical_derivative - Y_df)

    fig, axs = plt.subplots(2, 1)
    fig.set_size_inches(8, 16)

    axs[0].set_title(f"Analytic derivative vs. numpy derivative")
    axs[0].plot(X, Y_df, label="analytic")
    axs[0].plot(X, numerical_derivative, label="numpy result")
    axs[0].legend()

    axs[1].set_title(f"Error of numpy derivative")
    axs[1].plot(X, numerical_error, label="numpy result")

    plt.show()


def showcase_2D_scalarfield_derivative():
    epsilon = 0.05
    rng = np.arange(-1.0, 1.0 + epsilon, epsilon)
    X, Y = np.meshgrid(rng, rng, indexing='ij')
    R = np.sqrt(X ** 2 + Y ** 2)
    F = np.exp(-R) * np.cos(10 * R)

    # uniform spacing of datapoints: just pass stride parameter 'epsilon'
    dFx, dFy = np.gradient(F, epsilon)

    # you can also pass an array and the axis along which to take the derivative
    # dFx = np.gradient(F, rng, axis=0)
    # dFy = np.gradient(F, rng, axis=1)

    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(16, 8)

    axs[0].set_title("f(x, y)")
    axs[0].pcolor(X, Y, F)

    axs[1].set_title("grad f(x, y)")
    axs[1].quiver(X, Y, dFx, dFy)

    plt.show()


def showcase_vectorfield_derivative():
    epsilon = 1e-1
    angles = np.arange(0, 3 * np.pi, epsilon)

    data = np.stack((np.cos(angles), np.sin(angles)))
    derivative = np.gradient(data, epsilon, axis=1)

    # just to make the plot look nicer, we will show the derivative arrows a bit smaller than the rest
    rescaled = derivative * 0.5

    fig, axs = plt.subplots(1, 1, subplot_kw={'projection': '3d'})
    fig.set_size_inches(8, 8)

    selector_quiver = slice(None, None, 5)
    zeros = np.zeros(angles[selector_quiver].size)
    ones = epsilon * np.ones(zeros.size) * selector_quiver.step

    axs.plot(angles[selector_quiver], zeros, zeros, "black", linewidth=.5)

    axs.plot(angles, data[0], data[1], "black", linewidth=1)
    axs.quiver(angles[selector_quiver], zeros, zeros,
               zeros, data[0, selector_quiver], data[1, selector_quiver],
               color="black", arrow_length_ratio=0.1)

    axs.quiver(angles[selector_quiver], data[0, selector_quiver], data[1, selector_quiver],
               ones, rescaled[0, selector_quiver], rescaled[1, selector_quiver],
               color="red", arrow_length_ratio=0.1)


    axs.set_title("Vector function and derivative")

    plt.show()

    print(data.shape)


# ==================================================================================================================== #

if __name__ == '__main__':
    # showcase_1D_derivative()
    showcase_2D_scalarfield_derivative()
    # showcase_vectorfield_derivative()
