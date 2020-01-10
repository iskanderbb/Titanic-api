variable "client_id" {
    default= "ac9c7854-544b-4452-9805-3dd6f5f886d6"
    }
variable "client_secret" {
    default= "df0ac027-53f6-45e2-b46c-c9c2e3d17c61"
    }

variable "agent_count" {
  default = 2
}

variable "ssh_public_key" {
  default = "~/.ssh/id_rsa.pub"
}

variable "dns_prefix" {
  default = "k8stest"
}

variable cluster_name {
  default = "k8stest"
}

variable resource_group_name {
  default = "nic-k8stest"
}

variable location {
  default = "East US"
}
