# Changelog

## 1.2.0 — 2026-10-02

- `request.published`: an allocation line's `amount` may be `null` (and is no longer required). Found by the contract gate on the first
  real backfill: 2 of 13 live requests have allocation lines with no amount because the borrower lets institutions decide the split.
  A line still needs a `product_type`. Loosening only; every v1.1.0 event stays valid.

## 1.1.0 — 2026-10-02

- `request.published`: the employer name is no longer part of Phase 1. It is removed from the allowed
  properties and `employer` is added to the rejected identifiers. In a market the size of Mauritius the employer
  alone can identify a borrower. This tightens validation, but no producer existed yet, so no sender is affected.

## 1.0.0 — 2026-10-01

- Envelope v1 with per-type routing and source rules.
- Nine event types: `ping`, `request.published`, `request.status_changed`, `chat.message`, `bid.placed`, `bid.updated`, `bid.withdrawn`, `pipeline.stage_advanced`, `market.intelligence`.
- Acceptance call request and response schemas.
- Python and TypeScript validators and HMAC-SHA256 signing, tested against shared fixtures and signing vectors.
