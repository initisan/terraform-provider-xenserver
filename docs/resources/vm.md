---
# generated by https://github.com/hashicorp/terraform-plugin-docs
page_title: "xenserver_vm Resource - xenserver"
subcategory: ""
description: |-
  VM resource
---

# xenserver_vm (Resource)

VM resource

## Example Usage

```terraform
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
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name_label` (String) The name of the virtual machine
- `template_name` (String) The template name of the virtual machine which cloned from

### Optional

- `other_config` (Map of String) The other config of the virtual machine

### Read-Only

- `id` (String) UUID of the virtual machine
- `snapshots` (List of String) The all snapshots of the virtual machine

## Import

Import is supported using the following syntax:

```shell
terraform import xenserver_vm.vm1 "fa4a1711-fa0d-bfee-25c4-87ba3186c0c1"
```