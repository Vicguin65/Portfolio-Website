Run a Terraform plan for the portfolio infrastructure, show the plan to the user, then ask for confirmation before applying.

Steps:
1. `cd infrastructure/terraform`
2. Run `terraform plan -out=tfplan` and display the full output
3. Ask the user: "Apply these changes? (yes/no)"
4. If yes, run `terraform apply tfplan` and show the output including any final outputs (api_url, lambda_function_name, etc.)
5. If no, delete `tfplan` and confirm the plan was discarded

Use the Bash tool for each step. The AWS credentials must already be set in the environment (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION=us-east-1). If they are not set, ask the user to provide them before proceeding.
