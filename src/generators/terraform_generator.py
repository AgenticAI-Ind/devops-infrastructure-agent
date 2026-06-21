"""Terraform code generator"""

from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class TerraformGenerator:
    """Generate Terraform code for various cloud providers"""

    def __init__(self):
        self.templates = {}

    async def generate_terraform(
        self,
        provider: str,
        resources: List[Dict[str, Any]]
    ) -> str:
        """Generate Terraform configuration"""
        
        logger.info(f"Generating Terraform for {provider} with {len(resources)} resources")
        
        if provider == "aws":
            return await self._generate_aws_terraform(resources)
        elif provider == "gcp":
            return await self._generate_gcp_terraform(resources)
        elif provider == "azure":
            return await self._generate_azure_terraform(resources)
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    async def _generate_aws_terraform(self, resources: List[Dict[str, Any]]) -> str:
        """Generate AWS Terraform code"""
        
        terraform_code = """terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  default = "us-east-1"
}

"""
        
        for resource in resources:
            resource_type = resource.get("type", "")
            
            if resource_type == "ec2_instance":
                terraform_code += self._generate_ec2_instance(resource)
            elif resource_type == "rds_instance":
                terraform_code += self._generate_rds_instance(resource)
            elif resource_type == "s3_bucket":
                terraform_code += self._generate_s3_bucket(resource)
            elif resource_type == "vpc":
                terraform_code += self._generate_vpc(resource)
        
        return terraform_code

    def _generate_ec2_instance(self, resource: Dict[str, Any]) -> str:
        """Generate EC2 instance resource"""
        name = resource.get("name", "server")
        instance_type = resource.get("instance_type", "t3.medium")
        
        return f"""
resource "aws_instance" "{name}" {{
  ami           = data.aws_ami.ubuntu.id
  instance_type = "{instance_type}"

  tags = {{
    Name = "{name}"
    ManagedBy = "DevOps-Agent"
  }}
}}

data "aws_ami" "ubuntu" {{
  most_recent = true
  owners      = ["099720109477"]  # Canonical

  filter {{
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }}
}}
"""

    def _generate_rds_instance(self, resource: Dict[str, Any]) -> str:
        """Generate RDS instance resource"""
        name = resource.get("name", "database")
        engine = resource.get("engine", "postgres")
        instance_class = resource.get("instance_class", "db.t3.small")
        
        return f"""
resource "aws_db_instance" "{name}" {{
  identifier           = "{name}"
  engine              = "{engine}"
  instance_class      = "{instance_class}"
  allocated_storage   = 20
  db_name             = "{name}_db"
  username            = "admin"
  password            = var.db_password
  skip_final_snapshot = true

  tags = {{
    Name = "{name}"
    ManagedBy = "DevOps-Agent"
  }}
}}

variable "db_password" {{
  type      = string
  sensitive = true
}}
"""

    def _generate_s3_bucket(self, resource: Dict[str, Any]) -> str:
        """Generate S3 bucket resource"""
        name = resource.get("name", "bucket")
        
        return f"""
resource "aws_s3_bucket" "{name}" {{
  bucket = "{name}-${{random_id.bucket_suffix.hex}}"

  tags = {{
    Name = "{name}"
    ManagedBy = "DevOps-Agent"
  }}
}}

resource "random_id" "bucket_suffix" {{
  byte_length = 4
}}
"""

    def _generate_vpc(self, resource: Dict[str, Any]) -> str:
        """Generate VPC resource"""
        name = resource.get("name", "main")
        cidr = resource.get("cidr", "10.0.0.0/16")
        
        return f"""
resource "aws_vpc" "{name}" {{
  cidr_block           = "{cidr}"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {{
    Name = "{name}-vpc"
    ManagedBy = "DevOps-Agent"
  }}
}}
"""

    async def _generate_gcp_terraform(self, resources: List[Dict[str, Any]]) -> str:
        """Generate GCP Terraform code"""
        
        terraform_code = """terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

variable "gcp_project_id" {}
variable "gcp_region" {
  default = "us-central1"
}

"""
        
        for resource in resources:
            resource_type = resource.get("type", "")
            name = resource.get("name", "instance")
            
            if resource_type == "compute_instance":
                terraform_code += f"""
resource "google_compute_instance" "{name}" {{
  name         = "{name}"
  machine_type = "{resource.get('machine_type', 'e2-medium')}"
  zone         = "${{var.gcp_region}}-a"

  boot_disk {{
    initialize_params {{
      image = "debian-cloud/debian-11"
    }}
  }}

  network_interface {{
    network = "default"
  }}
}}
"""
        
        return terraform_code

    async def _generate_azure_terraform(self, resources: List[Dict[str, Any]]) -> str:
        """Generate Azure Terraform code"""
        
        return """terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Azure resources would be generated here
"""

    async def validate_terraform(self, code: str) -> Dict[str, Any]:
        """Validate Terraform code"""
        # Placeholder for terraform validate
        return {
            "valid": True,
            "errors": [],
            "warnings": []
        }

    async def estimate_cost(self, code: str, provider: str) -> float:
        """Estimate infrastructure cost"""
        # Simplified cost estimation
        estimated_cost = 0.0
        
        if "aws_instance" in code:
            estimated_cost += 50.0  # ~$50/month per t3.medium
        if "aws_db_instance" in code:
            estimated_cost += 30.0  # ~$30/month per db.t3.small
        if "aws_s3_bucket" in code:
            estimated_cost += 5.0   # ~$5/month storage
        
        return estimated_cost
