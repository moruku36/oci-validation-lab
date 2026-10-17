"""Fail closed if the Level 1 example grows beyond its offline model.

This is a narrow source guard, not a Terraform parser or proof of OCI behavior.
Run terraform validate and test as separate checks.
"""

from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1] / "terraform" / "level1-network"
sources = {path.name: path.read_text(encoding="utf-8") for path in root.glob("*.tf")}
errors = []

expected = {
    ("oci_core_vcn", "lab"),
    ("oci_core_security_list", "isolated"),
    ("oci_core_route_table", "isolated"),
    ("oci_core_subnet", "private"),
}
resources = re.findall(
    r'\bresource\s+"([^"]+)"\s+"([^"]+)"\s*\{',
    "\n".join(sources.values()),
)
if len(resources) != len(expected) or set(resources) != expected:
    errors.append(f"resource set changed: {resources!r}")

main = sources.get("main.tf", "")
required = (
    'cidr_blocks    = ["10.20.0.0/16"]',
    'cidr_block                 = "10.20.1.0/24"',
    "prohibit_public_ip_on_vnic = true",
    "security_list_ids          = [oci_core_security_list.isolated.id]",
    "route_table_id             = oci_core_route_table.isolated.id",
)
for line in required:
    if line not in main:
        errors.append(f"missing Level 1 contract: {line}")

for attribute in ("ingress_security_rules", "egress_security_rules", "route_rules"):
    if re.search(rf"^\s*{attribute}\s*(?:=|\{{)", main, flags=re.M):
        errors.append(f"unexpected {attribute} in main.tf")

if errors:
    print("FAIL: Level 1 IaC scope\n" + "\n".join(errors))
    sys.exit(1)
print("PASS: Level 1 IaC resource allowlist, private subnet and no configured rules")
