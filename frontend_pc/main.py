import requests


def get_transactions():
    response = requests.get('http://127.0.0.1:5000/transactions')
    if response.status_code == 200:
        transactions = response.json()
        print(transactions)
    else:
        print('Ошибка при выполнении запроса GET')


def add_transaction(transaction_type, amount, description):
    data = {
        'type': transaction_type,
        'amount': float(amount),
        'description': description
    }
    response = requests.post('http://127.0.0.1:5000/transactions', json=data)
    if response.status_code == 200:
        print('Запись добавлена')
    else:
        print('Ошибка при выполнении запроса POST')


def delete_transaction(transaction_id):
    response = requests.get(f'http://127.0.0.1:5000/transactions/<{transaction_id}>')
    if response.status_code == 200:
        print('Запись успешно добавлена')
    else:
        print('Ошибка при выполнении запроса DELETE')



while True:
    user_input = input('Введите команду POST или GET. Для выхода нажмите Q: ')
    if user_input == 'Q':
        break
    elif user_input == 'GET':
        get_transactions()
    elif user_input == 'POST':
        input_data = input('type;amount;description: ').split(';')
        add_transaction(*input_data)
    else:
        print('Неверный запрос')