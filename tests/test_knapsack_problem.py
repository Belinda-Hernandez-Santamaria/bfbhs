from bfbhs import knapsack_problem
import itertools as itt
def test_knapsack_problem():
    assert knapsack_problem([8, 5, 7, 5, 10, 9], [10, 8, 3, 4, 11, 15], 15, 25) == False
    assert knapsack_problem([3, 7, 2, 4, 8, 10, 1], [9, 3, 5, 6, 8, 7, 11], 10, 35) == False
    assert knapsack_problem([10, 6, 8, 7, 9], [5, 9, 6, 3, 9], 16, 10) == (0, 0, 0, 1, 1)
    assert knapsack_problem([1, 2, 3], [10, 15, 40], 6, 50) == (0, 1, 1)