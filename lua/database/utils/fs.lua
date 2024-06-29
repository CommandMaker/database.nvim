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

local fs = {}

local json = require('database.utils.json')

function fs.get_script_path()
    local str = debug.getinfo(2, 'S').source:sub(2)
    return str:match('(.*' .. '/' .. ')')
end

function fs.get_backend_command(request_object)
    return 'python ' .. fs.get_script_path() .. '../../../python/main.py ' .. "'" .. json.encode(request_object) .. "'"
end

return fs
