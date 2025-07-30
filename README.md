# 平和台ホテル アプリ管理画面マニュアル

このリポジトリは平和台ホテルアプリの管理画面操作マニュアルを管理しています。

## セットアップ方法

### 1. リポジトリの作成

1. GitHubで新しいプライベートリポジトリを作成
2. リポジトリ名: `heiwadai-manual` （任意の名前でOK）
3. プライベートリポジトリとして作成

### 2. ローカルからプッシュ

```bash
# リモートリポジトリを追加
git remote add origin https://github.com/YOUR_USERNAME/heiwadai-manual.git

# ファイルをステージング
git add .

# 初回コミット
git commit -m "Initial commit: 平和台ホテルアプリ管理画面マニュアル"

# mainブランチにプッシュ
git branch -M main
git push -u origin main
```

### 3. GitHub Pagesの設定

1. GitHubのリポジトリページで Settings → Pages を開く
2. Source を「Deploy from a branch」に設定
3. Branch を「main」、フォルダを「/ (root)」に設定
4. Save をクリック

### 4. GitHub Pagesのアクセス設定（プライベートリポジトリの場合）

プライベートリポジトリでGitHub Pagesを使用する場合：
- GitHub Pro、Team、またはEnterpriseプランが必要
- または、リポジトリをパブリックに変更

アクセス権限の管理：
1. Settings → Manage access でアクセス権限を付与
2. 招待したユーザーのみがサイトを閲覧可能

## ローカル開発

```bash
# 依存関係のインストール
bundle install

# ローカルサーバーの起動
bundle exec jekyll serve

# http://localhost:4000 でプレビュー
```

## ディレクトリ構造

```
.
├── _config.yml           # Jekyll設定ファイル
├── _layouts/            # レイアウトテンプレート
├── index.md             # トップページ
├── プライベート、シェア/  # マニュアルドキュメント
│   ├── *.md            # 各種マニュアル
│   ├── app-user-list/   # ユーザー一覧画像
│   ├── newsletter/      # メルマガ配信画像
│   ├── login-notification/ # ログイン時通知画像
│   ├── admin-manual/    # 管理画面マニュアル画像
│   └── admin-user-registration/ # ユーザー登録方法画像
└── README.md            # このファイル
```

## 注意事項

- 画像ファイル名にスペースが含まれる場合は、URLエンコード（%20）されています
- マークダウンファイルの更新時は、画像パスが正しいことを確認してください
- プライベートリポジトリでGitHub Pagesを使用する場合は、有料プランが必要です