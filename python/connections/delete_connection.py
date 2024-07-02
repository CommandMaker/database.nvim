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
from connections.list_connections import get_plugin_directory, list_connections


def delete_connection(connection: dict) -> None:
    connections = list_connections()

    if connections.__contains__(connection):
        connections.remove(connection)

    with open(os.path.join(get_plugin_directory(), 'connections.json'), 'w') as f:
        f.write(json.dumps(connections))
