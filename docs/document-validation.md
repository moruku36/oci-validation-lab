# 初期文書の確認記録 / Initial documentation validation

確認日：2026-10-13。対象は初期文書で、OCI実行検証ではありません。

| 確認 | 結果 | 制約 |
|---|---|---|
| 日英READMEの内容 | 対象読者、状態、7章、Level 2/3計画、資格名/ID、試験数値、禁止操作と注意が対応 | 詳細資料の主言語は日本語、各主要資料に英語要約 |
| ローカルリンク | `python scripts/check_docs.py` で存在確認 | 外部URLとMarkdown anchorは対象外 |
| 章別の理解確認 | 全7章に問題、解答の要点、証拠課題あり | 独自問題。公式試験問題ではない |
| クラウド状態 | 全実操作未実施と記載 | 成功/無課金/cleanupを証明しない |
| 外部資料 | Oracleの公開試験一覧、告知、更新案内、主要docsを閲覧確認 | MyLearn本文の動的取得制限、objective配点未確認 |
| 機密情報 | 手作業レビューと基本marker確認で認証情報・個人メール・raw OCIDなし | 完全な漏洩不在を自動保証する検査ではない |
| Git identity | 既存repoのauthor/committerで同じnoreplyを確認し本repoで設定 | 既存repoの過去個人メールをコピーしない |

Git identityの既存根拠：[cloud-validation-level3-architectのコミット](https://github.com/moruku36/cloud-validation-level3-architect/commit/ef8b022372c46b9f589ca5d06b2c4b4dae435921)。author/committerは `moruku36` と `12478466+moruku36@users.noreply.github.com`。公開可視性を拡張する依頼はないため、新規repoの可視性はprivateとする。

GitHub一覧で `oci-validation-lab` およびOCI類似名は見つからなかった。既存の `cloud-validation-level2-multicloud` と `cloud-validation-level3-architect` は形式の参照にのみ使い、変更していない。旧候補名のrepoは作成していない。

English summary: Documentation checks cover README parity, local link existence, original chapter checks, activity status, primary sources, basic secret hygiene and the verified noreply identity. They do not verify OCI behavior or complete exam coverage.
