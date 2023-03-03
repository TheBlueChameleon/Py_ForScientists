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
    def roll(img):
        img = np.roll(img, img.shape[0] // 2, axis=0)
        img = np.roll(img, img.shape[1] // 2, axis=1)
        return img

    def create_cirular_mask(shape, radius):
        w, h = shape
        center = (w//2, h//2)

        Y, X = np.ogrid[:h, :w]
        dist_from_center_squared = (X - center[0]) ** 2 + (Y - center[1]) ** 2

        mask = dist_from_center_squared <= (radius ** 2)
        return mask

    img_original = 256 - sci.misc.ascent()
    fft_original = sci.fft.fft2(img_original)
    display_original = roll(np.log(np.absolute(fft_original)))

    img_size = img_original.shape
    mask = create_cirular_mask(img_size, 20)

    fft_hi_pass_filter = roll(fft_original.copy())
    fft_hi_pass_filter[mask] = 0
    display_hi_pass_filter = roll(np.log(np.absolute(fft_hi_pass_filter)))
    fft_hi_pass_filter = roll(fft_hi_pass_filter)
    img_hi_pass_filter = sci.fft.ifft2(fft_hi_pass_filter).real

    display_hi_pass_filter = roll(display_hi_pass_filter)

    mask = np.logical_not(create_cirular_mask(img_size, 60))

    fft_lo_pass_filter = roll(fft_original.copy())
    fft_lo_pass_filter[mask] = 0
    display_lo_pass_filter = roll(np.log(np.absolute(fft_lo_pass_filter)))
    fft_lo_pass_filter = roll(fft_lo_pass_filter)
    img_lo_pass_filter = sci.fft.ifft2(fft_lo_pass_filter).real

    display_lo_pass_filter = roll(display_lo_pass_filter)

    fig, axs = plt.subplots(2, 3)
    fig.set_size_inches(16, 12)

    frequencies_X = np.arange(-img_size[0] // 2, img_size[0] // 2)
    frequencies_Y = np.arange(-img_size[1] // 2, img_size[1] // 2)
    kX, kY = np.meshgrid(frequencies_X, frequencies_Y)

    axs[0, 0].imshow(img_original, cmap='Greys')
    axs[1, 0].pcolor(kX, -kY,display_original, cmap='viridis')

    axs[0, 1].imshow(img_hi_pass_filter, cmap='Greys')
    axs[1, 1].pcolor(kX, -kY, display_hi_pass_filter, cmap='viridis')

    axs[0, 2].imshow(img_lo_pass_filter, cmap='Greys')
    axs[1, 2].pcolor(kX, -kY, display_lo_pass_filter, cmap='viridis')

    plt.show()


def main():
    # fourier_1d()
    # synthesized()
    fourier_2d()


if __name__ == '__main__':
    main()
