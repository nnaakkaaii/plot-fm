from enum import Enum
from typing import List, Optional

import pandas as pd
import yfinance as yf


class PLAttr(Enum):
    TotalRevenue = '売上高'
    CostOfRevenue = '売上原価'
    GrossProfit = '売上総利益'
    OperatingIncome = '営業利益'
    IncomeBeforeTax = '税引前利益'
    NetIncome = '当期純利益'


class PLRow:
    def __init__(self,
                 fy: int,
                 attr: PLAttr,
                 price: float) -> None:
        self.__fy = fy
        self.__attr = attr
        self.__price = price

    @property
    def fy(self) -> int:
        return self.__fy

    @property
    def attr(self) -> PLAttr:
        return self.__attr

    @property
    def price(self) -> float:
        return self.__price


class PL:
    def __init__(self,
                 company_id: str,
                 company_name: str,
                 data: List[PLRow],
                 ) -> None:
        self.__company_id = company_id
        self.__company_name = company_name
        self.__data = data

    @property
    def company_id(self) -> str:
        return self.__company_id

    @property
    def company_name(self) -> str:
        return self.__company_name

    @property
    def data(self):
        return self.__data

    @classmethod
    def from_dataframe(cls,
                       company_id: str,
                       company_name: str,
                       df: pd.DataFrame) -> 'PL':
        data = []
        for fy, series in df.iteritems():
            for attr, price in series.iteritems():
                at = attr.replace(' ', '')
                if not hasattr(PLAttr, at):
                    continue
                data.append(PLRow(
                    fy=fy.year,
                    attr=getattr(PLAttr, at),
                    price=price,
                ))
        return cls(
            company_id=company_id,
            company_name=company_name,
            data=data
        )


def list(company_id: str, company_name: str) -> Optional[PL]:
    """
    >>> list('0', '')
    """
    financial_df = yf.Ticker(f'{company_id}.T').financials
    if len(financial_df) == 0:
        return None
    return PL.from_dataframe(company_id,
                             company_name,
                             financial_df)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
