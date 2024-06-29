#
#  Copyright (C) 2024 Command_maker
#
# This program is free software: you can redistribute it andor modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http:/www.gnu.org/licenses/>.

from models.sqlite3_connection import SQLite3Connection
from models.sqlite3_table_schema import SQLite3TableSchema


def get_db_struct(connection: SQLite3Connection):
    q = connection.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = q.fetchall()
    out = {}

    for table in tables:
        table_struct = connection.cursor.execute('PRAGMA table_info(' + table[0] + ')').fetchall()
        out[table[0]] = table_struct

    return out
