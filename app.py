from flask import Flask, jsonify
from flask_restful import Resource, Api
import pyodbc
import configparser
from apis import *

config = configparser.ConfigParser()
config.read('config.ini')

server = config['CONNECTION']['HOST']
database = config['CONNECTION']['DATABASE']
username = config['CONNECTION']['USER'] 
password = config['CONNECTION']['PASS']
driver = config['CONNECTION']['DRIVER']
cnxn = pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


app = Flask(__name__)
api = Api(app)

# def select_all(query_string):
#     cursor.execute(query_string)
#     columns = [column[0] for column in cursor.description]
#     result = []
#     for row in cursor.fetchall():
#             result.append(dict(zip(columns, row)))
    
#     return result

# def select_one(query_string):
#     cursor.execute(query_string)
#     columns = [column[0] for column in cursor.description]
#     result = []
#     for row in cursor.fetchall():
#             result.append(dict(zip(columns, row)))
    
#     return result[0]
    



api.add_resource(GetProducts, '/products')

if __name__ == '__main__':
    app.run(debug=True)