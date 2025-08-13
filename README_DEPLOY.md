# Xserverへのデプロイ設定

## 必要なGitHub Secrets

以下のシークレットをGitHubリポジトリに設定してください：

1. `XSERVER_HOST`: XserverのホストアドレスまたはIPアドレス
2. `XSERVER_USERNAME`: SSHユーザー名（通常は`engine0606`）
3. `XSERVER_SSH_KEY`: SSH秘密鍵（改行を含む全文）
4. `XSERVER_PORT`: SSHポート番号（通常は`10022`）

## Basic認証の設定

1. Xserverにログインし、以下のコマンドで.htpasswdファイルを作成：
   ```bash
   htpasswd -c /home/engine0606/heiwadai-hotel.app/public_html/manual/.htpasswd ユーザー名
   ```

2. パスワードを入力

## デプロイの実行

- mainブランチへのプッシュ時に自動実行
- 手動実行も可能（Actions → Deploy to Xserver → Run workflow）

## 注意事項

- デプロイ時、既存のmanualディレクトリはバックアップされます