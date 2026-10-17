output "topology" {
  description = "Learning topology; no live identifiers are printed."
  value = {
    vcn_cidr            = "10.20.0.0/16"
    private_subnet_cidr = "10.20.1.0/24"
    public_ip_on_vnic   = false
    ingress_rules       = 0
    egress_rules        = 0
    route_rules         = 0
    compute_instances   = 0
  }
}
