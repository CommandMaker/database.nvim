#
#  Copyright (C) 2024 Command_maker
#
# This program is free software: you can redistribute it andor modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http:/www.gnu.org/licenses/>.
#

def format_lines(lines: list[str]) -> list[str]:
    longest_line = max(lines, key=len)

    splitted_line = longest_line.split('|')

    def reindent(line: str) -> str:
        l = line.split('|')
        out = []

        for i, part in enumerate(l):
            missing_length = len(splitted_line[i]) - len(part)

            out.append(part + (' ' * missing_length) if missing_length > 0 else part)

        return ' | '.join(out)


    output = list(map(reindent, lines))
    lengths = set(map(len, output))

    if len(lengths) > 1 and not lengths.__contains__(0):
        return format_lines(output)
    else:
        if not output[1].startswith('-'):
            output.insert(1, '─|─'.join(list(map(lambda l: '─' * len(l), splitted_line))))
        else:
            output[1] = '─|─'.join(list(map(lambda l: '─' * len(l), splitted_line)))

        return output

