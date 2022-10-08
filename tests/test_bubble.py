import pytest
import ma_lib


# тест функции осуществляющей сортировку пузырьком по возрастанию
class TestBubble:
    # Данные для проверки (отсортированный массив)
    @pytest.fixture
    def correct_example(self):
        return [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Данные для проверки (не отсортированная строка)
    @pytest.fixture
    def incorrect_example(self):
        return [5, 2, 9, 4, 6, 1, 7, 8, 3]

    # Данные для проверки (массив одинаковых значений)
    @pytest.fixture
    def equal_example(self):
        return [1, 1, 1, 1, 1, 1, 1, 1, 1]

    # Данные для проверки (массив строк)
    @pytest.fixture
    def mas_of_str_example(self):
        return ["1", "2", "п", "4", "5", "6", "е", "8", "9"]

    # Данные для проверки (массив стрко и чисел)
    @pytest.fixture
    def one_str_in_mas_example(self):
        return [1, 2, 3, 4, 5, 6, 7, 8, "9"]

    # Проверка сортировки отсортированного массива
    def test_correct(self, correct_example):
        assert ma_lib.bubble(correct_example) == correct_example

    # Проверка сортировки не отсортированного массива
    def test_incorrect(self, incorrect_example):
        assert ma_lib.bubble(incorrect_example.copy()) != incorrect_example

    # Проверка сортировки массива одинаковых чисел
    def test_equal(self, equal_example):
        assert ma_lib.bubble(equal_example) == equal_example

    # Проверка сортировки массива строк
    def test_invalid_input_1(self, mas_of_str_example):
        assert ma_lib.bubble(mas_of_str_example) == mas_of_str_example

    # Проверка, что при сортировке массива в котором есть числа и строки программа даст ошибку TypeError
    def test_invalid_input_2(self, one_str_in_mas_example):
        with pytest.raises(TypeError):
            ma_lib.bubble(one_str_in_mas_example)

