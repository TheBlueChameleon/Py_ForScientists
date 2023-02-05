import matplotlib.pyplot as plt
import numpy as np

# ==================================================================================================================== #

c = 0.02  # use this to control oscillation. Lower value means faster oscillation.
f = lambda x: np.sin(1 / (x * x + c))
df = lambda x: -2 * x * np.cos(1 / (x * x + c)) / ((x * x + c) ** 2)

X = np.arange(0, 1, .001)
Y_f = f(X)
Y_df = df(X)


# ==================================================================================================================== #

def dv_forward(f, x, epsilon=1E-4):
    return (f(x + epsilon) - f(x)) / epsilon


def dv_backward(f, x, epsilon=1E-4):
    return (f(x) - f(x - epsilon)) / epsilon


def dv_central(f, x, epsilon=1E-4):
    return (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)


# ==================================================================================================================== #

def show_difference_methods():
    Y_dv_forward = dv_forward(f, X)
    Y_dv_backward = dv_backward(f, X)
    Y_dv_central = dv_central(f, X)

    Y_delta_forward = Y_df - Y_dv_forward
    Y_delta_backward = Y_df - Y_dv_backward
    Y_delta_central = Y_df - Y_dv_central

    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(16, 8)

    axs[0].set_title("Derivatives")
    axs[0].plot(X, Y_f, "silver", linewidth=1, label="f(x)")
    axs[0].plot(X, Y_df, "purple", linewidth=2, label="f'(x), analytical")

    axs[0].plot(X, Y_dv_forward, "red", linewidth=1, label="f'(x), forward difference")
    axs[0].plot(X, Y_dv_backward, "blue", linewidth=1, label="f'(x), backward difference")
    axs[0].plot(X, Y_dv_central, "green", linewidth=1, label="f'(x), central difference")

    axs[0].legend()

    axs[1].set_title("Difference to analytical value")
    axs[1].plot(X, Y_delta_forward, "red", label="delta: forward difference")
    axs[1].plot(X, Y_delta_backward, "blue", label="delta: backward difference")
    axs[1].plot(X, Y_delta_central, "green", label="delta: central difference")
    axs[1].legend()

    plt.show()
    pass


# ==================================================================================================================== #

def get_color(val, min, max):
    rng = max - min
    ang = ((val - min) / rng) * (.5 * np.pi)  # map val to a range 0..90°

    red = int(np.cos(ang) * 255)
    blu = int(np.sin(ang) * 255)

    s_red = f"{red:#04x}"[2:]
    s_blu = f"{blu:#04x}"[2:]

    return f"#{s_red}00{s_blu}"


def show_effect_epsilon():
    powers_min = 2
    powers_max = 18
    powers_res = 3

    powers = np.arange(powers_min, powers_max, powers_res)

    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(16, 8)

    axs[0].set_title("Derivatives")
    axs[0].set_ylim(-250, 250)
    # axs[0].set_yscale('symlog', linthresh=.1)
    axs[0].plot(X, Y_df, color="lime", label="analytic", marker='.')

    axs[1].set_title("Difference to analytic result")
    axs[1].set_ylim(-5, 5)
    axs[1].set_yscale('symlog', linthresh=0.01)

    plot_selection = slice(None, None, 8)
    for i, power in enumerate(powers):
        epsilon = 10.0 ** (-power)
        absolute = dv_central(f, X, epsilon)
        difference = Y_df - absolute

        color = get_color(power, powers_min, powers_max)
        label = f"epsilon = 10**(-{power})"

        axs[0].plot(X, absolute, color=color, linewidth=1, label=label)
        axs[0].legend()

        axs[1].plot(X[plot_selection], difference[plot_selection], color=color, linewidth=1, label=label)
        axs[1].legend(loc="upper right")

    plt.show()


# ==================================================================================================================== #

if __name__ == '__main__':
    show_difference_methods()
    show_effect_epsilon()
