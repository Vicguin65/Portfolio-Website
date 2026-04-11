output "lambda_function_name" {
  value = aws_lambda_function.api.function_name
}

output "api_gateway_endpoint" {
  description = "Raw API Gateway invoke URL (before custom domain is active)"
  value       = aws_apigatewayv2_api.main.api_endpoint
}

output "custom_domain_url" {
  value = "https://${aws_apigatewayv2_domain_name.api.domain_name}"
}
