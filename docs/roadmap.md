# 学習ロードマップ / Learning roadmap

確認日：2026-10-13。各時間は独自の学習目安で、Oracleの推奨時間ではありません。資料の主言語は日本語、READMEは日英対応です。

## 今回の範囲

Level 1の資料作成とオフライン演習手順を整備します。学習者の理解確認・実操作はまだ未実施です。アカウント作成、ログイン、キー発行、課金変更、試験申込、実リソースの作成・更新・削除を今回の作業に含めません。

| 順序 | 内容 | 目安 | 修了時の成果 |
|---|---|---|---|
| 0 | 資格目標・用語を確認 | 30分 | 現行試験と資料確認日を記録 |
| 1 | 基礎第1–2章：配置とIAM | 60–90分 | tenancy/region/compartmentの違いと最小権限を説明 |
| 2 | 第3章：ネットワーク | 60–90分 | 通信経路と許可ルールを別々に描く |
| 3 | 第4–5章：Compute/Storage/DB | 60–90分 | 要件に合わせた選定理由を1つずつ説明 |
| 4 | 第6–7章：運用と費用 | 60分 | 監視・監査・予算・削除確認の違いを説明 |
| 5 | 最初のオフライン演習 | 45–60分 | 構成図、権限案、費用/削除計画、未検証一覧 |
| 6 | 公式教材と章別復習 | 個人差あり | 全章を自分の言葉で説明、誤答を再確認 |
| 7 | 将来：小規模実操作 | 別途計画 | 操作許可・見積り・実測・削除・請求確認の証拠 |

章を修了する条件は、全問への解答、根拠URLの記録、解答の要点との照合、誤答修正です。点数はOracle試験の合格判定と関係ありません。分からないことは不明と記録し、AIの説明を公式資料で再確認します。

## 同じリポジトリでの将来計画

| 段階 | 目的 | 今の状態 | 実施に進む条件 |
|---|---|---|---|
| Level 1 | OCI基礎とFoundations学習 | 文書整備、実操作未実施 | 自分で配置・権限・費用を説明できる |
| Level 2 | administratorレベルの操作実験 | 計画のみ | 対象tenancy/compartment、変更範囲、予算、削除対象を合意 |
| Level 3 | AIをarchitectとして扱う実証実験 | 計画のみ | 固定要件、評価尺度、証拠基準、比較条件、レビュー担当を定義 |

Level 2候補はIAMの最小権限、VCN、Computeのライフサイクル、監視、IaCの差分、drift、復旧、cleanupです。実験単位ごとに許可対象と禁止対象を定めます。

Level 3候補は要件から設計案・ADR・費用・IAM境界・復旧案・検証計画を作る実験です。AIの提案と人間の受入判断を区別し、モデル/設定が未確認ならUNKNOWNと記録します。机上設計とライブ実証を別に評価します。今の計画は実行許可ではありません。

## 既存資料から取り入れた形式

[Level 2 multi-cloud](https://github.com/moruku36/cloud-validation-level2-multicloud/tree/c5d25b637c2a71ffb84b6a7dab6c5f0f994062a0)の期待結果・状態整合・cleanup証拠と、[Level 3 architect](https://github.com/moruku36/cloud-validation-level3-architect/tree/ef8b022372c46b9f589ca5d06b2c4b4dae435921)の机上評価/実証の区別を参考にしました。過去のAWS/Azure/GCPの実施結果をOCIの結果として引き継ぎません。

English summary: Level 1 is prepared documentation, with learner checks and all cloud work unexecuted. Level 2 administrator experiments and Level 3 AI architect experiments are future work in this repository. Estimates and completion gates are local learning aids, not Oracle exam requirements.
