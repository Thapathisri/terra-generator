# templates/aws/ec2_instance.tpl

resource "aws_instance" "{{ instance_name }}" {
  ami           = "{{ ami }}"
  instance_type = "{{ instance_type }}"
  key_name      = "{{ key_name }}"
  subnet_id     = "{{ subnet_id }}"

  tags = {
    Name = "{{ instance_name }}"
  }
}
