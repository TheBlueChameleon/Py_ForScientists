import numpy as np
import sys
import time


def main():
    # the givens
    money = 10.0
    names = ["dark chocolate", "milk chocolate", "caramel nuts bar", "coco cubes", "mint drops"]
    prices = np.array([1.0, 0.9, 2.3, 1.5, 0.3])
    weights = np.array([5, 4, 12, 8, 1])

    tic = time.perf_counter()
    N = len(names)

    # construction of the meshgrid
    upper_limits = money // prices  # upper limits: this many elements can be bought if we limit ourselves to a single sort of sweets
    values = tuple(np.arange(u + 1) for u in upper_limits)  # tuple of lists: each lists goes from 0 to N_sweet ...
    meshgrid = np.meshgrid(*values)  # ... which can be used to build the meshgrid from this.

    # Find the cost for each configuration ...
    total_money = np.zeros(meshgrid[0].shape)
    for i, price in enumerate(prices):
        total_money += price * meshgrid[i]

    # ... and the point score as well
    totalScore = np.zeros(meshgrid[0].shape)
    for i, score in enumerate(weights):
        totalScore += score * meshgrid[i]

    # which configurations can we actually afford?
    mask = total_money > money
    totalScore[mask] = -1  # give bad score to configurations that are too expensive

    # argmax yields the ID of the best configuration ...
    best_id = np.argmax(totalScore)

    # ... and unravel_index reconstructs the indices in our multidimensional array from this ID
    bestConfig = np.unravel_index(best_id, shape=meshgrid[0].shape)

    toc = time.perf_counter()
    relevant_memory = sys.getsizeof(upper_limits) + \
                      sys.getsizeof(values) + \
                      sys.getsizeof(meshgrid) + \
                      sys.getsizeof(total_money) + \
                      sys.getsizeof(totalScore) + \
                      sys.getsizeof(mask)

    print("NUMPY RESULT:")
    print("Sugar-Strategy:")
    print("Sweet                | Count  | Price | Score ")
    print("---------------------+--------+-------+-------")
    for i in range(N):
        ith_component_count_count = meshgrid[i][bestConfig]
        # meshgrid[i] is the i-th tensor, i.e. the one for dark chocolate/milk chocolate/...
        # bestConfig holds the coordinates of the best configuration as a tuple
        # thus, meshgrid[i][bestConfig] is the number of bars/packages/... of the i-th sweet you'd want to buy, optimally
        print(
            f"{names[i]:20} | {ith_component_count_count:6.0f} | {ith_component_count_count * prices[i]:5.2f} | {ith_component_count_count * weights[i]:5}")
    print("---------------------+--------+-------+-------")
    print(f"{'TOTAL':20} | {np.sum(bestConfig):6} | {total_money[bestConfig]:5.2f} | {totalScore[bestConfig]:5.0f}")
    print()
    print("Analyzed", np.prod(1 + upper_limits, dtype=np.int), f"configurations in {(toc - tic) * 1000:5.2f} milliseconds.")
    print(f"Memory footprint: {relevant_memory / (1024**2):4.2f} megabytes.")
    print()


if __name__ == "__main__":
    main()
