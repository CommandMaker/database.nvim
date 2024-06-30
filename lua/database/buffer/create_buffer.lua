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

local create_buffer = {}

local fs = require('database.utils.fs')
local json = require('database.utils.json')


function create_buffer.register_highlight_groups()
    vim.api.nvim_set_hl(0, 'DatabasePanelColumnType', { link = 'FoldColumn' })
    vim.api.nvim_set_hl(0, 'DatabasePanelIndent', { link = 'Whitespace' })
    vim.api.nvim_set_hl(0, 'DatabasePanelTableIcon', { link = 'Identifier' })
    vim.api.nvim_set_hl(0, 'DatabasePanelColumnIcon', { link = 'WarningMsg' })
    vim.fn.matchadd('DatabasePanelColumnType', '(.*)')
    vim.fn.matchadd('DatabasePanelIndent', '├╴')
    vim.fn.matchadd('DatabasePanelIndent', '╰╴')
    vim.fn.matchadd('DatabasePanelTableIcon', '󰓫')
    vim.fn.matchadd('DatabasePanelColumnIcon', '󰠵')
end

local function get_formatted_struct()
    local struct = json.decode(create_buffer.get_buffer_content())
    local output = { 'Database structure', '' }

    for key, val in pairs(struct) do
        table.insert(output, '  󰓫 ' .. key)

        for i, col in ipairs(val) do
            local indent_char = '├╴'
            if i == #val then
                indent_char = '╰╴'
            end

            local icon = '󰠵'

            if col[6] == 1 then
                icon = '󰌆'
            end

            local default = ''
            if col[5] ~= nil then
                default = ', default : ' .. col[5]
            end

            table.insert(output, ' ' .. indent_char .. ' ' .. icon .. ' ' .. col[2] .. ' (' .. col[3] .. default ..')')
        end

        table.insert(output, '')
    end

    return output
end


function create_buffer.get_buffer_content()
    local db_struct = io.popen(fs.get_backend_command({request = {type = 'query', target = 'db_struct'}})):read('*a')

    if db_struct ~= nil then
        return db_struct
    end

    return '{}'
end

local options = {
    bo = {
        bufhidden = 'wipe',
        filetype = 'database-panel',
        buftype = 'nofile',
        modifiable = false
    },
    wo = {
        winbar = '',
        winblend = 0,
        cursorcolumn = false,
        cursorline = true,
        cursorlineopt = 'both',
        fillchars = 'eob: ',
        list = false,
        number = false,
        relativenumber = false,
        signcolumn = 'no',
        spell = false,
        statuscolumn = '',
        winfixheight = true,
        winfixwidth = true,
        wrap = false,
    }
}

function create_buffer.create_buffer()
    vim.cmd('vsplit')
    vim.cmd('vert resize 35')
    local win = vim.api.nvim_get_current_win()
    local buf = vim.api.nvim_create_buf(false, true)

    for key, val in pairs(options.bo) do
        vim.bo[buf][key] = val
    end

    for key, val in pairs(options.wo) do
        vim.wo[win][key] = val
    end

    vim.bo[buf].modifiable = true
    --vim.api.nvim_buf_set_lines(buf, 0, -1, true, {get_formatted_struct()})
    local lines = get_formatted_struct()
    vim.api.nvim_buf_set_lines(buf, 0, -1, true, lines)
    vim.bo[buf].modifiable = false

    vim.api.nvim_win_set_buf(win, buf)
    create_buffer.register_highlight_groups()
end

return create_buffer
