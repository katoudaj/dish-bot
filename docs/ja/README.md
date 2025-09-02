# DishBot
このプロジェクトは、LINE Messaging APIを使用して、おすすめのメニューをLINEで配信するボットアプリケーションです。

## 公式LINEアカウント
以下のQRコードからDishBotの公式LINEアカウントを友だち追加できます。

![DishBot公式LINE QRコード](../images/dish_bot_line_qr.png)

## LINE公式アカウント作成手順
自身でLINE公式アカウントを作成する場合の手順は以下の通りです。
1. [LINE Official Account Manager](https://manager.line.biz/) にアクセスします。
2. 「アカウントを作成」ボタンをクリックします。
3. アカウントの種類は個人用でOKです。
4. 必要な情報（アカウント名、メールアドレスなど）を入力して登録します。
5. 作成したアカウントを自分のLINEで友だち追加します。
6. LINE Developersでプロバイダーを作成します。
7. アカウント作成後、管理画面から「Messaging API」を有効にします。
8. 「チャネル基本設定」からチャネルID、チャネルシークレット、アクセストークンを取得します。
9. 取得した情報を `.env` ファイルに設定し、アプリケーションで利用できるようにします。

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
