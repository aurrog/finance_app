from flask import Flask, request, jsonify
from models import add_transaction, get_transactions, delete_transaction

app = Flask(__name__)

@app.route('/transactions', methods=['GET'])
def get_transactions_route():
    transactions = get_transactions()
    return jsonify(transactions)

@app.route('/transactions', methods=['POST'])
def add_transaction_route():
    data = request.json
    add_transaction(data['type'], data['amount'], data['description'])
    return jsonify({"status": "success"})

@app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction_route(transaction_id):
    delete_transaction(transaction_id)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
