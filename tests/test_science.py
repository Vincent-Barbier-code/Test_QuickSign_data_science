import random as rand

import numpy as np
import pytest

from qsdata.science import (
    find_duplicates,
    mean_squared_error,
    moving_average,
    prime_factors,
    quicksort,
)


def test_prime_factors():
    assert prime_factors(28) == [2, 2, 7]
    assert prime_factors(29) == [29]
    with pytest.raises(ValueError):
        prime_factors(-20)


def test_mean_squared_error():
    y_true = np.array([1, 2, 3])
    y_pred = np.array([1, 2, 3])
    print(mean_squared_error(y_true, y_pred))
    assert mean_squared_error(y_true, y_pred) == 0

    y_pred = np.array([2, 2, 2])
    assert mean_squared_error(y_true, y_pred) == 2 / 3
    with pytest.raises(ValueError):
        mean_squared_error(y_true, np.zeros((2, 4)))
    with pytest.raises(ValueError):
        mean_squared_error(np.zeros((2, 4)), y_pred)

    # my test
    y_true2 = np.array([[1, 2, 3], [1, 2, 3]])
    y_pred2 = np.array([1, 2, 3], ndmin=6)
    with pytest.raises(ValueError):
        mean_squared_error(y_true2, y_pred)
    with pytest.raises(ValueError):
        mean_squared_error(y_true, y_pred2)


def test_moving_average():
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = moving_average(data, 3)
    expected = np.array([2, 3, 4, 5, 6, 7, 8, 9])
    assert np.allclose(result, expected)

    # my test
    data2 = np.array([1, 2, 3], ndmin=2)
    with pytest.raises(ValueError):
        moving_average(data2, 3)
    with pytest.raises(ValueError):
        moving_average(data, 0)
    with pytest.raises(ValueError):
        moving_average(data, "string")


def test_find_duplicates():
    arr = [1, 2, 3, 1, 2, 4]
    duplicates = find_duplicates(arr)
    assert 1 in duplicates
    assert 2 in duplicates

    arr = [1, 2, 3, 4, 5]
    assert not find_duplicates(arr)

    # my test
    arr2 = [1, 2, 4.5, 3, 1, 2, 4.5]
    assert 1 in find_duplicates(arr2)
    assert 2 in find_duplicates(arr2)
    assert 4.5 in find_duplicates(arr2)

    with pytest.raises(ValueError):
        find_duplicates([1, 2, 3, 4, "string"])
    with pytest.raises(ValueError):
        find_duplicates([np.array([1, 2, 3]), 2, 3, 4])
    with pytest.raises(ValueError):
        find_duplicates("string")
    assert [] == find_duplicates([1, 2, 3])


def test_quicksort():
    assert quicksort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
    assert quicksort([]) == []
    assert quicksort([1]) == [1]

    # my test
    random_list = [rand.randint(-100, 100) for _ in range(100)]
    with pytest.raises(ValueError):
        quicksort({"Hello", 1})
    with pytest.raises(ValueError):
        quicksort([1, 2, 3, "string"])
    assert quicksort(random_list) == sorted(random_list)
