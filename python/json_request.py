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

import json

from models.sqlite3_connection import SQLite3Connection
from models.table import SQLTable
from tasks.sqlite.get_table_schema import get_table_schema
from tasks.sqlite.get_table_content import get_table_content


def process_json_request(req: str) -> None:
    request = json.loads(req)

    if request['connection']['type'] == 'sqlite3':
        connection = SQLite3Connection(request['connection'])

        if request['request'] == 'query':
           results = get_table_content(connection, SQLTable(request['data']))
           print(json.dumps(results))
