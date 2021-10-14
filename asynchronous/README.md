非同期通信を勉強するためのリポジトリです.Flaskを使っています.以下メモ書き

# docker-composeの使い方

docker-composeでサーバーを立ち上げる際には以下のコマンドを使用する
```
docker-compose up -d
```

サーバーを落とすときは以下のコマンド
```
docker-compose down
```

WSL上で実行する際はsetup_docker.shを事前に実行する.

# Postgresqlのサーバーの作り方

.envファイルに書いてあるユーザー名,パスワードでログインする.サーバーを作成する際の｢ホスト名/アドレス｣にはdocker inspect \[postresql\]でNetworkSettings->Networks->Gatewayに書いてあるipアドレスを入力する.