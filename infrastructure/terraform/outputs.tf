output "api_url" {
  description = "Public API base URL — set as VITE_API_URL in the frontend"
  value       = "https://${var.api_subdomain}"
}

output "api_gateway_endpoint" {
  description = "Raw API Gateway invoke URL (useful for debugging before DNS propagates)"
  value       = module.api.api_gateway_endpoint
}

output "lambda_function_name" {
  description = "Lambda function name (use for manual invocations or log tailing)"
  value       = module.api.lambda_function_name
}

output "ses_identity_arn" {
  description = "SES email identity ARN — check AWS console to confirm verification email was clicked"
  value       = module.ses.identity_arn
}
