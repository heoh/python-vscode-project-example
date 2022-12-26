from __future__ import annotations


class Calculator:
    def __init__(self) -> None:
        self.value = 0

    def add(self, value: int) -> Calculator:
        self.value += value
        return self

    def multiply(self, value: int) -> Calculator:
        self.value *= value
        return self
