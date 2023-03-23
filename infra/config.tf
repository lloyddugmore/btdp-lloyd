##################
# Terraform config
##################

terraform {
  required_version = "~>1.3"

  required_providers {
    aws = {
      version = "~>4.33"
    }
  }

  backend "s3" {}
}

provider "aws" {
  region = var.aws_region
}


###################################
# Inputs required by terraform-core
###################################
# These are set by the terraform core scripts, which means they shouldn't be set in the .tfvars files
variable "commit_id" {}
variable "terraform_core_region" {}
variable "terraform_state_bucket_name" {}
variable "waybeyond_build_artifacts_bucket_name" {}
variable "environment" {}
variable "component" {}


######################################
# Custom Inputs (set in .tfvars files)
######################################

variable "aws_region" {}


#################################################
# Dynamic inputs (from other component's outputs)
#################################################

# N/A


###########################
# Custom internal variables
###########################

locals {
  # a namespace prefix for all resource names
  ns = "${var.environment}-${var.component}"
}


####################################
# Outputs required by terraform-core
####################################

output "commit_id" {
  value = var.commit_id
}

#########################################################################################
# Custom outputs for other components to use. Make sure breaking changes are communicated
#########################################################################################
output "random_files_bucket_arn" {
  value = aws_s3_bucket.random_files.arn
}

output "random_files_bucket_name" {
  value = aws_s3_bucket.random_files.bucket
}

output "random_files_bucket_id" {
  value = aws_s3_bucket.random_files.id
}