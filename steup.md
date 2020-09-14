
## 1. Create a Virtual Environment using commands

####  pip install virtualenv
####  virtualenv venv

## 2. Activate virtual Environment

### On macOS and Linux:
source venv/bin/activate

### On Windows:
.\venv\Scripts\activate

## 3. Install deoendencies
#### pip install pyodbc
#### pip install flask_restful

## 4. Create a config file with name 'config.ini'
### copy the following content into that config file with filled information and remove <> 

[CONNECTION]
#### DRIVER = ODBC Driver 17 for SQL Server
#### DATABASE = <Database Name>
#### HOST = <SQLServer Address>
#### USER = <username>
#### PASS = <password>
#### PORT = <leave the empty> 
