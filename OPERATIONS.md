# Operations Guide

## Local Run

1. Create `.env` from `.env.example`.
2. Set secure values for auth and encryption key.
3. Start stack:

```bash
docker compose up -d
```

4. Open n8n at `http://localhost:5678`.

## Import and Configure Workflows

1. Import one or more workflow JSON files.
2. Open each OpenAI node and map/select your OpenAI credential.
3. Confirm MCP nodes point to `BOX_MCP_SSE_ENDPOINT` (already env-backed).
4. Replace demo Box folder/template IDs in prompts with real values.

## Validation Checklist

- MCP endpoint reachable from n8n container.
- OpenAI credential configured and tested.
- Sample data file available at `/files/sample_claims_data.json` for DocGen flow.
- Manual execution works for each workflow from the trigger node.

## Production Hardening

- Place n8n behind HTTPS reverse proxy.
- Rotate `N8N_ENCRYPTION_KEY` and auth credentials via secret manager.
- Back up `n8n_data` volume regularly.
- Add error trigger workflows for pager/alert channels.
- Restrict outgoing network egress to approved services.
