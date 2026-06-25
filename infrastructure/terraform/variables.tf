variable "aws_region" {
  description = "Primary AWS region for backend resources"
  type        = string
  default     = "us-east-1"
}

variable "domain_name" {
  description = "Root domain name"
  type        = string
  default     = "whoistylerdu.com"
}

variable "api_subdomain" {
  description = "Subdomain for the API"
  type        = string
  default     = "api.whoistylerdu.com"
}

variable "route53_zone_id" {
  description = "Route53 hosted zone ID for whoistylerdu.com"
  type        = string
  default     = "Z018519720Z0JNEXD5A5B"
}

variable "sender_email" {
  description = "SES-verified email used as the From address for contact form emails"
  type        = string
  default     = "tyleryeedu@gmail.com"
}

variable "recipient_email" {
  description = "Email address that receives contact form submissions"
  type        = string
  default     = "tyleryeedu@gmail.com"
}

variable "anthropic_api_key" {
  description = "Anthropic API key for the Ask Tyler agent"
  type        = string
  sensitive   = true
}
