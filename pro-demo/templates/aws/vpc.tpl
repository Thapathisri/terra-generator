# templates/aws/vpc.tpl

resource "aws_vpc" "{{ vpc_name }}" {
  cidr_block       = "{{ cidr_block }}"
  instance_tenancy = "{{ instance_tenancy }}"
}
