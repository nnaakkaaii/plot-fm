import json
from pathlib import Path
from typing import Dict, Optional

import pandas as pd


class Company:
    def __init__(self,
                 id: str,
                 name: str) -> None:
        self.__id = id
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
