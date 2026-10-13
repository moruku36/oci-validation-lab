# OCI基礎 / Foundations

確認日：2026-10-13。[公式資料一覧](sources.md)の各章リンクを併読します。全章の検証状態は `PLANNED`。以下の問いは独自の理解確認であり、実際の試験問題ではありません。章ごとに[章別記録](../templates/chapter-check.md)と[証拠記録](../templates/evidence.md)を使います。

## 1. CloudとOCIの配置

IaaSは計算・ネットワーク・ストレージを基盤として使い、PaaSは管理済みの実行/データ基盤、SaaSは完成したアプリを使う考え方です。管理サービスでも、利用者のデータ、アクセス設定、利用方法への責任は残ります。

OCIではregionが地理的なサービス配置単位です。Availability Domain（AD）はregion内のデータセンター単位、Fault Domain（FD）はAD内の障害影響を分散する配置単位です。regionごとのAD数とサービス提供状況は確認が必要です。複数FDへの配置はリージョン全体の障害対策を証明しません。RTOは復旧までの時間目標、RPOは許容するデータ損失の時間幅です。

確認：①regionとcompartmentは同じ階層か。②単一regionのFD分散でregion障害から復旧できるか。③managedサービスなら利用者のIAM設定責任はなくなるか。

解答の要点：①物理的な配置と論理的な管理範囲は異なる。②別regionへの復旧設計と試験が必要。③残る。証拠：配置図と共有責任の一覧を記録する。実際の可用性は未検証。

## 2. Tenancy、compartment、IAM

Tenancyは組織のOCI資源を管理するルートの範囲です。Compartmentは関連資源を論理的に整理し、アクセスや費用を管理する範囲で、複数regionの資源を含められます。Identity Domainはユーザーやグループ等のアイデンティティを管理します。資源の識別子OCIDと表示名を混同しないでください。

IAM policyでは主体、動作、資源タイプ、範囲を読みます。OCIのpolicyはallowで許可を付与する仕組みで、他クラウドのdeny文をそのまま移植しません。例として「研究者グループが学習compartment内のbucket情報を読める」という要件を分解できます。`inspect/read/use/manage`の動詞はサービスごとに許可操作を確認し、名前だけで推定しません。認証成功は操作権限の存在を保証しません。

確認：①compartmentを作るだけで全員のアクセスを防げるか。②bucket一覧を読む要件にtenancy全体のmanageは適切か。③ログイン成功なのに操作が拒否される理由を1つ挙げる。

解答の要点：①policyと継承範囲の確認が必要。②過大。対象資源/範囲/動作を絞る。③policy不足、範囲相違等。証拠：架空の主体で要件を4要素に分解。実policy変更は行わない。

## 3. Networking

VCNはOCIの仮想ネットワークです。Subnetはアドレス範囲と配置の単位で、regional subnetを基本として検討できます。Route Tableは宛先への次の経路を決め、Security ListやNetwork Security Group（NSG）は通信を許可する条件を設定します。NSGはVNICの集合を対象にできます。routeがあっても通信の許可とは限りません。

Internet Gatewayはインターネットへの経路、NAT Gatewayはprivate資源からの外向き通信、Service Gatewayは対応Oracleサービスへのprivate経路、DRGは外部ネットワーク等への接続に使う仮想ルーターです。Public IP・route・security rule・OS側firewall・アプリの待受は別々の確認対象です。

確認：①private VMの外向き更新通信にPublic IPが必須か。②routeだけでHTTPが通るか。③Object Storageへのprivate経路に検討するgatewayは何か。

解答の要点：①NAT等の経路を検討できる。②許可ルール、OS、待受も確認。③Service Gateway、対応サービスと地域の条件も確認。証拠：通信の始点/終点/port/経路/許可を表にする。疎通成功とは記さない。

## 4. ComputeとStorage

ComputeにはVMとbare metalがあり、imageは起動元、shapeはCPU/メモリ等の構成です。Flexible shapeではOCPUやメモリを選べます。OCPUと他クラウドのvCPUを単純に1対1換算せず、対象shapeの定義で比較します。

