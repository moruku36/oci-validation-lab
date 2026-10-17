"""Conservatively check a saved Terraform plan JSON for the Level 1 lab.

Read-only: this script never calls Terraform or OCI and never prints plan values.
It is an aid to human review, not authorization to apply or destroy.
"""

import argparse
import json
from pathlib import Path
import sys


EXPECTED = {
    "oci_core_vcn.lab": "oci_core_vcn",
    "oci_core_security_list.isolated": "oci_core_security_list",
    "oci_core_route_table.isolated": "oci_core_route_table",
    "oci_core_subnet.private": "oci_core_subnet",
}


def validate_plan(plan: dict, mode: str) -> list[str]:
    """Return generic errors without disclosing values from the plan."""
    if mode not in {"create", "destroy"}:
        return ["unsupported review mode"]
    changes = plan.get("resource_changes")
    if not isinstance(changes, list):
        return ["resource_changes must be a list"]
    errors: list[str] = []
    seen: set[str] = set()
    required_actions = ["create" if mode == "create" else "delete"]

    for entry in changes:
        if not isinstance(entry, dict):
            errors.append("malformed resource change")
            continue
        address = entry.get("address")
        if address not in EXPECTED:
            errors.append("unexpected resource address")
            continue
        if address in seen:
            errors.append("duplicate resource address")
        seen.add(address)
        if entry.get("mode") != "managed" or entry.get("type") != EXPECTED[address]:
            errors.append("unexpected resource mode or type")
        change = entry.get("change")
        if not isinstance(change, dict) or change.get("actions") != required_actions:
            errors.append("unexpected action, replacement, or no-op")

    if seen != set(EXPECTED):
        errors.append("expected four resource changes")
    output_changes = plan.get("output_changes", {})
    if not isinstance(output_changes, dict) or set(output_changes) - {"topology"}:
        errors.append("unexpected output changes")
    elif output_changes:
        topology = output_changes["topology"]
        if not isinstance(topology, dict) or topology.get("actions") != required_actions:
            errors.append("unexpected topology output action")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("create", "destroy"))
    parser.add_argument("plan_json", type=Path)
    args = parser.parse_args()
    try:
        with args.plan_json.open(encoding="utf-8") as stream:
            plan = json.load(stream)
    except (OSError, UnicodeError, json.JSONDecodeError):
        print("FAIL: cannot read Terraform plan JSON", file=sys.stderr)
        return 1
    if not isinstance(plan, dict):
        print("FAIL: invalid Terraform plan JSON", file=sys.stderr)
        return 1
    errors = validate_plan(plan, args.mode)
    if errors:
        print("FAIL: plan scope check: " + "; ".join(sorted(set(errors))))
        return 1
    print(f"PASS: {args.mode} plan contains exactly four expected resource changes; review values manually")
    return 0


if __name__ == "__main__":
    sys.exit(main())
