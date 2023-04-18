import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import convolve


class Simulation:
    def __init__(self):
        # defining characteristics
        self._shape = None
        self._t_min = 0
        self._t_max = None
        self._t_res = None
        self._alpha = None

        # derived attributes
        self._laplacian = None
        self._t = None
        self._initial_state = None
        self._fixed_gridpoints = None
        self._result = None

    # ================================================================================================================ #

    def get_shape(self) -> tuple:
        return self._shape

    def set_shape(self, shape: tuple):
        self._shape = shape
        self._allocate()
        return self

    def get_t_min(self) -> float:
        return self._t_min

    def set_t_min(self, t_min: float):
        self._t_min = t_min
        self._allocate()
        return self

    def get_t_max(self) -> float:
        return self._t_max

    def set_t_max(self, t_max: float):
        self._t_max = t_max
        self._allocate()
        return self

    def get_t_rex(self) -> float:
        return self._t_res

    def set_t_res(self, t_res: float):
        self._t_res = t_res
        self._allocate()
        return self

    def get_alpha(self) -> float:
        return self._alpha

    def set_alpha(self, alpha: float):
        self._alpha = alpha
        return self

    def get_initial_state(self) -> np.ndarray:
        return self._initial_state

    def set_initial_state(self, state: np.ndarray):
        if self._shape is None:
            self.set_shape(state.shape)
        self._initial_state = state
        return self

    def get_fixed_gridpoints(self) -> np.ndarray:
        return self._fixed_gridpoints

    def set_fixed_gridpoints(self, boundary: np.ndarray):
        self._fixed_gridpoints = boundary
        return self

    # ================================================================================================================ #

    def is_defined(self) -> bool:
        if self._shape is None: return False
        if self._t_min is None: return False
        if self._t_max is None: return False
        if self._t_res is None: return False

        return True

    def is_ready(self) -> bool:
        if self.is_defined():
            if self._t is None: return False
            if self._initial_state is None: return False
            if self._fixed_gridpoints is None: return False
            if self._alpha is None: return False

            if self._initial_state.shape != self._shape:
                raise RuntimeError("Inconsistent state of memory: registered shape does not meet data shape")

            if self._fixed_gridpoints.shape != self._shape:
                raise RuntimeError(
                    "Inconsistent state of memory: registered shape does not meet shape of fixed gridpoints")

            if self._t.size != (self._t_max - self._t_min) / self._t_res:
                raise RuntimeError("Inconsistent state of memory: registered time interval does not meet time shape")

            return True

        else:
            return False

    # ================================================================================================================ #

    def _allocate(self):
        if self.is_defined():
            self._t = np.arange(self._t_min, self._t_max, self._t_res)
            self._initial_state = np.zeros(shape=self._shape, dtype=np.float64)
            self._fixed_gridpoints = np.zeros(shape=self._shape, dtype=np.bool_)
            self._prepare_laplacian()
        else:
            pass

    def _prepare_laplacian(self):
        N_dimensions = len(self._shape)
        self._laplacian = np.zeros(shape=tuple(3 for _ in range(N_dimensions)))

        # set the axis elements through the central element to 1
        for dimension_index in range(N_dimensions):
            coordinate = tuple(slice(None, None, None) if i == dimension_index else 1 for i in range(N_dimensions))
            self._laplacian[coordinate] = 1

        # set the central element to 2 * N_dimensions
        coordinate = tuple(1 for _ in range(N_dimensions))
        self._laplacian[coordinate] = -2 * N_dimensions

    # ================================================================================================================ #

    def run(self):
        def dT(t: float, T: np.ndarray, operator: np.ndarray):
            T = T.reshape(self._shape)

            dT = convolve(T, operator, mode='same')
            dT[self._fixed_gridpoints] = 0.

            return dT.reshape((T.size))

        if self.is_ready():
            # pre-computing all factors into one operator saves a ton of multiplications
            scaled_laplacian = self._alpha * self._laplacian

            self._result = solve_ivp(dT, t_span=(self._t_min, self._t_max), y0=self._initial_state.flatten(),
                                     args=(scaled_laplacian,), t_eval=self._t, vectorized=True)

            final_shape = tuple((*self._shape, self._t.size))
            self._result.y = self._result.y.reshape(final_shape)
        else:
            raise RuntimeError(f"Not ready yet\n{self}")

        if not self._result.success:
            raise RuntimeError(self._result.message)

    # ================================================================================================================ #

    def _check_result_present(self):
        if self._result is None:
            raise RuntimeError("Simulation has not yet been started")

    def get_result(self):
        self._check_result_present()
        return self._result

    def get_heatmaps(self):
        self._check_result_present()
        return self._result.y

    # ================================================================================================================ #

    def show_plot(self):
        if len(self._shape) == 1:
            x_labels = np.arange(self._shape[0])
            t_labels = self._t

            grid_t, grid_x = np.meshgrid(t_labels, x_labels)

            plt.pcolor(grid_t, grid_x, self._result.y)
            plt.title("Time Evolution of Heat Distribution (1D)")
            plt.xlabel("time")
            plt.ylabel("length")
            plt.colorbar()
            plt.show()

        else:
            raise RuntimeError("Full Plot can only be generated for one dimension")

    def show_plot_final_state(self):
        N_dimensions = len(self._shape)
        if N_dimensions == 1:
            plt.plot(self._result.y[:, -1])
            plt.title(f"Temperature profile at t = {self._t[-1]}")
            plt.xlabel("x")
            plt.ylabel("T")
            plt.show()

        elif N_dimensions == 2:
            map = self._result.y[:, :, -1]
            plt.pcolor(map)
            plt.colorbar()
            plt.xlabel("x")
            plt.ylabel("y")
            plt.show()

        else:
            raise RuntimeError("Final Plot can only be generated for one- or two-dimensional scenarios")

    def __str__(self):
        result = "SIMULATION STATE:\n"
        result += f"  shape: {self._shape}\n"
        result += f"  t_min: {self._t_min}\n"
        result += f"  t_max: {self._t_max}\n"
        result += f"  t_res: {self._t_res}\n"
        result += f"  alpha: {self._alpha}\n"
        return result
