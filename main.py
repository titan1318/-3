def mask_card(card_number):
    return ' '.join(['XXXX XXXX XXXX ' + card_number[-4:]] if card_number else [])


def mask_account(account_number):
    return '**** ' + account_number[-4:]


def format_operation(operation):
    date = datetime.fromisoformat(operation['date'][:-1]).strftime('%d.%m.%Y')
    description = operation['description']
    from_account = mask_card(operation['from']) if 'from' in operation else 'Внутренний перевод'
    to_account = mask_account(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']

    return f"{date} {description}\n{from_account} -> {to_account}\n{amount} {currency}"


def display_last_operations(operations):
    executed_operations = [op for op in operations if op['state'] == 'EXECUTED']
    last_operations = executed_operations[-5:][::-1]  # последние 5, в обратном порядке

    for operation in last_operations:
        print(format_operation(operation))
        print()  # пустая строка между операциями


# Пример вызова
display_last_operations(operations)
