import numpy as np
from scipy.optimize import linear_sum_assignment


def main():
    """
    trains - ids of trains
    routes - ids of
    """

    trains, routes = {}, {}
    scores = np.matrix([[]])
    trains, routes, mapped, scores = apply_constraints(trains, routes, scores)

    mapped.update(matchmaking(trains, routes, scores))
    return mapped


def matchmaking(trains, routes, scores):
    mapped = {}
    # Apply linear assignment
    solutions = linear_sum_assignment(np.subtract(1, scores))

    sol_trains = solutions[0]
    sol_routes = solutions[1]

    for sol_index, train_index in enumerate(sol_trains):
        mapped[train_index] = sol_routes[sol_index]

    return mapped


def apply_constraints(trains, routes, scores):
    mapped = {}
    return trains, routes, mapped, scores


if __name__ == "__main__":
    main()