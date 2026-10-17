# Level 2 administrator validation plan

Status: `PLANNED` for OCI execution. This is this repository's learning stage, not an Oracle certification level. The [multi-cloud Level 2 record](https://github.com/moruku36/cloud-validation-level2-multicloud) motivates explicit lifecycle and evidence gates; its AWS/Azure/GCP results are not OCI evidence.

## Learning objective and boundary

Show that an operator can scope a disposable OCI change, predict its cost, apply only approved resources, verify network and access controls, detect drift, recover from a bounded fault, and prove cleanup. Each phase requires separate human approval before credentials or live changes. The current [Level 1 Terraform model](../terraform/level1-network/README.md) covers only a VCN, one private subnet, an empty security list, and an empty route table. It does not provide a working application. Expanding it to VMs, gateways, load balancers, monitoring, or CI is future work.

## Validation matrix

| Gate | Proposed check | Evidence | Current status |
|---|---|---|---|
| Scope | Named tenancy, dedicated compartment, region, owner, approved resources and expiration | Redacted scope sheet and pre-run inventory | `PLANNED` |
| Cost | Current price estimate, quotas, budget alert, maximum run time and stop condition | Dated estimate; budget alerts are not a hard cap | `PLANNED` |
| IaC | Pinned provider, `fmt`, `validate`, static source and plan-scope checks, reviewed plan | CLI versions, redacted plan summary, reviewer | `OFFLINE-ONLY` for source and synthetic plan checks |
| Access | Least-privilege identity and no public VM management | Policy review and effective access test | `PLANNED` |
| Network | Private subnet, no unapproved ingress/egress or routes, approved connectivity test | Configuration and independent OCI observations | `OFFLINE-ONLY` for mock assertions; live check `PLANNED` |
| Change | Only approved resource IDs and tags; separate apply approval | Before/after inventory and change record | `PLANNED` |
| Drift | Deliberate bounded change and detection; documented reconciliation | Plan output with sensitive fields redacted | `PLANNED` |
| Fault | One recoverable failure with stop and rollback conditions | Timeline, health observation and recovery result | `PLANNED` |
| Cleanup | Destroy only owned resources, inventory residuals, later billing review | Destroy record, fresh inventory and billing check | `PLANNED` |

The offline tests assert the planned private CIDRs, public-IP prohibition, zero security rules, and zero routes. They cannot demonstrate OCI API behavior, isolation, effective IAM, cost, drift, recovery, or deletion. Record those as `UNVERIFIED` until a separately authorized run provides observed evidence.

The [plan scope checker](../scripts/check_plan_scope.py) can inspect the JSON form of a saved Terraform plan after a separately approved operator creates one. It accepts only the four Level 1 resource addresses and pure create or pure delete actions. Run `python scripts/check_plan_scope.py create <private-plan-json>` (or `destroy`) from the repository root. Keep the plan JSON in a private local path; it may contain sensitive values. The script prints only generic findings and does not call OCI. Passing is a review aid, not permission to apply or proof that every attribute is safe; review the plan and current inventory independently.

## Suggested progression

1. Complete Level 1's offline checks and review failures before touching an OCI account.
2. Agree on a short-lived scope, owner, exact resource list, budget, and deletion criteria. Verify current Oracle pricing and service limits for the account.
3. Design a minimal Level 2 application topology with private compute and explicit management path. Review internet egress, image, storage, logs, and monitoring as separate cost and security decisions.
4. Prepare CI with plan-only privileges first. A real apply must require a human approval gate and a scoped identity; never place long-lived credentials in this repository.
5. Execute connectivity, monitoring, bounded fault, drift, and cleanup tests only in the approved environment. Compare expected and observed outcomes in [evidence records](../templates/evidence.md).

No Level 2 cloud test has run. Do not infer production readiness or parity with the referenced multi-cloud experiment.
