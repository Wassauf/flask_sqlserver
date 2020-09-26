from flask import Flask, jsonify
from flask_restful import Resource, Api, fields, reqparse,request
import pyodbc
from sql_helper import SQL_Helper as sql
from passlib.hash import pbkdf2_sha256

# product_post_args = reqparse.RequestParser()
# product_post_args.add_argument("product_name", type=str, help="Name of the Product")
# product_post_args.add_argument("price", type=float, help="Price of the Product")


class GetProduct(Resource):
    def get(self,product_id):
        get_product_qry = "select * from products where id = "+ str(product_id)
        product_data = sql.select_one(get_product_qry)
        # print(type(product_data))
        # print(product_data)
        if product_data == None:
            print("NOnenenennenne")
            return jsonify({"status":404,'message': "Not Found" })
        else:
            return jsonify({"status":200,'body': product_data })

class GetProducts(Resource):
    def get(self):
        get_product_qry = "select * from products"
        product_data = sql.select_all(get_product_qry)
        return jsonify({"status":200,'body': product_data })

class AddProduct(Resource):
    def post(self):
        # args = product_post_args.parse_args()
        # print(args["product_name"], args["price"])
        # return args, S201
        # args = parser.parse_args()
        
        json_data = request.get_json(force=True)
        data_exists_qry = "select * from products where product_name = '"+str(json_data["product_name"])+"' and price = "+str(json_data["price"])
        data = sql.select_one(data_exists_qry)
        if data == None:
            insert_product_qry = "Insert into products(product_name,price) values ('"+str(json_data["product_name"])+"',"+str(json_data["price"])+");"
            sql.insert_update(insert_product_qry)
            return jsonify({"status":201,"body":json_data})       
        else:
            return jsonify({"status":406, "message" : "Already exists"})
        pass

class CreaateUser(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        
        if json_data != None: 
            print(json_data.keys())
            # if "email" in list(json_data.keys()):
            try:
                if "username" in json_data and "password" in json_data and "email" in json_data:
                    first_name = json_data["first_name"]
                    last_name = json_data["last_name"]
                    username = json_data["username"]
                    password = json_data["password"]
                    email = json_data["email"]
                    # print(username,password,email)
                    hash = pbkdf2_sha256.hash(password)
                    
                    createuser_qry = f"insert into authenticated_users (first_name,last_name,username,password,is_active,email,date_joined,is_superuser) values ( '{first_name}','{last_name}','{username}','{hash}','0', '{email}',getutcdate(),0)"
                    print(createuser_qry)
                    sql.insert_update(createuser_qry)
                    return jsonify({ "status": 201 ,"body":{"username":username,"message":"User Created"}})
                else: 
                    return jsonify({"message":"API expects keys username, password, and email"})

            except Exception as e:
                return jsonify({"message":"API expects keys username, password, and email"})
                pass
                
