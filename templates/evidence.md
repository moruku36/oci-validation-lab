# 検証証拠 / Validation evidence template

テンプレートの状態：未記入・未実施。記入後はテンプレートのままと誤認されないよう別ファイル名で保存する。

- Experiment ID / Chapter:
- Status: PLANNED | OFFLINE-ONLY | EXECUTED | FAILED | BLOCKED
- Date/time and timezone:
- Operator / reviewer: role aliases only
- Objective / scope:
- Explicitly out of scope:
- Authorization reference (cloud work only):
- Official sources and access date:
- Assumption / uncertainty:
- Environment: fictional or redacted alias; no raw OCIDs or keys
- Model / settings if AI used: verified value or UNKNOWN

## Expected and observed

| Check | Expected result | Actual observation | Evidence path/time | Verdict |
|---|---|---|---|---|
| Understanding | | | | NOT-TESTED |
| Local artifact | | | | NOT-TESTED |
| Cloud behavior | | | | NOT-TESTED |
| Access restriction | | | | NOT-TESTED |
| Cleanup / residuals | | | | NOT-TESTED |
| Cost / billing | | | | NOT-MEASURED |

記入例は実施結果ではない。期待値を観測値へコピーしない。オフラインの図やpolicy案でcloud checkにPASSを付けない。

## Cost and cleanup

- Approved budget / estimate / currency / tax:
- Resource inventory before and after:
- Dependency-aware deletion plan:
- Retained / blocked resources and why:
- Cleanup scope / evidence / timestamp:
- Usage period / billing check time:
- Billing status: NOT-MEASURED | PENDING | CONFIRMED
- Next billing check / responsible role:

## Redaction and integrity

- Redacted: credentials, tokens, account/user identifiers, IPs, invoice/payment information, private URLs
- Sanitized artifact names and optional SHA-256:
- Unredacted originals stored privately, outside Git:
- Evidence limitations:
- Findings / corrected misunderstanding:
- Next step / retry conditions:

証拠ファイルは `evidence/private/` にローカル保存し、公開/共有するなら機密を除いた要約を新しく作る。private repoでも秘密をコミットしない。
