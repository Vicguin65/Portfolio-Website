terraform {
  backend "s3" {
    # Reuse existing bucket + DynamoDB lock table from prior projects
    bucket         = "rcos-terraform"
    key            = "portfolio/api/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform_tf_lockid"
    encrypt        = true
  }
}
