# 費用と削除の確認 / Cost and cleanup

確認日：2026-10-13。状態：計画のみ、費用実測・実削除未実施。[Oracle Cost Estimator](https://www.oracle.com/cloud/costestimator.html)、[Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm)、[Always Freeの現行条件](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm)、[Budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/budgetsoverview.htm)を実施時に再確認します。

## 見積り

| 項目 | 記録する入力 | 初期状態 |
|---|---|---|
| Compute | region、shape、architecture、OCPU、memory、稼働時間 | UNKNOWN |
| Storage | boot/data volume、bucket tier、容量、backup、保持期間 | UNKNOWN |
| Network | egress量、gateway、LB、接続サービス | UNKNOWN |
| Operations | ログ量/保持、監視、通知、鍵等 | UNKNOWN |
| Contract | 通貨/税、account種別、残無料枠、trial期限 | UNKNOWN |

基本は「単価 × 利用量」の積算ですが、最低保持期間、取り出し、requests、転送、時間単位等の条件も確認します。上限予算、終了予定、停止条件を決め、未知の費用があるなら実行を保留します。数値は最新公式見積りと本人の対象環境で埋めます。

Free Tier/Always Freeは無課金保証ではありません。対象tenancy、home region、資源別限度、既存使用量、無料対象label、trialとpaidの違い、idle資源回収、容量不足を確認します。古い記事のAmpere A1容量をコピーせず、上記の現行公式限度を参照します。容量不足でも、許可なく別の有料shapeやpaid accountへ変更しません。

Budgetはsoft alertでありhard spending capではありません。通知の遅延や費用計上の遅延があるため、予算通知だけを停止判断にしません。停止してもstorage等の課金が残り得ます。

## 削除前後のチェック

1. 作成資源台帳を用意：論理名、種別、scope、作成時刻、依存先、削除対象/保持対象。生識別子はprivateな手元記録に置く。
2. 実施前の既存資源一覧と比較し、lab専用資源だけを対象にする。名前だけで一致判定しない。
3. 依存関係の逆順に処理する。Object Storageはobject/version/retention等を先に確認。Computeはinstanceに加えてboot/data volume、backup、IP等を別に確認する。
4. 削除操作の応答だけで終了しない。同じregion/compartment/対象識別子で再照会し、非表示のfilterや別scopeを見ていないことを確認する。
5. 複数regionやglobal/IAM資源を作った場合は、その対象範囲を別途確認する。削除権限不足・retention等で残るものは `BLOCKED` とする。
6. 計上遅延後にusage/costを再確認する。期限、担当、結果を記録。削除成功でも過去の使用料金は残る。

## 結果の書き方

`RESOURCE-CLEANUP: PASS` は合意した対象資源の残存が証拠で否定できた時だけです。`BILLING: PENDING` は請求未反映、`BILLING: CONFIRMED` は確認時点と対象使用期間を記録できた時です。全tenancyの資源ゼロや無課金を、狭いlabの証拠から主張しません。

初回オフライン演習は `CLEANUP: NOT-APPLICABLE (no OCI resources created)`、`BILLING: NOT-MEASURED` と記録します。

English summary: Verify current eligibility and account-specific usage instead of promising a free lab. Budgets are soft alerts. Resource deletion, residual-resource checks and delayed billing confirmation require separate evidence.
