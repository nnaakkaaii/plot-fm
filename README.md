# plot-fm
plot financial model web app

## 準備

```shell
$ export OUTPUT_DIR=$PWD/tmp
```

## ローカルでのテスト

```shell
$ pytest ./pkg --doctest-modules
```

## dockerイメージの作成

```shell
$ docker build -t fukan:latest .
```

## dockerコンテナの作成

```shell
$ CID=$(docker run -d -p 9000:8080 fukan:latest)
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
$ curl "http://localhost:9000/2015-03-31/functions/function/invocations?name=ベイカレント"
```

## dockerコンテナの終了

```shell
$ docker stop $CID && docker rm $CID
```
