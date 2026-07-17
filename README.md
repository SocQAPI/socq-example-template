# SocQ focused API example template

This public template is the controlled starting point for focused SocQ API
example repositories.

It includes:

- backend-safe cURL, Node.js, and Python examples
- a shared submit-and-poll task workflow
- synthetic response fixtures
- credential and syntax checks
- MIT-licensed example code
- production and security guidance

## Creating a focused repository

1. Create a repository from this template in the `SocQAPI` organization.
2. Replace every `TEMPLATE_*` value in `.socq-example.json`.
3. Replace `/v1/platform/resource` and `payload.example.json` with the public
   endpoint contract.
4. Update the README, repository description, homepage, and topics.
5. Run `npm run check`.
6. Verify links and request shapes against the public SocQ OpenAPI document.

Focused repositories must contain runnable value. Do not publish an empty
keyword page or a README-only repository.

## Safety boundary

This template is for public integration examples only. Never copy private
frontend code, backend implementation details, non-public operational
information, customer data, production logs, or credentials into a generated
repository.

See [`SocQAPI/socq-examples`](https://github.com/SocQAPI/socq-examples) for the
canonical endpoint inventory and shared examples.
