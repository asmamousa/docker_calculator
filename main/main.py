from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def add(self, a: int, b: int) -> int:
        pass

    @abstractmethod
    def sub(self, a: int, b: int) -> int:
        pass

    @abstractmethod
    def multiply(self, a: int, b: int) -> int:
        pass

    @abstractmethod
    def divide(self, a: int, b: int) -> int:
        pass


class BasicCalculator(Calculator):
    def add(self, a: int, b: int) -> int:
        return a + b

    def sub(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> int:
        return a // b


class CalculatorDecorator(Calculator):
    def __init__(self, calculator: Calculator):
        self._calculator = calculator

    def add(self, a: int, b: int) -> int:
        return self._calculator.add(a, b)

    def sub(self, a: int, b: int) -> int:
        return self._calculator.sub(a, b)

    def multiply(self, a: int, b: int) -> int:
        return self._calculator.multiply(a, b)

    def divide(self, a: int, b: int) -> int:
        return self._calculator.divide(a, b)


class PrinterDecorator(CalculatorDecorator):
    def add(self, a: int, b: int) -> int:
        result = super().add(a, b)
        print(f'the result of adding {a},{b} is {result}')
        return result

    def sub(self, a: int, b: int) -> int:
        result = super().sub(a, b)
        print(f'the result of subtracting {a},{b} is {result}')
        return result

    def multiply(self, a: int, b: int) -> int:
        result = super().multiply(a, b)
        print(f'the result of multiplying {a},{b} is {result}')
        return result

    def divide(self, a: int, b: int) -> int:
        result = super().divide(a, b)
        print(f'the result of division of {a},{b} is {result}')
        return result


basic_cal = BasicCalculator()
printer_cal = PrinterDecorator(basic_cal)


printer_cal.add(15, 5)
printer_cal.sub(15, 5)
printer_cal.multiply(10, 5)
printer_cal.divide(10, 5)