Object Storageはbucket/objectとして非構造化データを扱い、Block VolumeはVMに接続するディスク用途、File Storageは共有ファイル用途です。Boot volumeとデータvolume、backupは別の資源になり得ます。VMを停止/終了しても付随ストレージやbackupまで消えるとは限りません。Archiveは取り出し時間や保持条件を含めて検討します。

確認：①画像ファイルを多数保存する基本候補は。②複数VMで共有ファイルシステムを使う候補は。③VM終了画面だけで削除完了と言えるか。

解答の要点：①Object Storage。②File Storage。③volume/backup等の残存確認が必要。証拠：画像・共有ファイル・OSディスクの選択理由と削除対象を記録する。作成は未実施。

## 5. Databaseとアプリサービス

DBではエンジン、管理責任、可用性、backup、復旧、ライセンスを比較します。OCIにはAutonomous AI DatabaseやOracle Databaseのサービス、MySQL HeatWave等があります。Autonomousという名前でも、データモデル・権限・アプリ接続・復旧要件の判断は必要です。最新のサービス名と提供regionは公式資料を再確認します。

Load Balancerは複数backendへトラフィックを配分する選択肢です。Functionsはイベント等でコードを実行するserverlessの選択肢、OKEはKubernetesの管理基盤です。VM・Functions・Kubernetesは学習目標や運用負荷が異なり、初回演習にすべてを組み込む必要はありません。

確認：①DBの自動管理だけでアプリの誤削除に備えた復旧試験は不要か。②短いイベント処理と常時動作VMの選定で何を比べるか。

解答の要点：①不要にはならない。②実行時間/起動/依存/スケール/運用/費用。証拠：架空の画像処理アプリの構成案を1つ選び、代替案と理由を記す。性能・復旧は未検証。

## 6. Securityと運用

IAMは管理API等へのアクセス、network ruleは通信範囲を制御します。暗号化だけで公開設定や過大権限は解消しません。Vaultは鍵等の管理、Cloud Guardは設定や活動の問題検出等に使うサービスです。Security Zonesは指定範囲の資源変更にセキュリティ条件を適用します。管理サービスの機能を有効にしただけで全リスクの解消とは言えません。

Monitoringはメトリクスとalarm、Loggingはログ、Auditは対応するAPI活動の記録に使います。Alarmの条件成立、通知配信、本人への通知到着は別の証拠です。障害の原因確認では時刻、資源、変更、ログ、メトリクスを照合します。

確認：①CPUが高いかを調べる入口は。②誰が管理APIを呼んだかを調べる入口は。③alarm作成だけで通知到達を証明できるか。

解答の要点：①Monitoring。②Audit。③発報と到達の試験が別途必要。証拠：観測したい事象と使う情報を表にする。ログ取得・監視設定は未実施。

## 7. 費用、管理、サポート

費用はComputeだけでなくstorage、backup、network転送、周辺サービス、ログ保持等を含めて見積ります。Free Tierは対象と制限があり、すべての資源が無料という意味ではありません。Budgetは費用を監視して通知するための仕組みで、自動的な支出上限とは扱いません。Service limitとcompartment quotaは費用そのものとは別です。

障害時にはOracleのstatus/サポート情報と自分の設定を分けて調べます。サポート契約や試験料金は契約・地域・時点で確認します。停止、削除、残存ゼロ、請求反映は同じ結果ではありません。

確認：①予算通知を設定すれば超過支出は必ず防げるか。②停止したVMに付属するvolumeの料金は必ず止まるか。③削除直後の請求画面だけで最終費用を確定できるか。

解答の要点：①保証しない。②契約/資源別の課金を確認。③計上遅延を考慮し後日再確認。証拠：[費用/削除計画](cost-and-cleanup.md)を埋める。請求実測は未実施。

English summary: Seven chapters cover placement, identity, networking, compute/storage, databases/app services, operations/security, and costs. Each includes original questions, answer hints, and an evidence task. All cloud checks are unexecuted; desk answers prove understanding only.
