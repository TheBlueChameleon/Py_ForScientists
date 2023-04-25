import matplotlib.pyplot as plt
import numpy as np
import scipy as sci


def prepare_noisy_function():
    N = 100
    frequency_1 = 5
    amplitude_1 = 2
    frequency_2 = 3
    amplitude_2 = 1
    noise_level = 1.5
    bias_const = 2.3
    bias_slope = 0.5

    xs = np.linspace(0, 2 * np.pi, N)
    ys = amplitude_1 * np.sin(frequency_1 * xs) + amplitude_2 * np.cos(frequency_2 * xs)

    bias = bias_const + bias_slope * xs
    noise = noise_level * np.random.random(N)
    signal = ys + bias + noise

    frequencies = 2 * np.pi * np.arange(N) / xs[-1]
    fft_clean = sci.fft.fft(ys)
    fft_noisy = sci.fft.fft(signal)

    return xs, ys, signal, frequencies, fft_clean, fft_noisy


def trend_filter(data):
    xs, signal_clean, signal_noisy, frequencies, fft_clean, fft_noisy = data
    signal_noisy = sci.signal.detrend(signal_noisy)
    fft_noisy = sci.fft.fft(signal_noisy)
    return xs, signal_clean, signal_noisy, frequencies, fft_clean, fft_noisy


def lopass_filter(data):
    xs, signal_clean, signal_noisy, frequencies, fft_clean, fft_noisy = data

    cutoff_frequency = 8
    cutoff_inverse = signal_noisy.size - cutoff_frequency
    mask = np.logical_and(frequencies > cutoff_frequency, frequencies < cutoff_inverse)
    fft_noisy[mask] = 0
    signal_noisy = sci.fft.ifft(fft_noisy)

    return xs, signal_clean, signal_noisy, frequencies, fft_clean, fft_noisy


def wiener_filter(data):
    xs, signal_clean, signal_noisy, frequencies, fft_clean, fft_noisy = data

    signal_noisy = sci.signal.wiener(signal_noisy, 5)
    fft_noisy = sci.fft.fft(signal_noisy)

    return xs, signal_clean, signal_noisy, frequencies, fft_clean, fft_noisy


def plot_data(data, label, axs, column):
    color_clean = "mediumblue"
    color_noisy = "crimson"
    fft_window = slice(0, 20, 1)

    xs, signal_clean, signal_noisy, frequencies, fft_clean, fft_noisy = data

    axs[0, column].set_title(label)

    axs[0, column].plot(xs, signal_clean, color=color_clean)
    axs[0, column].plot(xs, signal_noisy, color=color_noisy)

    axs[1, column].set_title("Fourier Transform")

    axs[1, column].plot(frequencies[fft_window], fft_clean[fft_window].real, label=r"$\Re$(clean)", color=color_clean,
                        marker="1", linewidth=0.2)
    axs[1, column].plot(frequencies[fft_window], fft_clean[fft_window].imag, label=r"$\Im$(clean)", color=color_clean,
                        marker="+", linewidth=0.2)
    axs[0, column].set_xlabel("$t$")
    axs[0, column].set_ylabel("$f(t)$")

    axs[1, column].plot(frequencies[fft_window], fft_noisy[fft_window].real, label=r"$\Re$(signal)", color=color_noisy,
                        marker="2", linewidth=0.2)
    axs[1, column].plot(frequencies[fft_window], fft_noisy[fft_window].imag, label=r"$\Im$(signal)", color=color_noisy,
                        marker="x", linewidth=0.2)
    axs[1, column].set_xlabel("$\omega$")
    axs[1, column].set_ylabel("$\hat{f}(\omega)$")
    axs[1, column].legend()


def main():
    data_original = prepare_noisy_function()
    data_detrended = trend_filter(data_original)
    data_lopass = lopass_filter(data_detrended)
    data_wiener = wiener_filter(data_detrended)

    fig, axs = plt.subplots(2, 4)
    fig.set_size_inches(16, 8)
    fig.suptitle(r"$f(t) = A_1 \sin(\omega_1 t) + A_2 \cos(\omega_2 t) + $noise$(t)$")

    plot_data(data_original, "Unfiltered", axs, 0)
    plot_data(data_detrended, "Trend Removal", axs, 1)
    plot_data(data_lopass, "Trend Removal and Lopass-Filter", axs, 2)
    plot_data(data_wiener, "Trend Removal and Wiener Filter", axs, 3)

    plt.show()


if __name__ == '__main__':
    main()
