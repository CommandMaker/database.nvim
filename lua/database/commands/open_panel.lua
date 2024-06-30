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

local open_panel = {}

local create_buffer = require('database.buffer.create_buffer')


function open_panel.open_panel()
    create_buffer.create_buffer()
end

function open_panel.register_command()
    vim.api.nvim_create_user_command('DatabasePanel', function ()
        open_panel.open_panel()
    end, {})
end

return open_panel
