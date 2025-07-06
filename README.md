# Directions API test
RareTECHのハッカソン用に簡易的な技術検証を実施した。

# Requirement
* Google Cloud Consoleにアクセス。新しいプロジェクトを作成。
* 左のナビメニューから「APIとサービス」→「ライブラリ」
* Directions API を検索して「有効にする」　→API_KEYを取得。

# Installation

```bash
pip install -r requirements.txt
cd direction_api_test
touch .env
```
* .envファイルに取得したAPIキーを入力する。「GOOGLE_MAPS_API_KEY ="API_KEY"」

# Note

* 10000リクエストまで無料。
