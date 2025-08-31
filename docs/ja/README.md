# DishBot
このプロジェクトは、LINE Messaging APIを使用して、おすすめのメニューをLINEで配信するボットアプリケーションです。

## LINE公式アカウント作成手順
1. [LINE Official Account Manager](https://manager.line.biz/) にアクセスします。
2. 「アカウントを作成」ボタンをクリックします。
3. アカウントの種類は個人用でOK
4. 必要な情報（アカウント名、メールアドレスなど）を入力して登録します。
5. 作成したアカウントを自分のLINEで友だち追加
6. LINE Developersでプロバイダーを作成
5. アカウント作成後、管理画面から「Messaging API」を有効にします。
6. 「チャネル基本設定」からチャネルID、チャネルシークレット、アクセストークンを取得します。
7. 取得した情報を `.env` ファイルに設定し、アプリケーションで利用できるようにします。

## 設定方法
1. プロジェクト直下に `.env` ファイルを作成し、`LINE_CHANNEL_ACCESS_TOKEN` に取得したアクセストークンを設定
   ```
   LINE_CHANNEL_ACCESS_TOKEN=ここにトークン
   ```
2. 必要なライブラリをインストール
   ```bash
   pip install -r requirements.txt
   ```

## 実行方法
```bash
python main.py
```
