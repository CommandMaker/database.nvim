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

import os
from models.sqlite3_connection import SQLite3Connection
from models.table import SQLTable
from filesystem.format_lines import format_lines
from filesystem.save_to_temp import create_temp_folder
from tasks.sqlite.flush_table import flush_table
from tasks.sqlite.get_table_content import get_table_content
from tasks.sqlite.get_db_struct import get_db_struct


def handle_request(connection: SQLite3Connection, request: dict) -> list|dict:
    if request['request']['target'] == 'db_struct':
        if connection.type == 'sqlite3':
            return get_db_struct(connection)
    elif request['request']['target'] == 'table':
        if connection.type == 'sqlite3':
            table_content = get_table_content(connection, SQLTable(request['data']))
            temp_folder = create_temp_folder(connection)
            table_file = os.path.join(temp_folder, request['data']['table_name'] + '.database-table')
            table_file_orig = os.path.join(temp_folder, request['data']['table_name'] + '.database-table.orig')

            table_content = list(map(lambda d: '|'.join(list(map(lambda e: e if type(e) == str else str(e), d))), table_content))

            with open(table_file, 'w') as f:
                f.write('\n'.join(format_lines(table_content)))

            with open(table_file_orig, 'w') as f:
                f.write('\n'.join(format_lines(table_content)))

            return {'result': table_file}
    elif request['request']['target'] == 'flush':
        if connection.type == 'sqlite3':
            flush_table(connection, SQLTable(request['data']))

    return []
