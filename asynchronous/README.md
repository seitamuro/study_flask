非同期通信を勉強するためのリポジトリです.Flaskを使っています.以下メモ書き

# requirements.txtの作成と使い方
pip freezeで出力される内容をそのまま使っています｡python -m venv -r requirements.txtで対応した仮想環境を作成することができます｡
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

# psycopg2のインストール

事前にpg_configをインストールする必要がある｡

# PostgreSQLに接続するための設定まとめ

DBの接続先はsetting.pyのDATABASEを以下のように設定する｡
```
DATABASE = "postgresql://{DBのユーザー}:{DBのパスワード}@{url}:{ポート番号}/{DB名}
```

# Nginxとは

Nginx(エンジンエックス)は静的なファイルを返すサーバーのこと｡これを使うことでFlaskではサービスの内容をつくることに集中することができる｡