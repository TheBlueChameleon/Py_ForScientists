import physics
import visualization

if __name__ == '__main__':
    field = physics.Field()
    field.evolve(time=100)

    observable = physics.Observable(field)

    figure = visualization.Figure()
    figure.add_plot(field)
    figure.add_plot(observable)

    figure.show()
