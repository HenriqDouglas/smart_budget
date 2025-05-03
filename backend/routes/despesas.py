from flask import request, jsonify
from database import SessionLocal
from models.despesa import Despesa
from datetime import datetime

def register_despesa_routes(app):
    @app.route('/api/despesas', methods=['GET'])
    def listar_despesas():
        session = SessionLocal()
        despesas = session.query(Despesa).all()
        resultado = [
            {
                'id': d.id,
                'descricao': d.descricao,
                'valor': d.valor,
                'data': d.data.strftime('%Y-%m-%d'),
                'categoria': d.categoria
            } for d in despesas
        ]
        session.close()
        return jsonify(resultado)

    @app.route('/api/despesas', methods=['POST'])
    def criar_despesa():
        data = request.json
        session = SessionLocal()
        nova = Despesa(
            descricao=data['descricao'],
            valor=float(data['valor']),
            data=datetime.strptime(data['data'], '%Y-%m-%d'),
            categoria=data['categoria']
        )
        session.add(nova)
        session.commit()
        session.close()
        return jsonify({'mensagem': 'Despesa criada com sucesso!'}), 201
from flask import request, jsonify
from database import SessionLocal
from models.despesa import Despesa
from datetime import datetime

def register_despesa_routes(app):
    @app.route('/api/despesas', methods=['GET'])
    def listar_despesas():
        session = SessionLocal()
        despesas = session.query(Despesa).all()
        resultado = [
            {
                'id': d.id,
                'descricao': d.descricao,
                'valor': d.valor,
                'data': d.data.strftime('%Y-%m-%d'),
                'categoria': d.categoria
            } for d in despesas
        ]
        session.close()
        return jsonify(resultado)

    @app.route('/api/despesas', methods=['POST'])
    def criar_despesa():
        data = request.json
        session = SessionLocal()
        nova = Despesa(
            descricao=data['descricao'],
            valor=float(data['valor']),
            data=datetime.strptime(data['data'], '%Y-%m-%d'),
            categoria=data['categoria']
        )
        session.add(nova)
        session.commit()
        session.close()
        return jsonify({'mensagem': 'Despesa criada com sucesso!'}), 201
