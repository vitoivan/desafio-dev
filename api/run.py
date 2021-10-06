from src import create_app

app = create_app()
PORT = 3000
HOST = '0.0.0.0'

if app.config['FLASK_ENV'] == 'development':
    app.run(host=HOST, port=PORT, debug=True)