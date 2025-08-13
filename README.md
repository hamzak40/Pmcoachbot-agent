# PM CoachBot Subscription Agent — Starter (Vercel, FastAPI, Jira + Slack)

This repo lets you:
- Gate access with a **shared subscription key** (MVP)
- Receive **Gumroad webhooks** to log purchases (optional verification)
- Plan ➜ Approve actions for **Jira + Slack**

## 1) Deploy (No-Code Path)
1. Create a GitHub repo and upload these files (Upload files ➜ drag the folder contents).
2. In Vercel: Add New Project ➜ Import Git Repo ➜ Deploy.
3. In Vercel Project ➜ Settings ➜ **Environment Variables**, add values from `.env.example`.
4. Redeploy. Test `/healthz`.

## 2) Auth Model (MVP)
- Admin calls use header: `x-api-key: API_KEY`.
- Customer calls use header: `x-subscription-key: SUBSCRIPTION_KEY` (shared among subscribers for now).
- Upgrade later to per-user keys or OAuth.

## 3) Endpoints
- `GET /healthz` — quick check
- `POST /runs/plan` — dry-run the sequence (requires x-api-key OR x-subscription-key)
- `POST /runs/{run_id}/approve` — execute Jira & Slack actions (requires x-api-key)
- `POST /gumroad/webhook` — logs purchase/cancel events (optional secret)
- `POST /access/test` — verifies provided subscription key

### Example: Plan (Dry-run)
```
curl -X POST "https://<your-app>.vercel.app/runs/plan" \
  -H "Content-Type: application/json" \
  -H "x-subscription-key: YOUR_SUBSCRIPTION_KEY" \
  -d '{
    "intent":"create_sprint_seed_issues_and_post_summary",
    "params":{
      "jira":{
        "projectKey":"FIN",
        "boardId":1234,
        "sprint":{"name":"Sprint 24","startDate":"2025-08-11","endDate":"2025-08-22"},
        "issues":[{"type":"Epic","summary":"Underwriting MVP","labels":["MVP"]}]
      },
      "slack":{"channel":"C0123456789","message":"Planning Sprint 24 for FIN (dry-run)."}
    }
  }'
```

### Example: Approve (Executes)
```
curl -X POST "https://<your-app>.vercel.app/runs/<RUN_ID>/approve" \
  -H "x-api-key: YOUR_ADMIN_API_KEY"
```
