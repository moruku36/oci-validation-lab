# This example describes only a VCN and an isolated private subnet. It is not
# applied by this repository's checks. A real apply requires separate approval.
resource "oci_core_vcn" "lab" {
  compartment_id = var.compartment_id
  cidr_blocks    = ["10.20.0.0/16"]
  display_name   = "${var.name_prefix}-vcn"
  dns_label      = "l1vcn"
}

# Explicitly empty rules avoid inheriting the VCN's default security list.
resource "oci_core_security_list" "isolated" {
  compartment_id = var.compartment_id
  vcn_id         = oci_core_vcn.lab.id
  display_name   = "${var.name_prefix}-deny-all"
}

# No internet, NAT, or service gateway and no route rules.
resource "oci_core_route_table" "isolated" {
  compartment_id = var.compartment_id
  vcn_id         = oci_core_vcn.lab.id
  display_name   = "${var.name_prefix}-no-routes"
}

resource "oci_core_subnet" "private" {
  compartment_id             = var.compartment_id
  vcn_id                     = oci_core_vcn.lab.id
  cidr_block                 = "10.20.1.0/24"
  display_name               = "${var.name_prefix}-private"
  dns_label                  = "l1private"
  prohibit_public_ip_on_vnic = true
  security_list_ids          = [oci_core_security_list.isolated.id]
  route_table_id             = oci_core_route_table.isolated.id
}
