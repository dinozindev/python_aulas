from flask import Flask, jsonify, request

app = Flask(__name__)

dados = [{"id": 1, "nome": "Produto 1", "preco": 50},
         {"id": 2, "nome": "Produto 2", "preco": 150}]