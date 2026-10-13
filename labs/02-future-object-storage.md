# Lab 02 — 将来のObject Storageハンズオン

状態：`PLANNED / NOT EXECUTED`。確認日：2026-10-13。実行許可を示す文書ではありません。今回アカウント作成・ログイン・キー発行・リソース変更は行いません。[Oracle Object Storage概要](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm)の現行Console手順と[費用/削除](../docs/cost-and-cleanup.md)を実施前に確認してください。

## 実施条件

本人が用意したOCI環境、専用の学習compartment、必要最小限の既存権限、region、料金と残り無料枠、許容予算、実施時間、削除対象を合意します。既存資源の変更は対象外。条件を満たさない場合は `BLOCKED` にし、権限を広げたりpaid upgradeをしたりして回避しません。

## 合意後の操作計画

1. 開始前にregionとcompartment、既存bucket一覧を確認し、privateな手元記録で操作対象を特定する。repoに生OCIDを貼らない。
2. 見積りを保存する。Standard storage、少量のrequests、download転送、ログ等の料金・残枠・計上遅延を確認。不明項目があれば開始しない。
3. 現行Consoleで `Storage > Object Storage > Buckets` 相当の画面へ進み、対象compartmentを再確認する。UI表記が違う場合は公式手順へ戻る。
4. 専用bucketを1つ作る計画。例 `oci-lab-disposable`。Standard、privateとし、replication、retention rule、versioning、public access、pre-authenticated requestを今回有効化しない。作成前に設定と費用を再確認する。
5. 個人情報を含まないローカル `hello.txt`（内容 `OCI learning sample`、1KB未満）を1つuploadする。共有や公開URLは作らない。
6. 認証されたConsoleからdownloadし、ローカルで内容を照合する。bucketのvisibilityがprivateである設定証拠と、download一致を別々に記録する。匿名アクセス拒否は、この操作だけでは未検証と記す。
7. 合意した専用objectを削除し、対象bucket内が空であることを確認する。もしversioning/retention等が想定外にあるなら削除を進めず差分を記録する。
8. 専用bucketを削除し、同じregion/compartmentの一覧から対象が消えたことを確認する。既存bucket一覧と照合し、既存資源を消していないことを記録する。
9. [証拠テンプレート](../templates/evidence.md)に開始/終了時刻、upload/download、削除、残存、請求確認予定を書く。usage/cost画面は計上遅延後に再確認する。請求未反映なら最終費用は `PENDING`。

## 成功条件と停止条件

成功は、対象のprivate設定、upload/downloadの一致、専用object/bucket削除、同一scopeの残存確認、後日の費用確認をそれぞれ証拠で示すことです。実施中にpublic設定、範囲相違、予期しない資源、retention lock、課金条件不明、権限拒否があれば停止します。削除不能なら未完了の資源と次の対応責任者を記録し、削除成功と書きません。

理解確認：①bucket削除前に何を確認するか。②download成功で匿名アクセス拒否は証明できるか。③削除と請求確定の違いは何か。

解答の要点：①対象scope、object/versions/retention等、既存資源との区別。②できない。③残存確認と計上後のcost確認は別。

English summary: A future, separately authorized console-only lab will create one private Standard bucket and a synthetic tiny object, verify authenticated download, delete only lab resources and recheck billing later. No public links, credentials, or current cloud changes are involved.
