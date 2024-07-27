"""Module containing some function for science processing."""

import numpy as np
from sklearn import metrics


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute mean squared error between two 1D arrays : y_true and y_true.

    Args:
        y_true: 1D numpy array containing floats
        y_pred: 1D numpy array containing floats

    Returns:
        mean squared error between y_true and y_pred

    Raises:
        ValueError if numpy arrays have more than one dimension.
    """
    if y_true.ndim != 1 or y_pred.ndim != 1:
        raise ValueError("Input arrays should be 1D.")

    # sklearn for the precision
    rmse: float = metrics.mean_squared_error(y_true, y_pred)
    return rmse


def moving_average(data: np.ndarray, window_size: int) -> np.ndarray:
    """Compute moving average of a 1D array data.

    Args:
        data: 1D numpy array containing floats

    Returns:
        numpy array containing moving average with the given window_size.

    Raises:
        ValueError if numpy arrays have more than one dimension.
        ValueError if window_size is not a positive integer and greater than 1.
    """
    if data.ndim != 1:
        raise ValueError("Input arrays should be 1D.")
    if not isinstance(window_size, int) or window_size < 1:
        raise ValueError(
            "Window size should be a positive integerand greater than 1."
        )

    result: np.ndarray = np.array([])
    for i in range(len(data) - window_size + 1):
        result = np.append(result, np.mean(data[i : i + window_size]))
    return result


def find_duplicates(arr: list[float]) -> list[float]:
    """
    Find duplicates in a list of floats.

    Args:
        arr: list of floats

    Returns:
        list of duplicates

    Raises:
        ValueError if input is not a list.
        ValueError if input is not a list of floats or int.
    """

    if not isinstance(arr, list):
        raise ValueError("Input should be a list.")
    if not all(isinstance(x, float | int) for x in arr):
        raise ValueError("Input should be a list of floats or int.")

    duplicates: list[float] = []
    first_occurence: list[float] = []

    for _, val in enumerate(arr):
        if val in first_occurence:
            if val not in duplicates:
                duplicates.append(val)
        else:
            first_occurence.append(val)
    print(first_occurence)
    print(duplicates)
    return duplicates


def prime_factors(n: int) -> list[int]:
    """Find all prime factors of a number n.

    Args:
        n: integer number to find prime factors of.

    Returns:
        list of prime factors of n.

    Raises:
        ValueError if input is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input should be a positive integer.")

    factors: list[int] = []
    factor = 2
    while n > 1:
        if n % factor == 0:
            factors.append(factor)
            n //= factor
        else:
            factor += 1
    return factors


def partition(arr: list[int], low: int, high: int) -> int:
    """
    Partition the array so that all elements smaller than the pivot are on the left
    and all elements greater are on the right.

    Args:
        arr: list of integers to partition.
        low: lower index of the array.
        high: higher index of the array.

    Returns:
        index of the pivot element.

    """

    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap
            print(arr)
            print(i, j)

    arr[i + 1], arr[high] = (
        arr[high],
        arr[i + 1],
    )  # swap pivot in the correct position
    return i + 1


def sort(arr: list[int], low: int, high: int) -> None:
    """
    Sort the array using quicksort algorithm.

    Args:
        arr: list of integers to sort.
        low: lower index of the array.
        high: higher index of the array.

    Returns:
        None
    """

    if low < high:
        pi = partition(arr, low, high)
        sort(arr, low, pi - 1)
        sort(arr, pi + 1, high)


def quicksort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers using quicksort algorithm.

    Args:
        arr: list of integers to sort.

    Returns:
        sorted list of integers.

    Raises:
        ValueError if input is not a list.
        ValueError if input is not a list of integers.
    """
    if not isinstance(arr, list):
        raise ValueError("Input should be a list.")
    for i in arr:
        if not isinstance(i, int):
            raise ValueError("Input should be a list of integers.")

    sort(arr, 0, len(arr) - 1)
    return arr
