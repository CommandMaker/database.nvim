#
#  copyright (c) 2024 command_maker
#
# this program is free software: you can redistribute it andor modify
# it under the terms of the gnu general public license as published by
# the free software foundation, either version 3 of the license, or
# (at your option) any later version.
# this program is distributed in the hope that it will be useful,
# but without any warranty; without even the implied warranty of
# merchantability or fitness for a particular purpose.  see the
# gnu general public license for more details.
#
# you should have received a copy of the gnu general public license
# along with this program.  if not, see <http:/www.gnu.org/licenses/>.


class SQLTable:

    columns: list[str]
    table_name: str
    extra_args: list[str] = [] 

    def __init__(self, table_obj: dict) -> None:
        self.table_name = table_obj['table_name']
        self.columns = table_obj['columns']
        self.extra_args = table_obj['extra_args'] if table_obj.__contains__('extra_args') else []
