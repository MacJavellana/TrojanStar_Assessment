import os

class Config:
#    SQLALCHEMY_DATABASE_URI = os.getenv('localhost\\SQLEXPRESS', 'mssql+pyodbc://sa:testdb@localhost\\SQLEXPRESS/RecipeAppDB?driver=ODBC+Driver+17+for+SQL+Server')
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:YourStrong!Passw0rd@db/RecipeAppDB?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
