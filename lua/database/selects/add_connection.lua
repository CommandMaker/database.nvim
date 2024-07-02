--
--  Copyright (C) 2024 Command_maker
--
-- This program is free software: you can redistribute it andor modify
-- it under the terms of the GNU General Public License as published by
-- the Free Software Foundation, either version 3 of the License, or
-- (at your option) any later version.
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with this program.  If not, see <http:/www.gnu.org/licenses/>.

local add_connection = {}

local fs = require('database.utils.fs')


function add_connection.add_connection_picker()
    local connection = {}
    local connection_types = {{name = 'SQLite 3', type = 'sqlite3'}}

    vim.ui.input({ prompt = 'Enter the name of the new connection : ' }, function (input)
        connection['name'] = input

        if input ~= nil then
            vim.ui.select(connection_types, {
                prompt = 'Choose a type of connection',
                format_item = function (item)
                    return item['name']
                end
            }, function (choice)
                if choice ~= nil then
                    connection['type'] = choice['type']

                    if choice['type'] == 'sqlite3' then
                        vim.ui.input({ prompt = 'Enter the full path of the SQLite 3 database file : ' }, function (path)
                            if path ~= nil then
                                connection['path'] = path
                            end

                            io.popen(fs.get_backend_command({request = 'connection_save', data = connection}))
                        end)
                    end
                end
            end)
        end
    end)
end

return add_connection
