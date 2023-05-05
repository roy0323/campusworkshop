"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaabee7avj5o48ja3h0-a.oregon-postgres.render.com",
        database="todo_4527",
        user="root",
        password="2B7FgQctd6nSEz7tnof6U8taQ62yHB5q "
        )
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
