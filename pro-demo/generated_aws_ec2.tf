# templates/aws/ec2_instance.tpl

resource "aws_instance" "my-instance" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  key_name      = "my-keypair"
  subnet_id     = "subnet-12345678"

  tags = {
    Name = "my-instance"
  }
}