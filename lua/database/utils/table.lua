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

local tableLib = {}

function tableLib.contains(t, val)
    for _, v in ipairs(t) do
        if val == v then
            return true
        end
    end

    return false
end

function tableLib.unique(t)
    local out = {}

    for _, val in ipairs(t) do
        if not tableLib.contains(out, val) then
            table.insert(out, val)
        end
    end

    return out
end

return tableLib
