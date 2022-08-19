from pathlib import Path
from typing import Optional

import pandas as pd


class Company:
    def __init__(self,
                 id: str,
                 name: str) -> None:
        self.__id = id
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name


def search(name: str) -> Optional[Company]:
    """
    >>> s1 = search("ベイカレント")
    >>> s1.id
    '6532'
    >>> s1.name
    'ベイカレント・コンサルティング'
    >>> s2 = search("ベイカレ")
    >>> s2.id
    '6532'
    >>> s2.name
    'ベイカレント・コンサルティング'
    >>> search("ベイ")  # 一意に定まらない
    >>> search("ベインカレント")  # 見つからない
    """
    p = (Path(__file__).parent / 'data/company.csv').absolute()
    df = pd.read_csv(p, encoding='utf-8')
    # 良い名寄せ方法がわからない
    df_target = df[df['銘柄名'].str.startswith(name)]
    if len(df_target) != 1:
        return None
    else:
        return Company(
            df_target['コード'].values[0].astype(str),
            df_target['銘柄名'].values[0]
            )


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
