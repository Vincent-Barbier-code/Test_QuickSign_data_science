""" Module for testing data_processing.py """

import pytest

from qsdata.data_processing import (
    aggregate_data,
    complex_filter,
    filter_data,
    sort_data,
)


@pytest.fixture
def sample_data():
    """Sample data for testing"""
    return [
        {"name": "Alice", "age": 30, "city": "Paris"},
        {"name": "Bob", "age": 25, "city": "Paris"},
        {"name": "Charlie", "age": 35, "city": "London"},
        {"name": "David", "age": 40, "city": "New York"},
        {"name": "Eve", "age": 22, "city": "Paris"},
    ]


# my data
def not_list_data() -> dict:
    """Data that is not a list"""
    return {"name": "Alice", "age": 30, "city": "Paris"}


def not_list_dict_data() -> list:
    """Data that is a list but not a list of dictionaries"""
    return [
        {"name": "Alice", "age": 30, "city": "Paris"},
        {"name": "Bob", "age": 25, "city": "Paris"},
        ["champion"],
    ]


def other_type_dict_data() -> list:
    """Data that has a dictionary with a key that is not a string"""
    return [
        {"name": "Alice", "age": 30, "city": "Paris"},
        {"name": "Bob", "age": [23], "city": "Paris"},
    ]


def both_str_int_data() -> list:
    """Data that has a dictionary with a key that is both a string and an integer"""
    return [
        {"name": "Alice", "age": 30, "city": "Paris"},
        {"name": "Bob", "age": "25", "city": "Paris"},
        {"name": "Charlie", "age": 35, "city": "London"},
    ]


def not_digit() -> list:
    """Data that has a dictionary with a key that is not a digit"""
    return [
        {"name": "Alice", "age": (), "city": "Paris"},
        {"name": "Bob", "age": [], "city": "Paris"},
        {"name": "Charlie", "age": 35, "city": "London"},
        {"name": "David", "age": 40, "city": "New York"},
        {"name": "Eve", "age": "22", "city": "Paris"},
    ]


def test_filter_data(sample_data):
    """Test filter_data function"""
    result = filter_data(sample_data, "city", "Paris")
    assert len(result) == 3
    assert all(item["city"] == "Paris" for item in result)
    assert not filter_data(sample_data, 1, "city")

    # my test
    result2 = filter_data(sample_data, "name", 30)
    assert len(result2) == 0
    result3 = filter_data(sample_data, "name", "Eve")
    assert len(result3) == 1

    with pytest.raises(ValueError):
        filter_data(not_list_data(), "age", 30)
    with pytest.raises(ValueError):
        filter_data(not_list_dict_data(), "age", 30)
    with pytest.raises(ValueError):
        filter_data(sample_data, "age", [12])
    with pytest.raises(ValueError):
        filter_data(sample_data, "age", 30.0)
    with pytest.raises(ValueError):
        filter_data(sample_data, ["age2"], 30)


def test_sort_data(sample_data):
    """Test sort_data function"""
    result = sort_data(sample_data, "age")
    assert result[0]["age"] == 22
    assert result[-1]["age"] == 40
    with pytest.raises(KeyError):
        sort_data(sample_data, "country")

    # my test
    result2 = sort_data(sample_data, "name")
    assert result2[0]["name"] == "Alice"
    assert result2[1]["name"] == "Bob"
    assert result2[-1]["name"] == "Eve"

    with pytest.raises(ValueError):
        sort_data(sample_data, 1)
    with pytest.raises(ValueError):
        sort_data([], "age")
    with pytest.raises(ValueError):
        sort_data(not_list_data(), "age")
    with pytest.raises(ValueError):
        sort_data(not_list_dict_data(), "age")
    with pytest.raises(KeyError):
        sort_data(both_str_int_data(), "Hello")
    with pytest.raises(ValueError):
        sort_data(other_type_dict_data(), "age")
    with pytest.raises(ValueError):
        sort_data(both_str_int_data(), "age")


def test_complex_filter(sample_data):
    """Test complex_filter function"""
    result = complex_filter(sample_data, "age", 30)
    assert len(result) == 2
    assert all(item["age"] > 30 for item in result)
    with pytest.raises(ValueError):
        complex_filter(sample_data, "city", "Paris")

    # my test

    with pytest.raises(ValueError):
        complex_filter(not_list_data(), "age", 30)
    with pytest.raises(ValueError):
        complex_filter(not_list_dict_data(), "age", 30)
    with pytest.raises(ValueError):
        complex_filter(sample_data, 12, 30)
    with pytest.raises(ValueError):
        complex_filter(sample_data, "age", [12])
    with pytest.raises(ValueError):
        complex_filter(sample_data, "age", 30.0)
    with pytest.raises(KeyError):
        complex_filter(sample_data, "age2", 30)
    with pytest.raises(ValueError):
        complex_filter(not_digit(), "age", 30)
    with pytest.raises(ValueError):
        complex_filter(other_type_dict_data, "age", "30")


def test_aggregate_data(sample_data):
    """Test aggregate_data function"""
    result = aggregate_data(sample_data, "city")
    assert result == {"Paris": 3, "London": 1, "New York": 1}
    with pytest.raises(KeyError):
        aggregate_data(sample_data, "London")

    # my test

    with pytest.raises(ValueError):
        aggregate_data(not_list_data(), "age")
    with pytest.raises(ValueError):
        aggregate_data(not_list_dict_data(), "age")
    with pytest.raises(ValueError):
        aggregate_data(sample_data, 12)
    with pytest.raises(ValueError):
        aggregate_data(sample_data, [12])
    with pytest.raises(ValueError):
        aggregate_data(not_digit(), "age")
    with pytest.raises(KeyError):
        aggregate_data(not_digit(), "Cityland")
