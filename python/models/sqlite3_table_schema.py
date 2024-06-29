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

from typing import Any

class SQLite3ColumnSchema:
    cid: int
    name: str
    type: str
    notnull: bool
    dflt_value: str|None
    pk: int

    def __init__(self, column_schema: list) -> None:
        self.cid = int(column_schema[0]) if type(column_schema[0]) == int else column_schema[0]
        self.name = column_schema[1]
        self.type = column_schema[2]
        self.notnull = bool(int(column_schema[3]))
        self.dflt_value = column_schema[4]
        self.pk = bool(int(column_schema[5]))


class SQLite3TableSchema:

    columns: list[SQLite3ColumnSchema]

    def __init__(self, table_schema: list[list[Any]]) -> None:
        self.columns = list(map(lambda c: SQLite3ColumnSchema(c), table_schema))
