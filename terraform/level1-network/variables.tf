variable "region" {
  description = "OCI region selected for a separately approved exercise."
  type        = string
}

variable "compartment_id" {
  description = "Dedicated lab compartment OCID; never commit a real value."
  type        = string
}

variable "name_prefix" {
  description = "Short label for disposable lab resources."
  type        = string
  default     = "oci-lab-l1"

  validation {
    condition     = can(regex("^[a-z][a-z0-9-]{2,24}$", var.name_prefix))
    error_message = "name_prefix must be 3-25 lowercase letters, digits or hyphens and start with a letter."
  }
}
