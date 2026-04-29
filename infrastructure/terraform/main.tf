terraform {
  required_version = ">= 1.6"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# ── Build Lambda deployment package ───────────────────────────────
# Rebuilds automatically when requirements.txt or any .py source file changes.
resource "null_resource" "lambda_build" {
  triggers = {
    requirements_hash = filemd5("${path.root}/../../backend/requirements.txt")
    source_hash = sha256(join("", [
      for f in sort(fileset("${path.root}/../../backend", "**/*.py")) :
      filemd5("${path.root}/../../backend/${f}")
    ]))
  }

  provisioner "local-exec" {
    interpreter = ["bash", "-c"]
    command     = <<-EOT
      set -euo pipefail
      BUILD="${abspath(path.root)}/.build"
      rm -rf "$BUILD" && mkdir -p "$BUILD"
      pip install \
        -r "${abspath(path.root)}/../../backend/requirements.txt" \
        -t "$BUILD/" \
        --platform manylinux2014_x86_64 \
        --only-binary=:all: \
        --implementation cp \
        --python-version 312 \
        --quiet
      cp -r "${abspath(path.root)}/../../backend/app" "$BUILD/"
      cp "${abspath(path.root)}/../../backend/lambda_function.py" "$BUILD/"
    EOT
  }
}

data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "${abspath(path.root)}/.build"
  output_path = "${abspath(path.root)}/.lambda.zip"
  depends_on  = [null_resource.lambda_build]
}

# ── SES ───────────────────────────────────────────────────────────
module "ses" {
  source       = "./modules/ses"
  sender_email = var.sender_email
}

# ── API (Lambda + API Gateway + custom domain) ────────────────────
module "api" {
  source = "./modules/api"

  lambda_zip_path    = data.archive_file.lambda.output_path
  lambda_source_hash = data.archive_file.lambda.output_base64sha256
  route53_zone_id    = var.route53_zone_id
  api_domain         = var.api_subdomain
  sender_email       = var.sender_email
  recipient_email    = var.recipient_email
  anthropic_api_key  = var.anthropic_api_key
  resume_bucket      = var.domain_name
}
