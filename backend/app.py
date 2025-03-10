from flask import Flask, request, jsonify
from models import add_transaction, get_transactions, delete_transaction, get_transaction_by_id, update_transaction
import logging

app = Flask(__name__)


logging.basicConfig(
    level=logging.DEBUG,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат логов
    handlers=[
        logging.FileHandler('app.log'),  # Запись логов в файл
        logging.StreamHandler()  # Вывод логов в консоль
    ]
)

logger = logging.getLogger(__name__)

@app.route('/')
def home():
    print("Request received from:", request.remote_addr)
    return '<h1>Developer telegram: aurrog</h1>'


@app.route('/transactions', methods=['GET'])
def get_transactions_route():
    print("Request received from:", request.remote_addr)
    logger.info('Получен GET-запрос на /transactions')
    transactions = get_transactions()
    return jsonify(transactions)


@app.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_single_transaction_route(transaction_id):
    transaction = get_transaction_by_id(transaction_id)
    if transaction:
        return jsonify(transaction)
    return jsonify({"error": "Transaction not found"}), 404


@app.route('/transactions', methods=['POST'])
def add_transaction_route():
    data = request.json
    logger.info(f'Получен POST-запрос на /transactions: {data}')
    add_transaction(data['type'], data['amount'], data['description'], data['date'])
    return jsonify({"status": "success"})


@app.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction_route(transaction_id):
    data = request.json
    logger.info(f'Получен PUT-запрос на /transactions по id {transaction_id}')
    update_transaction(transaction_id, data['type'], data['amount'], data['description'], data['date'])
    return jsonify({"status": "success"})


@app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction_route(transaction_id):
    logger.info(f'Получен DELETE-запрос на /transactions по id {transaction_id}')
    delete_transaction(transaction_id)
    return jsonify({"status": "success"})


if __name__ == '__main__':
    logger.info('Запуск приложения')
    app.run(debug=True)