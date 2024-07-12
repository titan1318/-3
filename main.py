import json
from datetime import datetime

def load_operations_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def mask_card_number(card_number):
    parts = card_number.split()
    return f"{parts[0]} {parts[1][:2]}** **** {parts[3]}"

def mask_account_number(account_number):
    return f"**{account_number[-4:]}"

def format_date(date_string):
    date = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')
    return date.strftime('%d.%m.%Y')

def get_last_operations(operations):
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return sorted_operations[:5]

def format_operation(operation):
    formatted_date = format_date(operation['date'])
    masked_from = mask_card_number(operation['from']) if 'from' in operation else 'N/A'
    masked_to = mask_account_number(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    description = operation['description']

    return f"{formatted_date} {description}\n{masked_from} -> {masked_to}\n{amount} {currency}\n"

def main():
    operations = load_operations_from_file('operations.json')
    last_operations = get_last_operations(operations)
    for operation in last_operations:
        formatted_output = format_operation(operation)
        print(formatted_output)

if __name__ == '__main__':
    main()
