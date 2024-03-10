from datetime import datetime
from flask import Flask, render_template, request, session, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'portfolio'

db = MySQL(app)

@app.route("/")
def projects_page():
  cursor = db.connection.cursor()
  cursor.execute("SELECT img_file FROM projects")
  projects = cursor.fetchall()
  for project in projects:
    print(project)

  return "hello"


app.run()