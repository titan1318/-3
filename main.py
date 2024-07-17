import json
from transactions import print_last_transactions

# Загрузка данных из файла
def load_transactions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

if __name__ == "__main__":
    transactions = load_transactions('operations.json')
    print_last_transactions(transactions)
