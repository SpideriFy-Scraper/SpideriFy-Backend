from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resources.product import FakeProduct
from common.db import db
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV'] == 'development':
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.TestingConfig')


api = Api(app)


# api.add_resource(Product, '/api/v1/<string:username>/product/<string:asin>')
# api.add_resource(ProductList, '/api/v1/<string:username>/product')
# api.add_resource(CommentList, '/api/v1/<string:username>/<string:asin>/comment')

api.add_resource(FakeProduct, '/api/v1/product')


if __name__ == '__main__':
    db.init_app(app)
    app.run(host='0.0.0.0', port=8080)
