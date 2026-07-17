# Submit with cURL

Replace the endpoint path and payload from the public SocQ API contract:

```bash
curl -X POST "https://api.socq.ai/v1/platform/resource" \
  -H "Authorization: Bearer $SOCQ_API_KEY" \
  -H "Content-Type: application/json" \
  --data @payload.example.json
```

Save `data.task_id`, then poll:

```bash
curl "https://api.socq.ai/v1/tasks/$TASK_ID?limit=50" \
  -H "Authorization: Bearer $SOCQ_API_KEY"
```
