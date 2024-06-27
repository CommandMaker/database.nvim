#
#  copyright (c) 2024 command_maker
#
# this program is free software: you can redistribute it andor modify
# it under the terms of the gnu general public license as published by
# the free software foundation, either version 3 of the license, or
# (at your option) any later version.
# this program is distributed in the hope that it will be useful,
# but without any warranty; without even the implied warranty of
# merchantability or fitness for a particular purpose.  see the
# gnu general public license for more details.
#
# you should have received a copy of the gnu general public license
# along with this program.  if not, see <http:/www.gnu.org/licenses/>.


import json
from models.sqlite3_connection import SQLite3Connection
from models.table import SQLTable
from models.sqlite3_table_schema import SQLite3TableSchema


def get_table_schema(connection: SQLite3Connection, table: SQLTable) -> SQLite3TableSchema:
    q = connection.cursor.execute(f'PRAGMA table_info({table.table_name})')
    result = q.fetchall()

    return SQLite3TableSchema(result)
