#!/usr/bin/env python

from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
from flask_bootstrap import Bootstrap
from flask_security import (
    Security,
    PeeweeUserDatastore,
    UserMixin,
    RoleMixin,
    login_required,
)
from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    TextField,
    BooleanField,
    DateTimeField,
    ForeignKeyField,
    create_model_tables,
)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'iP4Yey6wd9su7cWtcS2urH0h1qWRCmP7Quakzg04k616wzAy4'
bootstrap = Bootstrap(app)
db = SqliteDatabase('data.db')
admin = Admin(app, name='tilda', template_mode='bootstrap3')


class BaseModel(Model):
    class Meta:
        database = db


class Role(BaseModel, RoleMixin):
    name = CharField(unique=True)
    description = TextField(null=True)


class User(BaseModel, UserMixin):
    email = TextField()
    password = TextField()
    active = BooleanField(default=True)
    confirmed_at = DateTimeField(null=True)


class UserRoles(BaseModel):
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)


user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)

try:
    user_datastore.create_user(email='admin@example.com', password='Sekrit')
except:
    pass


@app.before_request
def db_connect():
    db.connect()


@app.teardown_request
def db_close(exc):
    if not db.is_closed():
        db.close()


models = (Role, User, UserRoles)
create_model_tables(models, fail_silently=True)

for model in models:
    admin.add_view(ModelView(model))


@app.route('/')
@login_required
def home():
    user_in_python = User.get(email='admin@example.com')
    return render_template('index.html', user_in_template=user_in_python)


if __name__ == '__main__':
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.debug = True
    app.reload = True
    app.run(host='0.0.0.0')
