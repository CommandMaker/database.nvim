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

local connection_select = {}

local json = require('database.utils.json')
local fs = require('database.utils.fs')

function connection_select.connection_select(callback)
    local req = {
        request = 'connection_list'
    }

    local available_connections = json.decode(io.popen(fs.get_backend_command(req)):read('*a'))
    table.insert(available_connections, 1, {name = '[Add new]'})

    vim.ui.select(available_connections, {
        prompt = 'Select a connection',
        format_item = function (item)
            return item['name']
        end
    }, function (choice)
        if choice ~= nil then
            if choice['name'] == '[Add new]' then
                callback(choice)
                return
            end

            local options = {'Connect', 'Delete'}
            vim.ui.select(options, {
                prompt = 'What do you want to do ?',
            }, function (todo)
                if todo ~= nil then
                    if todo == 'Connect' then
                        callback(choice)
                    else
                        io.popen(fs.get_backend_command({request = 'connection_delete', data = { connection = choice }}))
                    end
                end
            end)
        end
    end)
end

return connection_select
