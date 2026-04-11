variable "lambda_zip_path" {
  description = "Local path to the Lambda deployment zip"
  type        = string
}

variable "lambda_source_hash" {
  description = "Base64-encoded SHA256 of the zip (triggers re-deploy on change)"
  type        = string
}

variable "route53_zone_id" {
  description = "Route53 hosted zone ID for whoistylerdu.com"
  type        = string
}

variable "api_domain" {
  description = "Custom domain for the API (e.g. api.whoistylerdu.com)"
  type        = string
}

variable "sender_email" {
  description = "SES-verified From address"
  type        = string
}

variable "recipient_email" {
  description = "Email address that receives contact form messages"
  type        = string
}
