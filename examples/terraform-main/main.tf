locals {
  env_vars = { for tuple in regexall("export\\s*(\\S*)\\s*=\\s*(\\S*)\\s*", file("../../.env")) : tuple[0] => tuple[1] }
}

terraform {
  required_providers {
    xenserver = {
      source = "xenserver/xenserver"
    }
  }
}

provider "xenserver" {
  host     = local.env_vars["XENSERVER_HOST"]
  username = local.env_vars["XENSERVER_USERNAME"]
  password = local.env_vars["XENSERVER_PASSWORD"]
}

data "xenserver_pif" "pif_data" {
  device     = "eth0"
  management = true
}

output "pif_data_out" {
  value = data.xenserver_pif.pif_data
}

resource "xenserver_vm" "vm" {
  name_label    = "Test CentOS VM"
  template_name = "CentOS 7"
  other_config = {
    flag = "1"
  }
}

output "vm_out" {
  value = xenserver_vm.vm
}
