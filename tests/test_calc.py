import pytest
from src import ma_lib


# тест функции осуществляющей логику калькулятора
class TestCalc:
    # Проверка, суммирования двух чисел типа int
    def test_addition(self):
        assert ma_lib.calc(2, 4, "+") == 6

    # Проверка, вычитания двух чисел типа int
    def test_subtraction(self):
        assert ma_lib.calc(10, 4, "-") == 6

    # Проверка, деления двух чисел типа int
    def test_division(self):
        assert ma_lib.calc(36, 6, "/") == 6

    # Проверка, умножения двух чисел типа int
    def test_multiplication(self):
        assert ma_lib.calc(2, 3, "*") == 6

    # Проверка, ввода некорректной математической операции
    def test_unknown_action(self):
        assert ma_lib.calc(2, 3, "^") == "ERROR"

    # Проверка, что при делении на ноль программа даст ошибку ZeroDivisionError
    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            ma_lib.calc(1, 0, "/")

    # Проверка, что при попытке разделить str на int программа даст ошибку TypeError
    def test_invaild_input_1(self):
        with pytest.raises(TypeError):
            ma_lib.calc("a", 2, "/")

    # Проверка, что при попытке разделить int на str программа даст ошибку TypeError
    def test_invaild_input_2(self):
        with pytest.raises(TypeError):
            ma_lib.calc(1, "b", "/")

    # Проверка, конкатенации двух строк
    def test_concat_strings(self):
        assert ma_lib.calc("a", "b", "+") == "ab"

    # Проверка, что при попытке сложить int и str программа даст ошибку TypeError
    def test_concat_strin_and_int(self):
        with pytest.raises(TypeError):
            ma_lib.calc(1, "b", "+")

    # Проверка, что при попытке умножить str на str программа даст ошибку TypeError
    def test_multiply_strings(self):
        with pytest.raises(TypeError):
            ma_lib.calc("a", "b", "*")

    # Проверка умножения str на int
    def test_multiply_string_and_int(self):
        assert ma_lib.calc(5, "b", "*") == "bbbbb"

    # Проверка, что при попытке вычесть str из str программа даст ошибку TypeError
    def test_division_strings(self):
        with pytest.raises(TypeError):
            ma_lib.calc("a", "b", "-")

    # Проверка, что при попытке вычесть int из str программа даст ошибку TypeError
    def test_division_string_and_int(self):
        with pytest.raises(TypeError):
            ma_lib.calc("a", 5, "-")
