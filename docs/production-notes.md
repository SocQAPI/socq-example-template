# Production notes

## Shared integration controls

- Keep `SOCQ_API_KEY` on the server and outside browser, mobile, fixture, screenshot, and log output.
- Validate and normalize every input before submit; reject empty arrays, unsupported URL shapes, and invalid enum values.
- Persist `data.task_id` before polling so interrupted workers can resume.
- Use bounded retries with backoff for `429` and transient `5xx` responses.
- Treat `succeeded` and `failed` as terminal states and enforce an application-level timeout.
- Read every result page by following `results.next_cursor` until `results.has_more` is false.
- Deduplicate stored records by stable record ID when a workflow can be retried.
- Log task IDs, status transitions, durations, and record counts; never log credentials or full sensitive payloads.
- Keep callback handling idempotent and retain polling as a fallback when callbacks are used.
- Store `collected_at` with records whose public fields or metrics can change over time.

## Endpoint-specific considerations

- Replace this section with verified behavior from the public endpoint contract.
- Document input semantics, limits, missing fields, ranking, and time sensitivity.
- Do not claim guarantees that the public API contract does not provide.

## Data handling

- Treat public records as changeable snapshots rather than permanent truth.
- Keep raw payloads and exported result files in access-controlled storage.
- Define a retention period and remove data that is no longer needed.
- Review platform terms, privacy requirements, and applicable law before launch.
