from pathlib import Path
from typing import Any, List, Optional

import openpyxl
from openpyxl.worksheet import worksheet

from pkg.env import OUTPUT_DIR


class WorkSheet:
    def __init__(self, ws: worksheet.Worksheet) -> None:
        self.__ws = ws

    def write(self,
              data: List[List[Any]],
              index: Optional[List[Any]] = None,
              header: Optional[List[Any]] = None,
              ) -> None:
        if header is not None:
            for j, col in enumerate(header, start=2):
                self.__ws.cell(row=1, column=j).value = col
        if index is not None:
            for i, ind in enumerate(index, start=2):
                self.__ws.cell(row=i, column=1).value = ind
        for i, row in enumerate(data, start=2):
            for j, elem in enumerate(row, start=2):
                self.__ws.cell(row=i, column=j).value = elem


class WorkBook:
    def __init__(self) -> None:
        self.__wb = openpyxl.Workbook()
        self.__ws_ind = 0
        self.__path: Optional[Path] = None

    def save(self, name: str) -> None:
        assert isinstance(OUTPUT_DIR, str)
        p = Path(OUTPUT_DIR) / name
        self.__wb.save(p)
        self.__path = p

    def create_sheet(self, title: str) -> WorkSheet:
        if self.__ws_ind == 0:
            ws = self.__wb.active
            ws.title = title
        else:
            ws = self.__wb.create_sheet(index=self.__ws_ind, title=title)
        self.__ws_ind += 1
        return WorkSheet(ws)

    @property
    def path(self) -> Optional[Path]:
        return self.__path


def create() -> WorkBook:
    wb = WorkBook()
    return wb


if __name__ == '__main__':
    wb = create()
    sheet = wb.create_sheet('PL')
    sheet.write([[1, 2, 3], [4, 5, 6]],
                header=['a', 'b', 'c'],
                index=['A', 'B'])
    wb.save('test.xlsx')
