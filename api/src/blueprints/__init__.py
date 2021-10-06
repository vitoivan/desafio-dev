from flask import Flask

def init_app(app: Flask):

    from .bp_transaction import transaction_bp
    app.register_blueprint(transaction_bp)