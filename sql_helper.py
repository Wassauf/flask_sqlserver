import pyodbc
import configparser

class SQL_Helper:
        
    @staticmethod
    def init():
        config = configparser.ConfigParser()
        config.read('config.ini')

        server = config['CONNECTION']['HOST']
        database = config['CONNECTION']['DATABASE']
        username = config['CONNECTION']['USER'] 
        password = config['CONNECTION']['PASS']
        driver = config['CONNECTION']['DRIVER']
        cnxn = pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        return cnxn,cursor

    @staticmethod
    def select_one(query_string):

        cnxn, cursor = SQL_Helper.init()
        cursor.execute(query_string)
        columns = [column[0] for column in cursor.description]
        result = []
        for row in cursor.fetchall():
                result.append(dict(zip(columns, row)))

        cursor.close()
        cnxn.close()
        if len(result) > 0:
            return result[0]
        else: 
            return None

    @staticmethod
    def select_all(query_string):

        cnxn, cursor = SQL_Helper.init()
        cursor.execute(query_string)
        columns = [column[0] for column in cursor.description]
        result = []
        for row in cursor.fetchall():
                result.append(dict(zip(columns, row)))

        cursor.close()
        cnxn.close()
        
        return result

    @staticmethod
    def insert_update(query_string):
        cnxn, cursor = SQL_Helper.init()
        cursor.execute(query_string)
        cnxn.commit()
        cursor.close()
        cnxn.close()