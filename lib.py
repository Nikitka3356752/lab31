# Функция для определения n чисел Фибоначчи с обработкой ошибок
def fibonacci(n):
    if not isinstance(n, int):  # Проверка, что n — это целое число
        raise TypeError("n должно быть целым числом")
    if n < 0:  # Проверка, что n не отрицательное
        raise ValueError("n не может быть отрицательным")

    list = []
    a, b = 0, 1
    for _ in range(n):
        list.append(a)
        a, b = b, a + b
    return list


# Функция сортировки пузырьком с обработкой ошибок
def bubble(lst):
    if not isinstance(lst, list):  # Проверка, что передан список
        raise TypeError("Аргумент должен быть списком")

    if not all(isinstance(i, (int, float)) for i in lst):  # Проверка, что все элементы числовые
        raise TypeError("Список должен содержать только числа")

    sort = lst.copy()  # создаем копию списка, чтобы не изменять оригинал
    n = len(sort)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sort[j] > sort[j + 1]:
                sort[j], sort[j + 1] = sort[j + 1], sort[j]
    return sort


# Функция калькулятора с обработкой ошибок
def calculator(num1, num2, operation):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):  # Проверка типов данных
        raise TypeError("Оба аргумента должны быть числами")

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Ошибка: деление на ноль"
        return num1 / num2
    else:
        return "Неподдерживаемая операция"
