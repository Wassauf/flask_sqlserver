from flask import Flask, jsonify
from flask_restful import Resource, Api
import pyodbc
import configparser
from apis import *

app = Flask(__name__)
api = Api(app)

api.add_resource(GetProduct, '/products/<int:product_id>')
api.add_resource(GetProducts, '/products')
api.add_resource(AddProduct, '/product_add')
api.add_resource(CreaateUser,'/new_user')


if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0')