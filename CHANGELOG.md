# Changelog

## 1.0.0 — 2026-10-01

- Envelope v1 with per-type routing and source rules.
- Nine event types: `ping`, `request.published`, `request.status_changed`, `chat.message`, `bid.placed`, `bid.updated`, `bid.withdrawn`, `pipeline.stage_advanced`, `market.intelligence`.
- Acceptance call request and response schemas.
- Python and TypeScript validators and HMAC-SHA256 signing, tested against shared fixtures and signing vectors.
