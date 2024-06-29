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

local close_connection = {}

local fs = require('database.utils.fs')

function close_connection.close_connection()
    local req = {
        request = 'connection_close'
    }

    io.popen(fs.get_backend_command(req))
end

function close_connection.register_command()
    vim.api.nvim_create_user_command('DatabaseClose', function ()
        close_connection.close_connection()
    end, {})
end

return close_connection
