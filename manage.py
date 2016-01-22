#!/usr/bin/env python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from peewee import SqliteDatabase, Model, CharField, create_model_tables


app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SqliteDatabase('data.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField


@app.before_request
def db_connect():
    db.connect()


@app.teardown_request
def db_close(exc):
    if not db.is_closed():
        db.close()


models = [User]
create_model_tables(models, fail_silently=True)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.debug = True
    app.reload = True
    app.run(host='0.0.0.0')
