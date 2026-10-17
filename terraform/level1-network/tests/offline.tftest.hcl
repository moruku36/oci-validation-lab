mock_provider "oci" {}

run "private_network_contract" {
  command = plan

  variables {
    region         = "us-ashburn-1"
    compartment_id = "mock-compartment-for-offline-test"
  }

  assert {
    condition     = oci_core_vcn.lab.cidr_blocks[0] == "10.20.0.0/16"
    error_message = "VCN must retain the offline lab CIDR."
  }

  assert {
    condition     = oci_core_subnet.private.cidr_block == "10.20.1.0/24" && oci_core_subnet.private.prohibit_public_ip_on_vnic
    error_message = "Subnet must stay private and within the documented CIDR."
  }

  assert {
    condition     = length(oci_core_security_list.isolated.ingress_security_rules) == 0 && length(oci_core_security_list.isolated.egress_security_rules) == 0
    error_message = "Security list must contain no ingress or egress rules."
  }

  assert {
    condition     = length(oci_core_route_table.isolated.route_rules) == 0
    error_message = "Route table must contain no routes."
  }
}
