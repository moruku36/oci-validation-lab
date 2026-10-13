# AWS / Azure / Google CloudからOCIへ

確認日：2026-10-13。用途を理解するための比較であり、権限・課金・可用性・API互換性が同じという意味ではありません。各クラウドの実操作は行っていません。

| 用途 | OCI | AWS | Azure | Google Cloud | 移行時に確認する差 |
|---|---|---|---|---|---|
| 組織の管理範囲 | Tenancy / Compartment | Account / Organizations | Tenant / Subscription / Resource Group | Organization / Folder / Project | Compartmentはaccountやsubscriptionと同じ契約境界ではない |
| 地理的配置 | Region / AD / FD | Region / Availability Zone | Region / Availability Zone | Region / Zone | FDはAZと同義ではない。配置保証はサービス単位 |
| 権限 | Identity Domains / IAM policy | IAM | Entra ID / Azure RBAC | IAM | 主体・scope・継承・動詞の意味が異なる |
| 仮想ネットワーク | VCN | VPC | VNet | VPC | Google Cloud VPCはglobal、OCI VCNはregional |
| Subnet | RegionalまたはAD固有 | AZ固有 | VNet内でregional | Regional | OCIでAWSのAZごとのsubnet設計をそのまま前提にしない |
| VMの通信制御 | NSG / Security List | Security Group / Network ACL | Network Security Group | VPC firewall rules / policies | 同名NSGでも対象と評価方法を確認。対応は概念比較 |
| 仮想マシン | Compute instance / Shape | EC2 / Instance type | Virtual Machines / Size | Compute Engine / Machine type | OCPU/vCPU、architecture、image、課金単位 |
| Object storage | Object Storage | S3 | Blob Storage | Cloud Storage | 公開設定・IAM・versioning・retention・削除挙動 |
| Block / File | Block Volume / File Storage | EBS / EFS | Managed Disks / Azure Files | Persistent Disk・Hyperdisk / Filestore | 永続性、attach、障害範囲、snapshot/backupの残存 |
| Managed database | Autonomous Database等 | RDS / Aurora等 | Azure SQL等 | Cloud SQL / AlloyDB等 | エンジン・互換性・ライセンス・復旧機能を個別評価 |
| Container / Function | OKE / Functions | EKS / Lambda | AKS / Functions | GKE / Cloud Run functions | 実行モデルと管理責任、上限、料金 |
| Metrics / API audit | Monitoring / Audit | CloudWatch / CloudTrail | Azure Monitor / Activity Log | Cloud Monitoring / Cloud Audit Logs | ログ対象・保持・通知到達は別途確認 |
| Budget | Budgets | AWS Budgets | Cost Management budgets | Cloud Billing budgets | 通知をhard spending capと誤認しない |

## 経験者が最初に検証する問い

1. 「同じネットワークの資源なら同じcompartmentにある」は成立するか。論理管理と接続は別です。
2. 「public subnetならすべてのVMがinternetから到達可能」は成立するか。IP・route・rule・OS・待受を確認します。
3. 「停止すれば費用ゼロ」は成立するか。volume・backup・network・周辺サービスを確認します。
4. 「別クラウドで成功したTerraformなら同等に再現できる」は成立するか。provider・認証・API・差分・削除の別検証が必要です。

Oracle側根拠は[公式資料一覧](sources.md)。他クラウドの比較用公式入口：[AWS services comparison](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html)、[Azure fundamentals](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-setup-guide/organize-resources)、[Google Cloud resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)、[Google Cloud VPC](https://cloud.google.com/vpc/docs/vpc)。この表はサービス選定の推奨や機能同等性の保証ではありません。

English summary: Compare purposes, then verify differences in scope, region/zone placement, IAM semantics, network rules, billing and cleanup. These are analogies rather than migration guarantees.
