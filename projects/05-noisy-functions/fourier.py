import matplotlib.pyplot as plt
import numpy as np
import scipy as sci


def fourier_1d():
    N = 200
    frequency_1 = 3
    amplitude_1 = 2
    frequency_2 = 20
    amplitude_2 = 1

    xs = np.linspace(0, 2 * np.pi, N)
    ys = amplitude_1 * np.sin(frequency_1 * xs) + amplitude_2 * np.cos(frequency_2 * xs)

    frequencies = 2 * np.pi * np.arange(-N // 2, +N // 2) / xs[-1]
    fft = sci.fft.fft(ys)
    fft = np.roll(fft, N // 2)

    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(16, 8)

    axs[0].plot(xs, ys, label="$y(t)$")

    axs[1].plot(frequencies, fft.real, label="$\Re(\mathcal{F}[y])(\omega)$")
    axs[1].plot(frequencies, fft.imag, label="$\Im(\mathcal{F}[y])(\omega)$")
    axs[1].legend()

    plt.show()


def synthesized():
    N = 100

    fft = np.zeros(N)
    fft[0] = 1
    ys = sci.fft.ifft(fft)
    plt.plot(ys, color="darkslateblue")

    fft = np.zeros(N)
    fft[1] = 1
    ys = sci.fft.ifft(fft)
    plt.plot(ys, color="crimson")

    fft = np.zeros(N)
    fft[-1] = 1
    ys = sci.fft.ifft(fft)
    plt.plot(ys, "1", color="crimson")

    fft = np.zeros(N, dtype=np.complex)
    fft[1] = 1j
    ys = sci.fft.ifft(fft)
    plt.plot(ys.real, color="gold")

    fft = np.zeros(N, dtype=np.complex)
    fft[-1] = 1j
    ys = sci.fft.ifft(fft)
    plt.plot(ys, "1", color="gold")

    plt.show()

    ax = plt.subplot(projection='3d')
    fft = np.zeros(N, dtype=np.complex)
    fft[5] = 1j
    ys = sci.fft.ifft(fft)
    plt.plot(range(N), ys.real, ys.imag)
    plt.xlabel("$t$")
    plt.ylabel("$\Re$")
    ax.set_zlabel("$\Im$")
    plt.show()


def fourier_2d():
    img_original = 256 - sci.misc.ascent()
    fft_original = sci.fft.fft2(img_original)
    fla_original = np.log(np.absolute(fft_original))
    size = img_original.shape

    fft_hi_pass_filter = fft_original.copy()
    hi_pass_filter_size = 20
    fft_hi_pass_filter[:hi_pass_filter_size, :hi_pass_filter_size] = 0
    fft_hi_pass_filter[-hi_pass_filter_size:, -hi_pass_filter_size:] = 0
    fft_hi_pass_filter[-hi_pass_filter_size:, :hi_pass_filter_size] = 0
    fft_hi_pass_filter[:hi_pass_filter_size, -hi_pass_filter_size:] = 0
    fla_hi_pass_filter = np.log(np.absolute(fft_hi_pass_filter))
    img_hi_pass_filter = sci.fft.ifft2(fft_hi_pass_filter).real

    fft_lo_pass_filter = fft_original.copy()
    lo_pass_filter_size = 225
    fft_lo_pass_filter[size[0]//2 - lo_pass_filter_size:size[0]//2 + lo_pass_filter_size,
                       size[1]//2 - lo_pass_filter_size:size[1]//2 + lo_pass_filter_size] = 0
    fla_lo_pass_filter = np.log(np.absolute(fft_lo_pass_filter))
    img_lo_pass_filter = sci.fft.ifft2(fft_lo_pass_filter).real

    fig, axs = plt.subplots(2, 3)
    fig.set_size_inches(16, 12)

    axs[0, 0].imshow(img_original, cmap='Greys')
    axs[1, 0].imshow(fla_original, cmap='viridis')

    axs[0, 1].imshow(img_hi_pass_filter, cmap='Greys')
    axs[1, 1].imshow(fla_hi_pass_filter, cmap='viridis')

    axs[0, 2].imshow(img_lo_pass_filter, cmap='Greys')
    axs[1, 2].imshow(fla_lo_pass_filter, cmap='viridis')

    plt.show()


def main():
    # fourier_1d()
    # synthesized()
    fourier_2d()


if __name__ == '__main__':
    main()
