# Функция выполняющая поиск простых чисел до заданного методов решета Эрастофена
# вход - число, выход - массив простых чисел до входного
def sieve(n):
    a = [i for i in range(n + 1)]
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    return list(a)


# Функция сортирующая массив пузырьком
# вход - массив, выход - отсортированный массив
def bubble(n):
    for i in range(len(n)):
        for j in range(len(n) - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
    return n


# Функция реализующая логику калькулятора
# вход - (число, число, операция (текстовым символом)), выход - число
def calc(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "/":
        return a / b
    elif operation == "*":
        return a * b
    else:
        return "ERROR"
