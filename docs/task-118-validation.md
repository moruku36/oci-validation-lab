# TASK-118 offline validation record

Date: 2026-10-18 JST. Scope: [Level 1 network model](../terraform/level1-network/README.md) and [Level 2 plan](level2-validation-plan.md). Activity status: `OFFLINE-ONLY`. No OCI credentials were configured, no OCI API was called, and no `terraform plan`, `apply`, or `destroy` was run.

| Check | Result | Evidence and limit |
|---|---|---|
| Terraform CLI download | PASS | HashiCorp Terraform 1.16.6 Windows AMD64 zip SHA-256 matched the official `SHA256SUMS` file before extraction. |
| Provider initialization | PASS | `terraform init -backend=false -input=false` selected oracle/oci 7.32.0; `.terraform.lock.hcl` records the selected provider. Only Registry access was used. |
| Formatting | PASS | `terraform fmt -recursive`, then `terraform fmt -check -recursive`. |
| Schema validation | PASS | `terraform validate -no-color` reported “Success! The configuration is valid.” This checks schema and expressions, not OCI deployment. |
| Mock plan assertions | PASS | `terraform test -no-color`: 1 passed, 0 failed. Fake compartment and mocked OCI provider; private CIDRs, no public IP, no security rules, and no routes asserted. |
| General HCL lint | PASS | TFLint 0.64.0 bundled Terraform rules, `tflint --no-color`: no findings. Its release zip SHA-256 matched the official `checksums.txt`. No OCI-specific rules were used. |
| Static scope guard | PASS | `python scripts/check_iac_scope.py`: exactly four allowed resource types/labels and required private-network properties; rejects explicit rule blocks. The guard is a narrow source check, not a full HCL parser. |
| Plan scope checker | PASS | `python -m unittest discover -s tests`: 3 tests using synthetic JSON. Exact create/delete plans accepted; extra resource, replacement, missing resource and unexpected output rejected. No real OCI plan was generated. |
| Documentation check | PASS | `python scripts/check_docs.py`: 19 Markdown files, local links, fences, basic secret markers and README shared facts. External URLs and semantic parity need manual review. |
| Diff hygiene | PASS | `git diff --check` found no whitespace errors. Sensitive-data review of the proposed diff is required again before PR publication. |

The first `validate` and `test` attempt in the restricted executor failed when the provider child process did not respond to the schema request. TFLint also failed there when local plugin communication was blocked. Repeats through the permitted process execution path passed. These were execution-environment limitations, not demonstrated OCI configuration failures.

## Not verified

OCI API behavior, account IAM, current prices, service limits, real plan, resource creation, isolation in a live tenancy, drift, failure recovery, cleanup and billing. These remain `UNVERIFIED` or `PLANNED`; no production suitability claim follows from the offline checks. Before a live run, obtain a separate approval covering scope, credentials, budget and cleanup ownership.
