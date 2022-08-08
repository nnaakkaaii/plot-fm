# AWS LambdaによるサーバーサイドのAPI実装

## 環境構築

serverディレクトリにて

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate  # mac,linuxの場合
$ pip3 install -r requirements.local
```

## ローカルにおけるテスト

serverディレクトリにて

```shell
$ for p in $(ls -d */); do pytest $p --doctest-modules; done
```

## ローカルにおけるlintのチェック

serverディレクトリにて

```shell
$ for p in $(ls -d */); do flake8 $p; done
$ for p in $(ls -d */); do isort $p --check-only; done
$ for p in $(ls -d */); do mypy $p; done
```

## ローカルにおけるdockerイメージの検証

各ディレクトリのREADME.mdを参照

* [list_pl](./list_pl/README.md)
* [search_company](./search_company/README.md)
