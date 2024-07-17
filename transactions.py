from datetime import datetime


def mask_account(account):
    return f"**{account[-4:]}"


def mask_card(card):
    return " ".join([card[:6], "****", "****", card[-4:]])


def print_last_transactions(transactions, n=5):
    executed_transactions = [
        t for t in transactions
        if t.get("state") == "EXECUTED"
    ]

    last_transactions = sorted(executed_transactions, key=lambda x: x["date"], reverse=True)[:n]

    for transaction in last_transactions:
        # Обновленный формат даты
        date = datetime.strptime(transaction['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        print(f"{date} {transaction['description']}")

        if "from" in transaction:
            print(f"{mask_card(transaction['from'])} -> {mask_account(transaction['to'])}")
        else:
            print(f"-> {mask_account(transaction['to'])}")

        amount = transaction['operationAmount']['amount']
        currency = transaction['operationAmount']['currency']
        print(f"{amount} {currency}\n")

