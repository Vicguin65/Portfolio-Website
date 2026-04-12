Build the React frontend and deploy it to S3 + CloudFront.

Steps:
1. Run `npm run build` inside `portfolio-website/` with `VITE_API_URL=https://api.whoistylerdu.com`
2. Sync `dist/` to `s3://whoistylerdu.com/` — hashed assets get long-lived cache headers, `index.html` gets no-cache. `Resume_Tyler_Du.pdf` is excluded from the sync (it lives in S3 independently and must not be deleted).
3. Create a CloudFront invalidation on distribution `E23G2M0PQP2735` for `/*`
4. Report the invalidation ID and confirm the deploy is live at https://whoistylerdu.com

Use the Bash tool to run each step. Show output so the user can see progress. If any step fails, stop and report the error clearly before proceeding.
