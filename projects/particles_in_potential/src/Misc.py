class Misc:
    @staticmethod
    def central_difference_quotient(f, x, epsilon):
        return (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)

    @staticmethod
    def bind_all_parameters_but_ith(f, i, coordinates):
        def inner(x):
            parameters = list(coordinates)
            parameters[i] = x
            return f(*parameters)

        return inner

    @staticmethod
    def demo_overwrite_default(default=[]):
        default.append( len(default) )
        print(f"This is call #{len(default)} to this function.")