import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import functools

def show_1d_minimal():
    res = 250

    amplitude = 1
    decay = 5
    amplitude_noise = 0.1

    f = lambda x, a, k : a * np.exp(-k * x)

    xs = np.linspace(0, 1, res)
    ys = f(xs, amplitude, decay) + amplitude_noise * np.random.random(res)

    popt, pcov = sci.optimize.curve_fit(f, xs, ys)
    reconstructed = f(xs, *popt)

    print(pcov)
    print(np.sqrt(np.diag(pcov)))

    plt.plot(xs, ys, label="signal")
    plt.plot(xs, reconstructed, label="{0:4.2f} $\\exp(-${1:4.2f}$t)$".format(*popt))
    plt.legend()
    plt.show()


def show_1d_fail():
    tau = 2 * np.pi
    res = 250
    amplitude_true = 3
    frequency_true = 7 * tau
    f = lambda t, amplitude, frequency: amplitude * np.sin(frequency * t)

    xs = np.linspace(0, 1, res)
    ys = f(xs, amplitude_true, frequency_true)

    window = slice(0, 20, 1)

    popt_naive, pcov_naive = sci.optimize.curve_fit(f, xs, ys)
    perr_naive = np.sqrt(np.diag(pcov_naive))
    ys_recovered_naive = f(xs, *popt_naive)

    popt_hint, pcov_hint = sci.optimize.curve_fit(f, xs, ys, p0=(5, 20))
    perr_hint = np.sqrt(np.diag(pcov_hint))
    ys_recovered_hint = f(xs, *popt_hint)

    popt_window, pcov_window = sci.optimize.curve_fit(f, xs[window], ys[window])
    perr_window = np.sqrt(np.diag(pcov_window))
    ys_recovered_window = f(xs, *popt_window)

    print("method", "", "amplitude", "", "", "", "frequency", sep="\t")
    print("naive", f"{popt_naive[0]:+7.3f} +/- {perr_naive[0]:9.2f}", f"{popt_naive[1]:+7.3f} +/- {perr_naive[1]:7.3f}",
          sep="\t")
    print("hinted", f"{popt_hint[0]:+7.3f} +/- {perr_hint[0]:9.2f}", f"{popt_hint[1]:+7.3f} +/- {perr_hint[1]:7.3f}",
          sep="\t")
    print("window", f"{popt_window[0]:+7.3f} +/- {perr_window[0]:9.2f}",
          f"{popt_window[1]:+7.3f} +/- {perr_window[1]:7.3f}", sep="\t")

    plt.plot(xs, ys, label="original data")
    plt.plot(xs, ys_recovered_naive, "-", label="naive fit")
    plt.plot(xs, ys_recovered_hint, "-", label="hinted fit")
    plt.plot(xs, ys_recovered_window, "1", label="windowed fit")
    plt.legend()
    plt.show()


def prepare_data_2d(show_plot=False):
    res = 250
    xs = np.linspace(0, 1, res)
    ys = np.linspace(0, 1, res)
    Y, X = np.meshgrid(xs, ys)

    amplitude_left = 2
    slope_left = 4
    amplitude_right = 6
    slope_right = 2

    f_left = lambda t: amplitude_left * (np.cosh(slope_left * (t - 0.5)) - 1)
    f_right = lambda t: amplitude_right * np.exp(-slope_right * t)
    f = lambda x, y: x * f_right(y) + (1 - x) * f_left(y)

    Z = f(X, Y)

    if show_plot:
        fig, axs = plt.subplots(1, 3)
        fig.set_size_inches(15, 5)

        axs[0].set_title("Full 2D Dataset")
        axs[0].set_xlabel("x")
        axs[0].set_ylabel("y")
        axs[0].pcolor(X, Y, Z)

        axs[1].set_title("Left Edge of Graph")
        axs[1].set_xlabel("y")
        axs[1].set_ylabel("z")
        axs[1].plot(X[:, 0], Z[0])

        axs[2].set_title("Right Edge of Graph")
        axs[2].set_xlabel("y")
        axs[2].set_ylabel("z")
        axs[2].plot(X[:, -1], Z[-1])

        plt.show()

    return X, Y, Z


def fit_2D(data):
    X, Y, Z = data

    column = -1
    xs = X[:, column]

    f_left = lambda t, amplitude_left, slope_left: amplitude_left * (np.cosh(slope_left * (t - 0.5)) - 1)
    f_right = lambda t, amplitude_right, slope_right: amplitude_right * np.exp(-slope_right * t)
    f = lambda x, y, amplitude_left, slope_left, amplitude_right, slope_right: \
        x * f_right(y, amplitude_right, slope_right) +\
        (1 - x) * f_left(y, amplitude_left, slope_left)

    p0=(1,1,1,1)
    for i, x in enumerate(xs):
        zs = Z[i]
        f_set_in_x = functools.partial(f, x=x)
        f_local = lambda t, param_1, param_2, param_3, param_4 : \
            f_set_in_x(y=t,
                       amplitude_left=param_1, slope_left=param_2,
                       amplitude_right=param_3, slope_right=param_4
                       )
        popt, pcov = sci.optimize.curve_fit(f_local, xs, zs, p0=p0)
        p0 = popt

    print(popt)

    Z_reconstructed = f(X, Y, *popt)
    difference = np.sum(Z - Z_reconstructed)
    print("deviation from true result:", difference)



def main():
    # show_1d_minimal()
    # show_1d_fail()

    data = prepare_data_2d(show_plot=True)
    fit_2D(data)


if __name__ == '__main__':
    main()


