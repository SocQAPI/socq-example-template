# Production notes

- Keep `SOCQ_API_KEY` on the server.
- Validate all public-data inputs before submit.
- Store `data.task_id`.
- Poll with backoff and treat `succeeded` and `failed` as terminal.
- Follow result cursors until `has_more` is false.
- Keep polling as a fallback when using callbacks.
- Never log credentials or sensitive payloads.
