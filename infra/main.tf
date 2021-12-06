terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.68"
    }
  }

    required_version = ">= 0.14.10"
}

provider "aws" {
  profile = "default"
  region  = "us-east-2"
}

resource "aws_instance" "Terraform-Test-ec2" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}