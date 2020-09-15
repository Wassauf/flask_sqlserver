import pyodbc
import configparser

class SQL_Helper:
        
    def init(self):
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

    def select_one(self,query_string):
        # config = configparser.ConfigParser()
        # config.read('config.ini')

        # server = config['CONNECTION']['HOST']
        # database = config['CONNECTION']['DATABASE']
        # username = config['CONNECTION']['USER'] 
        # password = config['CONNECTION']['PASS']
        # driver = config['CONNECTION']['DRIVER']
        # cnxn = pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # cursor = cnxn.cursor()
        cnxn, cursor = SQL_Helper.init(self)
        cursor.execute(query_string)
        columns = [column[0] for column in cursor.description]
        result = []
        for row in cursor.fetchall():
                result.append(dict(zip(columns, row)))

        cursor.close()
        cnxn.close()
        
        return result[0]
    
    def select_all(self,query_string):
        # config = configparser.ConfigParser()
        # config.read('config.ini')

        # server = config['CONNECTION']['HOST']
        # database = config['CONNECTION']['DATABASE']
        # username = config['CONNECTION']['USER'] 
        # password = config['CONNECTION']['PASS']
        # driver = config['CONNECTION']['DRIVER']
        # cnxn = pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # cursor = cnxn.cursor()
        cnxn, cursor = SQL_Helper.init(self)
        cursor.execute(query_string)
        columns = [column[0] for column in cursor.description]
        result = []
        for row in cursor.fetchall():
                result.append(dict(zip(columns, row)))

        cursor.close()
        cnxn.close()
        
        return result
    
    def insert_update(self,query_string):
        cnxn, cursor = SQL_Helper.init(self)
        cursor.execute(query_string)
        cnxn.commit()
        cursor.close()
        cnxn.close()