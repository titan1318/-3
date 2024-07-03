import pytest
from main import mask_card_number, mask_account_number, format_date, get_last_operations

# Тест для функции маскирования номера карты
def test_mask_card_number():
    assert mask_card_number("Visa Platinum 7000 1234 5678 9012") == "Visa Platinum 70** **** 9012"

# Тест для функции маскирования номера счета
def test_mask_account_number():
    assert mask_account_number("Счет 12345678") == "**5678"

# Тест для функции форматирования даты
def test_format_date():
    assert format_date("2018-10-14T00:00:00.000") == "14.10.2018"

# Тест для функции получения последних операций
def test_get_last_operations():
    operations = [
        {
            "id": 1,
            "date": "2023-07-01T00:00:00.000",
            "state": "EXECUTED",
            "operationAmount": {"amount": "5000", "currency": {"name": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 7000 1234 5678 9012",
            "to": "Счет 12345678"
        },
        # Добавить еще несколько операций для тестирования
    ]
    result = get_last_operations(operations, count=1)
    assert "01.07.2023 Перевод организации" in result

# Запуск тестов
if __name__ == "__main__":
    pytest.main()
