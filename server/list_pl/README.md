# ListPL

## ローカルでのテスト

server/list_plディレクトリで

```shell
$ pytest . --doctest-modules
```

## dockerイメージの作成

server/list_plディレクトリ下で

```shell
$ docker build -t fukan-list-pl:latest .
```

## dockerコンテナの作成

```shell
$ CID=$(docker run -d -p 9010:8080 fukan-list-pl:latest)
```

※注意 : 他に9010番ポートで動かしているプロセスがある場合失敗します

プロセスの削除

```shell
$ lsof -i:9010
...  # pid (プロセスID) を取得する
$ kill -9 <pid>
```

## dockerコンテナへのリクエストのテスト

```shell
$ curl -XPOST \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -d '{"company_id": "6532", "company_name": "ベイカレント"}' \
  "http://localhost:9010/2015-03-31/functions/function/invocations"
```

## dockerコンテナの終了

```shell
$ docker stop $CID && docker rm $CID
```
