from index import (app, api,)
from Application.Api.login import Login
from Application.Api.tabledata import TableData
from Application.Model.models import db
db


api.add_resource(Login, '/login')
api.add_resource(TableData, '/tabledata')