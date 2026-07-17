# SocQ focused API example template

This template is the controlled starting point for focused SocQ API example
repositories. Generated repositories must provide runnable integration value,
not just a keyword page.

## Required public content

Every focused repository must include:

- use cases grounded in the public endpoint contract
- endpoint-specific behavior and limitations
- a complete cURL, Node.js, and Python workflow
- production guidance for retries, timeouts, pagination, deduplication, and logs
- responsible-use and platform-scope notes
- synthetic fixtures with no customer or production data

## Creating a focused repository

1. Create a repository from this template in the `SocQAPI` organization.
2. Replace every `TEMPLATE_*` value in `.socq-example.json`.
3. Replace `/v1/platform/resource` and `payload.example.json` with the public
   endpoint contract.
4. Add endpoint-specific use cases, behavior, production notes, and scope.
5. Update the repository description, homepage, topics, and README links.
6. Run `npm run check` and verify request shapes against the public SocQ
   OpenAPI document.

## Safety boundary

This template is for public integration examples only. Never include private
product source code, non-public operational information, customer data,
production logs, local filesystem paths, or credentials.

See [`SocQAPI/socq-examples`](https://github.com/SocQAPI/socq-examples) for
the canonical endpoint inventory and all published focused repositories.
