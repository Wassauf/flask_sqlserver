from flask import Flask, jsonify
from flask_restful import Resource, Api, fields, reqparse,request
import pyodbc
from sql_helper import SQL_Helper as sql


# product_post_args = reqparse.RequestParser()
# product_post_args.add_argument("product_name", type=str, help="Name of the Product")
# product_post_args.add_argument("price", type=float, help="Price of the Product")


class GetProduct(Resource):
    def get(self,product_id):
        get_product_qry = "select * from products where id = "+ str(product_id)
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

class AddProduct(Resource):
    def post(self):
        # args = product_post_args.parse_args()
        # print(args["product_name"], args["price"])
        # return args, S201
        # args = parser.parse_args()
        
        json_data = request.get_json(force=True)
        insert_product_qry = "Insert into products(product_name,price) values ('"+str(json_data["product_name"])+"',"+str(json_data["price"])+");"
        sql.insert_update(self,insert_product_qry)
        return jsonify({"status":201,"body":json_data})       
        pass
