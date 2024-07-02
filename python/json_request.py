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
import os
import tempfile

from filesystem.save_to_temp import get_temp_path

import controllers.connection_controller as connection_controller
import controllers.query_controller as query_controller
from models.sqlite3_connection import SQLite3Connection


def process_json_request(req: str) -> None:
    request = json.loads(req)

    plugin_temp = os.path.join(tempfile.gettempdir(), 'database.nvim')

    if not os.path.exists(plugin_temp):
        os.mkdir(plugin_temp)

    if type(request['request']) == dict and request['request']['type'] == 'query':
        connection = json.loads(open(os.path.join(get_temp_path(), 'opened_connection.json')).read())
        print(json.dumps(query_controller.handle_request(SQLite3Connection(connection), request)), end='')

    if type(request['request']) == str and request['request'].startswith('connection_'):
        print(json.dumps(connection_controller.handle_request(request['request'], request['data'] if request.__contains__('data') else {})))


