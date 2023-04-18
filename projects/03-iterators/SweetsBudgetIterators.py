import itertools
import sys
import time


def main():
    money = 10.0
    sweets_price_and_score = {
        "dark chocolate": (1.0, 5),
        "milk chocolate": (0.9, 4),
        "caramel nuts bar": (2.3, 12),
        "coco cubes": (1.5, 8),
        "mint drops": (0.3, 1),
        # "A": (1, 1),
        # "B": (2, 2),
        # "C": (3, 3)
    }

    tic = time.perf_counter()
    upper_limits = map(lambda price_and_score: int(money // price_and_score[0]), sweets_price_and_score.values())
    individual_counts = (range(0, u + 1) for u in upper_limits)
    configurations = itertools.product(*individual_counts)

    get_price_for_configuration = lambda config: (sum(
        qty * evaluation[0]
        for qty, evaluation
        in zip(config, sweets_price_and_score.values())
    ), config)
    prices = map(get_price_for_configuration, configurations)

    get_value_for_configuration = lambda price, config: (sum(
        qty * evaluation[1]
        for qty, evaluation
        in zip(config, sweets_price_and_score.values())
    ), price, config)
    values_affordable = itertools.starmap(
        get_value_for_configuration,
        filter(lambda price: price[0] <= money, prices)
    )
    best_value, best_price, best_config = max(values_affordable, key=lambda all_data: all_data[0])
    toc = time.perf_counter()

    relevant_memory = \
        sys.getsizeof(upper_limits) + \
        sys.getsizeof(individual_counts) + \
        sys.getsizeof(configurations) + \
        sys.getsizeof(prices) + \
        sys.getsizeof(values_affordable)

    print("ITERATORS RESULT:")
    print("It is best to buy:")
    for amount, sweet in zip(best_config, sweets_price_and_score.items()):
        print(f"{amount:2} of {sweet[0]:20} (for ${amount * sweet[1][0]:4.2f} and {amount * sweet[1][1]:2} points)")
    print(f"For a grand total of {best_value} points at ${best_price:5.2f}")
    print(f"It took {(toc - tic) * 1000:7.2f} milliseconds to analyze this optimization problem")
    print(f"Memory footprint: {relevant_memory} bytes.")
    print()


if __name__ == "__main__":
    main()
