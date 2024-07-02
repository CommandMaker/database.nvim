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
import sys


def get_plugin_directory() -> str:
    if sys.platform.startswith('win32'):
        path = ''

        if os.getenv('XDG_DATA_HOME') != None:
            path = os.getenv('XDG_DATA_HOME', '')
        elif os.getenv('LOCALAPPDATA') != None:
            path = os.getenv('LOCALAPPDATA', '')
        else:
            # If we're here, I don't know why !
            path = ''

        return os.path.join(path, '')

    return os.path.join(os.path.expanduser('~'), '.local', 'share', 'nvim', 'database.nvim') 


def list_connections() -> list:
    plugin_dir = get_plugin_directory()

    if not os.path.exists(plugin_dir):
        os.mkdir(plugin_dir)

    connections_file = os.path.join(plugin_dir, 'connections.json')

    if os.path.exists(connections_file):
        with open(connections_file, 'r') as f:
            data = f.read()
            return json.loads(data)

    return []
