"""Synthetic plans only; no OCI access or Terraform plan generation."""

import unittest

from scripts.check_plan_scope import EXPECTED, validate_plan


def plan(actions: list[str]) -> dict:
    return {
        "resource_changes": [
            {
                "address": address,
                "mode": "managed",
                "type": resource_type,
                "change": {"actions": actions},
            }
            for address, resource_type in EXPECTED.items()
        ]
    }


class PlanScopeTests(unittest.TestCase):
    def test_exact_create_and_destroy(self):
        self.assertEqual(validate_plan(plan(["create"]), "create"), [])
        self.assertEqual(validate_plan(plan(["delete"]), "destroy"), [])
        with_output = plan(["create"])
        with_output["output_changes"] = {"topology": {"actions": ["create"]}}
        self.assertEqual(validate_plan(with_output, "create"), [])

    def test_rejects_extra_resource_and_replacement(self):
        expanded = plan(["create"])
        expanded["resource_changes"].append(
            {
                "address": "oci_core_internet_gateway.unapproved",
                "mode": "managed",
                "type": "oci_core_internet_gateway",
                "change": {"actions": ["create"]},
            }
        )
        self.assertTrue(validate_plan(expanded, "create"))
        self.assertTrue(validate_plan(plan(["delete", "create"]), "create"))

    def test_rejects_incomplete_or_output_changing_plan(self):
        incomplete = plan(["create"])
        incomplete["resource_changes"].pop()
        self.assertTrue(validate_plan(incomplete, "create"))
        output_change = plan(["create"])
        output_change["output_changes"] = {"unexpected": {"actions": ["create"]}}
        self.assertTrue(validate_plan(output_change, "create"))


if __name__ == "__main__":
    unittest.main()
