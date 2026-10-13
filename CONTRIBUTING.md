# 資料の更新 / Contributing

独立した非公式学習資料です。公式情報はOracle一次情報で確認し、URL・確認日・適用範囲を書きます。試験や無料枠の変更を見つけたら、READMEの日英両方、資格対応表、関連章を更新してください。

計画は `PLANNED`、ローカル演習は `OFFLINE-ONLY` とし、実観測がなければ実施済みにしません。未知の費用・モデル設定・資格細目は推測せずUNKNOWNです。実験結果を追加する時は期待値、観測値、証拠、残存資源、請求確認を分けます。

学習記録には[章別テンプレート](templates/chapter-check.md)と[証拠テンプレート](templates/evidence.md)を使います。秘密、raw state、未加工screenshotsをコミットしません。`.gitignore`は補助であり全漏洩を防ぐ保証ではありません。

ローカル文書チェックは `python scripts/check_docs.py`。チェックが通っても内容の正しさや秘密の完全な不在は保証しないため、変更内容を目視レビューします。Git authorとcommitterは検証済みGitHub noreplyに限定します。

English: Update both READMEs when shared facts change. Preserve planned versus observed status, cite current primary sources, redact evidence, check local links, and keep both Git identities on the verified noreply address.
