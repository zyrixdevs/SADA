# 01 — Security principles

Least authority; explicit purpose-bound opt-in; evidence before inference; human accountability; local guild autonomy; minimization and expiry; auditable correction; safe degradation; privacy-preserving transparency; measured complexity. Exceptions name owner, threat, data, expiry, test and rollback.
## Control mapping

Translate each principle into a concrete control owner and acceptance test: consent defaults off; API scope tests prevent tenant escape; database roles separate ingestion and approval; score tests prove no moderation side effect; correction tests update active projections; outage tests preserve local bot behavior. An exception must name the policy version it changes and the date it expires.
