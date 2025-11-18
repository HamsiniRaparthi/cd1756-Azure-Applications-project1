import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') 
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') 
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') 

    # SQL Database
    SQL_SERVER = os.environ.get('SQL_SERVER') 
    SQL_DATABASE = os.environ.get('SQL_DATABASE') 
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') 
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') 

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#
    # Microsoft Authentication
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'ToG8Q~kyqKjFQGz7ZpcgTWRUTKgZTSvrF~y70cpv'

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "64e5b0a4-088a-440a-967a-871f16d5b039"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-sidesession
