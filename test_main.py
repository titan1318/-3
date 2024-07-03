import json
from datetime import datetime

# Функция для чтения данных из файла
def read_operations(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        operations = json.load(file)
    return operations

# Функция для маскирования номера карты
def mask_card_number(card_number):
    parts = card_number.split()
    return f"{parts[0]} {parts[1][:2]}** **** {parts[3]}"

# Функция для маскирования номера счета
def mask_account_number(account_number):
    return f"**{account_number[-4:]}"

# Функция для форматирования даты
def format_date(date_str):
    date = datetime.fromisoformat(date_str[:-1])
    return date.strftime("%d.%m.%Y")

# Основная функция для получения и форматирования последних операций
def get_last_operations(operations, count=5):
    executed_operations = [op for op in operations if op['state'] == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)
    last_operations = sorted_operations[:count]

    formatted_operations = []
    for op in last_operations:
        date = format_date(op['date'])
        description = op['description']
        from_account = mask_card_number(op['from']) if 'from' in op else 'N/A'
        to_account = mask_account_number(op['to'])
        amount = f"{op['operationAmount']['amount']} {op['operationAmount']['currency']['name']}"
        formatted_operations.append(f"{date} {description}\n{from_account} -> {to_account}\n{amount}\n")

    return '\n'.join(formatted_operations)

# Пример использования
if __name__ == "__main__":
    operations = read_operations('operations.json')
    print(get_last_operations(operations))
