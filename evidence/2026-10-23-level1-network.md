# Level 1 network exercise ? OCI Console (2026-10-23)

Status: `EXECUTED` for the narrow network exercise below; `RESOURCE-CLEANUP: PASS` for its named resources; `BILLING: PENDING`. This is **not** a completion claim for Level 1, a Terraform deployment, a VM exercise, or an IAM exercise.

This record is intentionally redacted. It contains no tenancy or resource OCIDs, account details, billing identifiers, credentials, or unprocessed console captures. Full identifiers and the exact deletion receipt stay outside this public repository.

## Scope and observations

Japan East (Tokyo) was selected in the OCI Console. The exercise used a new, temporary compartment and no existing resources were changed.

| Stage | Console path | Observed result |
| --- | --- | --- |
| Isolate | Identity �� Compartments | A temporary compartment entered `Active` at about 09:07 UTC. |
| Create VCN | Networking �� Virtual cloud networks �� basic VCN creation | One IPv4 VCN with `10.77.0.0/16` entered `Available` at about 09:10 UTC. IPv6 and DNS hostnames were off. OCI showed managed default route table, security list, DHCP options and DNS resolver links. No gateway was created. |
| Check default rules | VCN �� Security �� default security list �� Security rules | The new list initially had three ingress rules (SSH and ICMP) and one all-protocol egress rule. All four were removed from **this new VCN only**. The UI then showed no ingress and no egress items. |
| Create subnet | VCN �� Subnets �� Create Subnet �� subnet details | One regional `10.77.1.0/24` subnet became `Available`. The details showed `Private Subnet`, DNS disabled, and the VCN's default route table and DHCP options. The creation form prohibited public IP addresses and selected the now-empty default security list. |
| Clean up subnet | Subnet �� Actions �� Terminate | The subnet disappeared from the VCN's subnet list. |
| Clean up VCN | VCN �� Actions �� Delete | A scan limited to the temporary compartment completed with zero associated resources listed. Deletion was submitted; the compartment's VCN list then showed no items. |
| Clean up compartment | Identity �� Compartments �� temporary compartment �� Actions �� Delete | The detail moved from `Deleting` to terminal `Deleted` at about 09:24 UTC. Its historical deleted entry is not an active compartment. |

The default route table was selected for the subnet, but its individual rules were **not** independently read back. The exercise created no VM, VNIC workload, public IP, internet/NAT/service gateway, peering, load balancer, storage, IPv6 address, or test traffic. IAM policies, credentials, account settings, and contracts were not changed.

## Cost and evidence limits

[Oracle's VCN FAQ](https://www.oracle.com/cloud/networking/virtual-cloud-network/faq/) says creating and using a VCN has no charge; other OCI services and data transfer can incur charges. No such workload or traffic was intentionally used here. The final account bill was not measured and can lag deletion, so this record does not claim a confirmed \0 charge.

No screenshot was saved during the live run. The raw console views contained identifiers and cannot be added to GitHub as public evidence. This text records the observed UI states; it does not substitute for a redacted image. The resources will not be recreated merely to obtain pictures. The private receipt stays outside GitHub.

## Corresponding read-only CLI commands ? **reference only, not executed**

The real exercise was performed in the Console. These examples show where a future authorized operator could list the two resource types; placeholders must be replaced locally and must never be committed. They require a separately configured OCI CLI identity and permissions.

```sh
oci network vcn list --compartment-id '<COMPARTMENT_OCID>' --region ap-tokyo-1
oci network subnet list --compartment-id '<COMPARTMENT_OCID>' --vcn-id '<VCN_OCID>' --region ap-tokyo-1
```

CLI references: [VCN list](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/list.html), [subnet list](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/list.html). No OCI CLI call, Terraform `plan`/`apply`/`destroy`, VM creation/deletion, authentication exercise, or test was performed as part of this live exercise. The earlier [offline Terraform validation](../docs/task-118-validation.md) is a separate result.

## Remaining Level 1 work

Read and document the intended IAM/console concepts and the VM creation/deletion exercise only after separate scope, cost, access, and cleanup checks. A human's understanding or exam readiness cannot be inferred from this network exercise alone.

