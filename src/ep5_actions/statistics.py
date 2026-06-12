"""Pequenas funcoes estatisticas para demonstrar testes automatizados."""

from collections.abc import Iterable


def _to_number_list(values: Iterable[float]) -> list[float]:
    numbers = list(values)
    if not numbers:
        raise ValueError("a lista de valores nao pode estar vazia")
    return numbers


def mean(values: Iterable[float]) -> float:
    """Retorna a media aritmetica dos valores."""
    numbers = _to_number_list(values)
    return sum(numbers) / len(numbers)


def median(values: Iterable[float]) -> float:
    """Retorna a mediana dos valores."""
    numbers = sorted(_to_number_list(values))
    middle = len(numbers) // 2

    if len(numbers) % 2 == 1:
        return numbers[middle]

    return (numbers[middle - 1] + numbers[middle]) / 2


def amplitude(values: Iterable[float]) -> float:
    """Retorna a diferenca entre o maior e o menor valor."""
    numbers = _to_number_list(values)
    return max(numbers) - min(numbers)


def min_max_normalize(values: Iterable[float]) -> list[float]:
    """Normaliza valores para a faixa de 0 a 1."""
    numbers = _to_number_list(values)
    minimum = min(numbers)
    maximum = max(numbers)

    if minimum == maximum:
        return [0.0 for _ in numbers]

    return [(number - minimum) / (maximum - minimum) for number in numbers]
