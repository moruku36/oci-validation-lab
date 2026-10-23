# OCI Validation Lab

[English](README.md) | [日本語](README.ja.md)

A learning and validation repository for engineers experienced with AWS, Azure, and Google Cloud who are new to Oracle Cloud Infrastructure (OCI). Start with Level 1 foundations; later use the same repository for administrator operations and AI architect experiments.

**Status (2026-10-13): documentation prepared; no OCI account access, resource deployment, or exam attempt performed.** Level 1/2/3 are this repository's learning stages, not Oracle certification levels. This is independent, unofficial study material with no guarantee of passing an exam.

**Update (2026-10-18):** Added an [offline Level 1 Terraform model](terraform/level1-network/README.md) and [Level 2 validation plan](docs/level2-validation-plan.md). No OCI resources were deployed. See the [validation record](docs/task-118-validation.md).

**Update (2026-10-23 live exercise):** A narrowly scoped VCN and private subnet were created and deleted through the OCI Console in Tokyo. The [public record](evidence/2026-10-23-level1-network.md) separates observed results from unknowns. VM, IAM, live Terraform deployment, and completion of Level 1 remain unverified. Final billing and redacted screenshots are unavailable.\n\n## Five-minute start

1. Read [scope and roadmap](docs/roadmap.md).
2. Draw a tenancy, compartment, region, and VCN using [the first offline lab](labs/01-offline-foundations.md).
3. Answer chapter 1 and 2 checks in [the foundations guide](docs/foundations.md).
4. Copy [the evidence template](templates/evidence.md) locally and label the result `OFFLINE-ONLY`.

Reading and completing this first exercise require no OCI account, keys, subscription, or cloud commands. Future cloud exercises are plans requiring a separately agreed scope and budget.

## Learning structure

```mermaid
flowchart LR
    S[Official Oracle sources] --> L1[Level 1: foundations / prepared]
    L1 --> E[Checks and evidence records]
    E -. future .-> L2[Level 2: administrator / planned]
    L2 -. future .-> L3[Level 3: AI architect / planned]
    L3 --> R[Human evaluation and acceptance]
```

## Contents

| Guide | Use |
|---|---|
| [Roadmap](docs/roadmap.md) | Sequence, time estimates, completion gates, future Level 2/3 |
| [Certification map](docs/certification-map.md) | Current Foundations target and study coverage |
| [Foundations](docs/foundations.md) | Seven chapters with explanation, scenarios, checks and answer hints |
| [Cloud comparison](docs/cloud-comparison.md) | Transfer AWS/Azure/GCP knowledge without assuming equivalence |
| [First lab](labs/01-offline-foundations.md) | Offline topology, access and cost review; no deployment |
| [Level 1 Terraform model](terraform/level1-network/README.md) | Isolated private network example and offline checks; no deployment |
| [Level 2 validation plan](docs/level2-validation-plan.md) | Administrator test matrix and evidence gates; no live execution |
| [Validation record](docs/task-118-validation.md) | Tool versions, checks, results and unverified work |
| [Future hands-on](labs/02-future-object-storage.md) | A bounded object-storage exercise, not executed |
| [Costs and cleanup](docs/cost-and-cleanup.md) | Estimate, stop conditions, residual resources and billing checks |
| [Evidence template](templates/evidence.md) | Expected vs observed results, redaction, cost and deletion evidence |
| [Chapter record](templates/chapter-check.md) | Record answers, uncertainty and retry results |
| [Official sources](docs/sources.md) | Oracle URLs and verification date 2026-10-13 |

## Certification target

The exam target is **Oracle Cloud Infrastructure Foundations Associate**, exam **1Z0-1085-26**, with Japanese exam **1Z0-1085-26-JPN**. The credential is **Oracle Cloud Infrastructure Certified Foundations Associate**; its name does not include an annual suffix in the 2026 naming. The [Japanese official exam list](https://www.oracle.com/jp/education/certification/certification-exam-list/) shows 60 minutes, 40 questions, a 65% pass threshold and no exam fee as of 2026-10-13. This does not make cloud usage free. Use the [official learning path](https://learn.oracle.com/ols/learning-path/become-an-oci-foundations-associate/163512/163541) and [certification map](docs/certification-map.md) to recheck details before booking. Domain weights remain unverified.

## Working rules

Keep evidence of real runs separate from hypotheses. `PLANNED`, `OFFLINE-ONLY`, `EXECUTED`, `FAILED`, and `BLOCKED` describe activity; passing a chapter check does not prove production readiness. Do not commit credentials, raw account identifiers, invoices, unredacted console captures, or Terraform state. GitHub repository privacy does not replace secret hygiene.

The Level 1 Terraform model is available for offline validation but has not been applied. There are no OCI credentials, cloud workflows, or automatic cloud actions. See [contributing](CONTRIBUTING.md) for updating sources and records.
