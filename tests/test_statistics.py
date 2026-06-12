import pytest

from ep5_actions import amplitude, mean, median, min_max_normalize


def test_mean_calculates_average():
    assert mean([10, 20, 30, 40]) == 25


def test_median_with_odd_amount_of_values():
    assert median([9, 1, 5]) == 5


def test_median_with_even_amount_of_values():
    assert median([10, 2, 8, 4]) == 6


def test_amplitude_uses_minimum_and_maximum_values():
    assert amplitude([-3, 7, 10, 2]) == 13


def test_min_max_normalize_scales_values_between_zero_and_one():
    assert min_max_normalize([10, 20, 30]) == [0.0, 0.5, 1.0]


def test_min_max_normalize_handles_repeated_values():
    assert min_max_normalize([4, 4, 4]) == [0.0, 0.0, 0.0]


def test_empty_values_raise_value_error():
    with pytest.raises(ValueError, match="nao pode estar vazia"):
        mean([])
