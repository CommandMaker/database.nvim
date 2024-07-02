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

from models.sqlite3_connection import SQLite3Connection
from models.table import SQLTable
from .get_table_schema import get_table_schema


def get_table_content(connection: SQLite3Connection, table: SQLTable):
    q = connection.cursor.execute(f'SELECT {", ".join(table.columns)} FROM {table.table_name} {" ".join(table.extra_args)}')
    results = q.fetchall()

    results.insert(0, table.columns if table.columns != ['*'] else list(map(lambda d: d.name, get_table_schema(connection, table).columns)))
    return results
