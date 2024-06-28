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

local json = require('database.utils.json')

local open_table = {}

local function get_script_path()
    local str = debug.getinfo(2, 'S').source:sub(2)
    return str:match('(.*' .. '/' .. ')')
end

function open_table.open_table(table_name)
    local a = {
        connection = {
            type = 'sqlite3',
            path = '/Users/command_maker/Lab/gestion-mdl/server/database.db'
        },
        request = 'query',
        data = {
            table_name = table_name,
            columns = {'*'}
        }
    }

    local table_file = io.popen('python ' .. get_script_path() .. '../../../python/main.py ' .. "'" .. json.encode(a) .. "'")
    vim.cmd('e ' .. json.decode(table_file:read('*a'))['result'])
end

function open_table.register_command()
    vim.api.nvim_create_user_command('DatabaseTable', function ()
        open_table.open_table('users')
    end, {})
end

return open_table
