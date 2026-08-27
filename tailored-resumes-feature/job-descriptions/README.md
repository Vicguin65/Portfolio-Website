# Job Descriptions

Drop a job description here as a `.md` or `.txt` file, then run:

```bash
python tailored-resumes-feature/scripts/tailor_resume.py
```

The filename becomes the output name, so `stripe-backend-eng.md` produces
`tailored-resumes/stripe-backend-eng.md` and `tailored-resumes/Du_Tyler_Resume_Stripe.pdf`.

This README is skipped, and so is any job description that already has output. Use
`--force` to re-run those.

See [../README.md](../README.md) for the full workflow, including how to hand-edit a
resume before sending it.
