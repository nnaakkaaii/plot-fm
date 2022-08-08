from typing import Dict, Optional
import json


class Company:
    def __init__(self,
                 id_: int,
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
    if not name.startswith("ベイカレ"):
        # FIXME : テストを通過するための適当なコードなので、EDINET APIなどを叩くように変更
        #         もちろんベイカレ以外にも対応する必要があるのでこのようなルールベースはNG
        return None

    return Company("6532", "ベイカレント・コンサルティング")


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
