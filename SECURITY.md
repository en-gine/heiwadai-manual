# セキュリティ設定

## GitHub Pages使用時の注意事項

### 組織アカウントでの設定

1. **プランの確認**
   ```
   組織ページ → Settings → Billing & plans
   ```

2. **GitHub Pagesの可視性設定**
   ```
   リポジトリ → Settings → Pages → Visibility
   - Private: 組織メンバーのみ（要GitHub Team以上）
   - Public: 誰でもアクセス可能
   ```

3. **アクセスログの確認**
   ```
   Settings → Pages → View deployment
   ```

### セキュリティベストプラクティス

- [ ] 機密情報は絶対にコミットしない
- [ ] 定期的にアクセスログを確認
- [ ] 不要になったら速やかに非公開化
- [ ] 組織メンバーの定期的な棚卸し

### 代替ホスティング（より安全）

1. **Netlify** - Basic認証対応
2. **Vercel** - パスワード保護機能
3. **AWS S3 + CloudFront** - IAM制御
4. **社内サーバー** - 完全な制御が可能