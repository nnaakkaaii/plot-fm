from pathlib import Path

import openpyxl
from openpyxl.worksheet import worksheet

from pkg.env import OUTPUT_DIR


class WorkSheet:
    def __init__(self, wb: 'WorkBook', ws: worksheet.Worksheet) -> None:
        self.__wb = wb
        self.__ws = ws


class WorkBook:
    def __init__(self) -> None:
        self.__wb = openpyxl.Workbook()
        self.__ws_ind = 0

    def save(self, name: str) -> None:
        p = Path(OUTPUT_DIR) / name
        self.__wb.save(p)

    def create_sheet(self, title: str) -> WorkSheet:
        if self.__ws_ind == 0:
            ws = self.__wb.active
        else:
            ws = self.__wb.create_sheet(index=self.__ws_ind, title=title)
        self.__ws_ind += 1
        return ws


def create() -> WorkBook:
    wb = WorkBook()
    return wb
