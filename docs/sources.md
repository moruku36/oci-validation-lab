# Oracle公式一次情報 / Official sources

確認日：**2026-10-13**。リンク先は更新されるため、受験・実施直前に再確認します。公開資料の確認でありOCIログインやクラウド操作はしていません。MyLearnの動的ページ本文は自動取得できない箇所があり、詳細objective配点を確認できたとは扱いません。

## 資格と教材

| 一次情報 | 用途 / 確認範囲 |
|---|---|
| [日本語試験一覧](https://www.oracle.com/jp/education/certification/certification-exam-list/) | 1Z0-1085-26-JPN、試験名、60分/40問/65%/無償を公開一覧で確認 |
| [Oracle日本 新着ニュース](https://www.oracle.com/jp/education/news/) | 日本語2026試験の2026-09-04開始、Certified資格名 |
| [2026 certification updates](https://blogs.oracle.com/oracleuniversity/oci-certification-learning-paths-and-exams-2026-updates-now-available) | 資格名称の年削除、認定24ヶ月有効の案内 |
| [英語Foundations learning path](https://learn.oracle.com/ols/learning-path/become-an-oci-foundations-associate/163512/163541) | 現行学習入口。詳細objective配点は公開取得では未確認 |
| [日本語Foundations learning path](https://mylearn.oracle.com/ou/learning-path/japanese-become-an-oci-foundations-associate-2026-/164047) | 日本語学習入口。動的内容の自動取得に制約あり |
| [LiveLabs: OCI core services](https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/view-workshop?wid=648) | 将来の公式演習候補。sandbox予約可否は未確認、自分のtenancy利用は課金可能 |

## 基礎の章別資料

| 章 | Oracle資料 | 確認する内容 |
|---|---|---|
| 1 | [OCI入門](https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/baremetalintro.htm)、[Cloud basics](https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/concepts.htm)、[Regions and ADs](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm) | 用語・物理配置 |
| 2 | [IAM overview](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm)、[Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/overview.htm)、[Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm)、[Policy syntax](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/policy-syntax.htm) | 論理scope・主体・policy |
| 3 | [Network overview](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm)、[NSG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm)、[Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm) | VCN・subnet・route・gateway・通信許可 |
| 4 | [Compute](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm)、[Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm)、[Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm)、[Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm)、[File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/filestorageoverview.htm) | image・shape・永続性・storage選定 |
| 5 | [Database docs](https://docs.oracle.com/en-us/iaas/Content/Database/home.htm)、[Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/balanceoverview.htm)、[Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm)、[OKE](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengoverview.htm) | DB/アプリ基盤の認識と選択 |
| 6 | [Monitoring](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm)、[Logging](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm)、[Audit](https://docs.oracle.com/en-us/iaas/Content/Audit/Concepts/auditoverview.htm)、[Vault](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm)、[Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/cloud-guard/using/part-start.htm)、[Security Zones](https://docs.oracle.com/en-us/iaas/Content/security-zone/using/security-zones.htm) | 観測・API活動・鍵・検出・制約 |
| 7 | [Cost Estimator](https://www.oracle.com/cloud/costestimator.html)、[Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm)、[Always Free resources](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm)、[Budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/budgetsoverview.htm) | 費用入力・対象/限度・soft alert |

全章の対応は独自のcourse-aligned構成です。公式の分野別配点や試験全範囲を保証しません。例・理解確認は本リポジトリで作成し、公式問題の転載やexam dumpは含めていません。

English summary: Sources were checked on 2026-10-13. Public exam facts are separated from dynamic content and unverified objective weights. LiveLabs is a future option with sandbox availability unconfirmed; using a personal tenancy can incur charges.
