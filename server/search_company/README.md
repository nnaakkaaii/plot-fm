# SearchCompany

## ローカルでのテスト

server/search_companyディレクトリで

```shell
$ pytest . --doctest-modules
```

## dockerイメージの作成

server/search_companyディレクトリ下で

```shell
$ docker build -t fukan-search-company:latest .
```

## dockerコンテナの作成

```shell
$ CID=$(docker run -d -p 9000:8080 fukan-search-company:latest)
```

※注意 : 他に9000番ポートで動かしているプロセスがある場合失敗します

プロセスの削除

```shell
$ lsof -i:9000
...  # pid (プロセスID) を取得する
$ kill -9 <pid>
```

## dockerコンテナへのリクエストのテスト

```shell
$ curl -XPOST \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -d '{"company_name": "ベイカレント"}' \
  "http://localhost:9000/2015-03-31/functions/function/invocations"
```

## dockerコンテナの終了

```shell
$ docker stop $CID && docker rm $CID
```
