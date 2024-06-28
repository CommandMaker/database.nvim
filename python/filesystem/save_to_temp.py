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
#

import os
import tempfile
import hashlib
import shutil

from models.sqlite3_connection import SQLite3Connection

def create_temp_folder(connection: SQLite3Connection) -> str:
    path = os.path.join(tempfile.gettempdir(), 'database.nvim')

    if not os.path.exists(path):
        os.mkdir(path)

    path = os.path.join(path, hashlib.md5(connection.path.encode('utf-8')).hexdigest())

    if not os.path.exists(path):
        os.mkdir(path)

    return path


def delete_temp_folder(connection: SQLite3Connection) -> None:
    path = os.path.join(tempfile.gettempdir(), 'database.nvim', hashlib.md5(connection.path.encode('utf-8')).hexdigest())
    print(hashlib.md5(connection.path.encode('utf-8')).hexdigest())

    if os.path.exists(path):
        shutil.rmtree(path)

