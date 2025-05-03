from .despesas import register_despesa_routes

def init_routes(app):
    register_despesa_routes(app)

    @app.route('/api/ping')
    def ping():
        return {'message': 'API está funcionando'}
