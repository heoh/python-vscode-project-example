import pytest
from project.core.calculator import Calculator


@pytest.fixture
def calculator() -> Calculator:
    calculator = Calculator()
    calculator.value = 1
    return calculator


def test_add_positive_value(calculator: Calculator):
    calculator.add(5)
    assert calculator.value == 6


def test_add_negative_value(calculator: Calculator):
    calculator.add(-3)
    assert calculator.value == -2


def test_multiply(calculator: Calculator):
    assert calculator.multiply(2).value == 2


def test_complex(calculator: Calculator):
    assert calculator.add(2).multiply(3).add(1).value == 10
