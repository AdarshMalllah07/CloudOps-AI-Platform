resource "aws_instance" "cloudops_server" {

  ami           = "ami-006f82a1d5a27da54"
  instance_type = var.instance_type

  key_name = "cloudops-key"

  vpc_security_group_ids = [
    aws_security_group.cloudops_sg.id
  ]

  tags = {
    Name    = "CloudOps-Server"
    Project = "CloudOps-AI-Platform"
  }
}