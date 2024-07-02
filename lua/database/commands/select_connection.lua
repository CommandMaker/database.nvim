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

local select_connection = {}

local connection_select = require('database.selects.connection_select')
local fs = require('database.utils.fs')
local add_connection = require('database.selects.add_connection')

function select_connection.select_connection()
    connection_select.connection_select(function (choice)
        if choice ~= nil then
            if choice['name'] == '[Add new]' then
                add_connection.add_connection_picker()
                return
            end

            local req = {
                request = 'connection_open',
                data = {
                    connection = choice
                }
            }

            io.popen(fs.get_backend_command(req))
        end
    end)
end

function select_connection.register_command()
    vim.api.nvim_create_user_command('Database', function ()
        select_connection.select_connection()
    end, {})
end

return select_connection
