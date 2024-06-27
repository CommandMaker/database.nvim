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


import sqlite3


class SQLite3Connection:

    type: str
    path: str
    database: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self, json_obj: dict) -> None:
        self.type = json_obj['type']
        self.path = json_obj['path']
        self.database = sqlite3.connect(self.path)
        self.cursor = self.database.cursor()
