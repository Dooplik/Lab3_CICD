import pytest
from src import ma_lib


# тест функции выполняющей поиск простых чисел до заданного
class TestSieve:
    # Тест корректности выполнения программы по поиску простых чисел до заданного
    def test_on_correct_n(self):
        assert ma_lib.sieve(15) == [2, 3, 5, 7, 11, 13]

    # Проверка, что при вводу нуля программа даст ошибку IndexError
    def test_on_zero(self):
        with pytest.raises(IndexError):
            ma_lib.sieve(0)

    # Проверка, что при вводу строки программа даст ошибку TypeError
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            ma_lib.sieve("f")
