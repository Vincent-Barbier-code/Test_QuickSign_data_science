"""Module containing data processing for dicts."""


def filter_data(
    data: list[dict[str, int | str]], key: str, value: int | str
) -> list[dict[str, int | str]]:
    """Filter data to keep only the items where data[key] == value.

    Args:
        data : The list of data to filter.
        key : The key to filter by.
        value: The value to match.

    Returns:
        A list of dictionaries that match the filter criteria.

    Raises:
        ValueError: if data is not a list of dictionaries.
        ValueError: if key is not a string.
        ValueError: if value is not an int or a string.
    """
    if not isinstance(data, list):
        raise ValueError("data should be a list.")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("data should be a list of dictionaries.")
    if not isinstance(key, str | int):
        raise ValueError("key should be a string or int.")
    # Pourquoi autorisons nous les int ? voir test_filter_data l-64
    if not isinstance(value, (int, str)):
        raise ValueError("value should be an int or a string.")

    result = []
    for item in data:
        # if key not in item:
        #     raise KeyError(f"Key {key} not found in dictionary.")
        #      Pourquoi autorisons nous les clés qui n'existent pas ? voir test_filter_data l-64
        if item.get(key) == value:
            result.append(item)
    return result


def sort_data(
    data: list[dict[str, int | str]], key: str
) -> list[dict[str, int | str]]:
    """Sort data by a given key in ascending order.

    Args:
        data: The list of data to sort.
        key: The key to sort by.

    Returns:
        A list of dictionaries sorted by the specified key.
        if the values of dictionary are strings, they are sorted in lexicographical order.

    Raises:
        ValueError: if data is not a list of dictionaries.
        ValueError: if key is not a string.
        KeyError: if key is not found in a dictionary.
        ValueError: if the values of dictionary are not digits.
    """
    if not isinstance(data, list) or not data:
        raise ValueError("data should be a list.")
    tab_val = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("data should be a list of dictionaries.")
        if not isinstance(key, str):
            raise ValueError("key should be a string.")
        if key not in item:
            raise KeyError(f"Key {key} not found in dictionary.")
        tab_val.append(item[key])
        if not isinstance(item[key], int | str):
            raise ValueError(
                "Values of dictionary should be either strings or integers."
            )
        if not (
            all(isinstance(val, str) for val in tab_val)
            or all(isinstance(val, int) for val in tab_val)
        ):
            raise ValueError(
                "Values of dictionary should be either all strings or all integers, not both."
            )

    data.sort(key=lambda dic: str(dic[key]))
    return data


def complex_filter(
    data: list[dict[str, int | str]], key: str, threshold: int
) -> list[dict[str, int | str]]:
    """Filter data using a threshold condition.

    Args:
        data: The list of data to filter.
        key: The key to filter by.
        threshold: The threshold value.

    Returns:
        A list of dictionaries that match the threshold criteria.

    Raises:
        ValueError: if data is not a list of dictionaries.
        ValueError: if key is not a string.
        ValueError: if threshold is not an int.
    """
    if not isinstance(data, list):
        raise ValueError("data should be a list.")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("data should be a list of dictionaries.")
    if not isinstance(key, str):
        raise ValueError("key should be a string.")
    if not isinstance(threshold, int):
        raise ValueError("threshold should be an int.")

    result = []
    for item in data:
        if key not in item:
            raise KeyError(f"Key {key} not found in dictionary.")
        if not isinstance(item[key], str | int):
            raise ValueError("Values of dictionary should be strings or int.")
        val = int(item[key])
        if val > threshold:
            result.append(item)
    return result


def aggregate_data(
    data: list[dict[str, int | str]], key: str
) -> dict[str, int]:
    """Aggregate data by a given key and count occurrences.

    Args:
        data: The list of data to aggregate.
        key: The key to aggregate by.

    Returns:
        A dictionary with the aggregated data.

    Raises:
        ValueError: if data is not a list of dictionaries.
        ValueError: if key is not a string.
        KeyError: if key is not found in a dictionary.
    """
    if not isinstance(data, list):
        raise ValueError("data should be a list.")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("data should be a list of dictionaries.")
    if not isinstance(key, str):
        raise ValueError("key should be a string.")

    result = {}
    for item in data:
        if key not in item:
            raise KeyError(f"Key {key} not found in dictionary.")
        if not isinstance(item[key], str | int):
            raise ValueError("Values of dictionary should be strings or int.")
        val = str(item[key])
        if val not in result:
            result[val] = 0
        result[val] += 1

    return result
