import json
from typing import Dict, Optional

import pandas as pd
import yfinance as yf


class Company:
    def __init__(self,
                 id_: str,
                 name: str) -> None:
        self.__id = id_
        self.__name = name

    def as_dict(self) -> Dict[str, str]:
        return {
            "id": self.__id,
            "name": self.__name,
        }

    def as_json(self, *args, **kwargs) -> str:
        return json.dumps(self.as_dict(), *args, **kwargs)


def search(name: str) -> Optional[Company]:
    """
    >>> search("ベイカレント").as_dict()
    {'id': '6532', 'name': 'ベイカレント・コンサルティング'}
    >>> search("ベイカレ").as_dict()
    {'id': '6532', 'name': 'ベイカレント・コンサルティング'}
    >>> search("ベイ")  # 一意に定まらない
    >>> search("ベインカレント")  # 見つからない
    """
    df = pd.read_csv('search_company/data/company.csv', encoding='utf-8')
    # 良い名寄せ方法がわからない
    df_target = df[df['銘柄名'].str.startswith(name)]
    if len(df_target) != 1:
        return None
    else:
        return Company(
            df_target['コード'].values[0].astype(str),
            df_target['銘柄名'].values[0]
            )


def get_financial_info(company: Company) -> Optional[pd.DataFrame]:
    """
    >>> get_financial_info(Company(id_='6532', name='ベイカレント・コンサルティング')).shape
    (22, 4)
    """
    company_dict = company.as_dict()
    financial_info = yf.Ticker(company_dict['id'] + ".T").financials
    return financial_info


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
