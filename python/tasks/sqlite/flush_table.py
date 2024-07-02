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


import hashlib
import os
from filesystem.save_to_temp import get_temp_path
from models.sqlite3_connection import SQLite3Connection
from models.table import SQLTable


def flush_table(connection: SQLite3Connection, table: SQLTable) -> None:
    table_path = os.path.join(get_temp_path(), hashlib.md5(connection.path.encode('utf-8')).hexdigest(), table.table_name + '.database-table')
    table_file = open(table_path, 'r')
    table_file_content = table_file.readlines()
    table_path_orig = os.path.join(get_temp_path(), hashlib.md5(connection.path.encode('utf-8')).hexdigest(), table.table_name + '.database-table.orig')
    table_file_orig = open(table_path_orig, 'r')
    col_line = list(map(lambda d: d.replace(' ', '').replace('\n', ''), table_file_content[0].split('|')))

    # Get the columns to update using UNIX diff command
    diff = os.popen(f'diff {table_path_orig} {table_path}').readlines()

    for d in diff:
        line = list(map(lambda e: e.replace('\n', '').strip(' '), d.split('|')))
        if not line[0].startswith('> ') and not d.replace('> ', '') == table_file_content[1]:
            continue

        line[0] = line[0][2:]
        cols = []

        for l in line:
            if type(l) == str and not l.isnumeric():
                cols.append(f'\'{l}\'')
                continue

            cols.append(f'{l}')


        connection.database.execute(f'REPLACE INTO {table.table_name} ({", ".join(col_line)}) VALUES ({", ".join(cols)})')

    connection.database.commit()
    table_file.close()
    table_file_orig.close()
    with open(os.path.join(get_temp_path(), hashlib.md5(connection.path.encode('utf-8')).hexdigest(), table.table_name + '.database-table.orig'), 'w') as f:
        with open(os.path.join(get_temp_path(), hashlib.md5(connection.path.encode('utf-8')).hexdigest(), table.table_name + '.database-table')) as f1:
            f.write(''.join(f1.readlines()))
