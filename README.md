# サンプルプロジェクト: code-serverリバースプロキシ + Flask 静的ファイル配信

このプロジェクトは、Docker環境でcode-serverとFlaskアプリケーションを動作させ、code-serverのリバースプロキシ環墧下でFlaskアプリケーションの静的ファイルを配信するサンプルプロジェクトです。

解説記事

- [code-serverのリバースプロキシ環境下でのFlaskアプリ静的ファイルのパス問題](https://zenn.dev/aplulu/articles/code-server-flask-proxy-static-files)

## セットアップ

1. Dockerイメージのビルドとコンテナ起動

```bash
docker compose up -d --build
```

2. code-serverへのアクセス

- ブラウザで [http://localhost:8080](http://localhost:8080) にアクセス
- `cat config/code-server/config.yaml` で確認できるパスワードを入力

3. Flaskアプリの起動

- code-serverのターミナルで以下のコマンドを実行

```bash
cd app
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
flask run --debug
```

- 実行後、出力されたURLにアクセスするとFlaskアプリが動作し、静的ファイルの配信が正常に行われることを確認できます。

## ディレクトリ構成

```
.
├── Dockerfile
├── README.md
├── app
│   ├── app.py
│   ├── requirements.txt
│   ├── static
│   │   └── styles.css
│   └── templates
│       ├── index.html
│       └── layout.html
└── compose.yaml
```

## License

MIT License
