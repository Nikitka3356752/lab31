import pytest
from lib import fibonacci, bubble, calculator

# Тесты для функции fibonacci
def test_fibonacci_valid():
    assert fibonacci(0) == []  # Граничное значение: n = 0
    assert fibonacci(1) == [0]  # Граничное значение: n = 1
    assert fibonacci(5) == [0, 1, 1, 2, 3]  # Валидный класс

def test_fibonacci_invalid():
    with pytest.raises(TypeError):
        fibonacci("5")  # Некорректный тип данных: строка вместо целого числа
    with pytest.raises(ValueError):
        fibonacci(-5)  # Некорректное значение: отрицательное число

# Тесты для функции bubble
def test_bubble_valid():
    assert bubble([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]  # Валидный класс
    assert bubble([1]) == [1]  # Граничное значение: список с одним элементом
    assert bubble([]) == []  # Граничное значение: пустой список

def test_bubble_invalid():
    with pytest.raises(TypeError):
        bubble("not a list")  # Некорректный тип данных: строка вместо списка
    with pytest.raises(TypeError):
        bubble([1, "string", 3])  # Некорректные данные: список с нечисловыми элементами

# Тесты для функции calculator
def test_calculator_valid():
    assert calculator(10, 5, '+') == 15  # Валидное значение для сложения
    assert calculator(10, 5, '-') == 5  # Валидное значение для вычитания
    assert calculator(10, 5, '*') == 50  # Валидное значение для умножения
    assert calculator(10, 5, '/') == 2  # Валидное значение для деления

def test_calculator_invalid():
    assert calculator(10, 0, '/') == "Ошибка: деление на ноль"  # Деление на ноль: обработка ошибки
    assert calculator(10, 5, '%') == "Неподдерживаемая операция"  # Некорректная операция
    with pytest.raises(TypeError):
        calculator("10", 5, '+')  # Некорректный тип данных: строка вместо числа
        calculator(10, "5", '+')  # Некорректный тип данных: строка вместо числа
