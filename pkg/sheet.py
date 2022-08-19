from pathlib import Path

import openpyxl

from pkg.env import OUTPUT_DIR


class Sheet:
    def __init__(self) -> None:
        self.__wb = openpyxl.Workbook()
        self.__sh = self.__wb.active

    def set_title(self, name: str) -> None:
        self.__sh.title = name

    def save(self, name: str) -> None:
        p = Path(OUTPUT_DIR) / name
        self.__wb.save(p)


def create(name: str) -> Sheet:
    s = Sheet()
    s.set_title(name)
    return s
