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

local autocmd = vim.api.nvim_create_autocmd

local stringLib = require('database.utils.string')
local tableLib = require('database.utils.table')

local function reindent_lines(lines)
    local longest_line = 1
    local longest_line_count = 0

    for i, line in ipairs(lines) do
        if line:len() > longest_line_count then
            longest_line = i
            longest_line_count = line:len()
        end
    end

    local splitted_line = stringLib.explode(vim.api.nvim_buf_get_lines(0, longest_line - 1, longest_line, true)[1], '|')

    local output_lines = {}
    local props_exploded = stringLib.explode(lines[1], '|')

    for _, line in ipairs(lines) do
        local s = stringLib.explode(line, '|')
        local l = {}

        for j, sub_line in ipairs(s) do
            local missing_length = splitted_line[j]:len() - sub_line:len()

            if missing_length > 0 then
                table.insert(l, sub_line .. stringLib.fill(missing_length, ' '))
            else
                table.insert(l, sub_line)
            end
        end

        table.insert(output_lines, table.concat(l, '|'))
    end

    local lines_lengths = {}

    for _, val in ipairs(output_lines) do
        table.insert(lines_lengths, val:len())
    end

    local o = tableLib.unique(lines_lengths)

    if #o > 1 and not tableLib.contains(o, 0) then
        return reindent_lines(output_lines)
    else
        return output_lines
    end
end

-- Reindent when switching to normal mode
autocmd({ 'InsertLeave' }, {
    pattern = { '*.database-table' },
    callback = function ()
        local lines = reindent_lines(vim.api.nvim_buf_get_lines(0, 0, -1, false))
        vim.api.nvim_buf_set_lines(0, 0, -1, true, {})
        vim.api.nvim_buf_set_lines(0, 0, 0, true, lines)
    end
})

