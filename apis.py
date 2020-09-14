from flask import Flask, jsonify
from flask_restful import Resource, Api
import pyodbc
from sql_helper import SQL_Helper as sql

class HelloWorld(Resource):
    def get(self):
        get_product_qry = "select * from products"
        product_data = sql.select_one(self,get_product_qry)
        print(type(product_data))
        print(product_data)
        return jsonify({"status":200,'body': product_data })

class GetProducts(Resource):
    def get(self):
        get_product_qry = "select * from products"
        product_data = sql.select_all(self,get_product_qry)
        print(type(product_data))
        print(product_data)
        return jsonify({"status":200,'body': product_data })