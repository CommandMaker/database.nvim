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

from connections.list_connections import list_connections
from connections.open_connection import open_connection
from connections.close_connection import close_connection


def handle_request(request: str, data: dict = {}) -> dict|list:
    if request == 'connection_list':
        return list_connections()
    elif request == 'connection_open':
        open_connection(data['connection'])
    elif request == 'connection_close':
        close_connection()

    return []
