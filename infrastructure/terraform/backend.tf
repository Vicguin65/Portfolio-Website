terraform {
  backend "s3" {
    bucket       = "rcos-terraform"
    key          = "portfolio/api/terraform.tfstate"
    region       = "us-east-1"
    encrypt      = true
    use_lockfile = true
  }
}
