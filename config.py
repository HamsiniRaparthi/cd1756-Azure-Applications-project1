import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or'images11hams'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')  
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # SQL Database
    SQL_SERVER = 'cms-server-09-sqlserver.database.windows.net' or os.environ.get('SQL_SERVER')
    SQL_DATABASE = 'cms-server-1122' or os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = 'cmsadmin' or os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = 'CMS4admin' or  os.environ.get('SQL_PASSWORD')
    SQL_PASSWORD_ENC = quote_plus(SQL_PASSWORD)

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD_ENC}@{SQL_SERVER}:1433/"
        f"{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')  # keep secret in Azure

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "f820762c-91bc-420c-a088-395db79e9e1d"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
