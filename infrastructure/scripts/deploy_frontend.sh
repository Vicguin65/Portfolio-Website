#!/usr/bin/env bash
# Usage: ./infrastructure/scripts/deploy_frontend.sh [cloudfront-distribution-id]
# Builds the React app and syncs it to the S3 bucket, then invalidates CloudFront.
#
# Prerequisites:
#   - AWS CLI configured (or AWS_* env vars set)
#   - Node.js + npm installed
#   - VITE_API_URL set in portfolio-website/.env.local (or .env.production)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
FRONTEND_DIR="$ROOT_DIR/portfolio-website"

S3_BUCKET="whoistylerdu.com"
CLOUDFRONT_ID="${1:-E23G2M0PQP2735}"

echo "▶ Building React app..."
cd "$FRONTEND_DIR"
npm run build

echo "▶ Syncing to s3://$S3_BUCKET ..."
aws s3 sync dist/ "s3://$S3_BUCKET/" \
  --delete \
  --cache-control "public, max-age=31536000, immutable" \
  --exclude "index.html" \
  --exclude "Resume_Tyler_Du.pdf" \
  --exclude "tyler.jpg"

# index.html should not be cached so browsers always get the latest shell
aws s3 cp dist/index.html "s3://$S3_BUCKET/index.html" \
  --cache-control "no-cache, no-store, must-revalidate"

echo "▶ Invalidating CloudFront distribution $CLOUDFRONT_ID ..."
aws cloudfront create-invalidation \
  --distribution-id "$CLOUDFRONT_ID" \
  --paths "/*" \
  --query 'Invalidation.Id' \
  --output text

echo "✓ Frontend deployed to https://whoistylerdu.com"
