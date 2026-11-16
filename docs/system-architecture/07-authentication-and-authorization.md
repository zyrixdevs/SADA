# 07 — Authentication and authorization

Principals: scoped installation, guild admin for own settings, centrally assigned reviewer, infrastructure operator, limited worker. Guild role does not grant global review; operator does not imply case approval. Use TLS and mTLS or request signature with key ID, canonical body/path, timestamp, nonce, rotation/revocation. Secrets in secret manager. Authenticate then authorize object/field; request guild ID is not authority. Tenant filters on every query. Recheck reviewer scope and case revision at decision.
## Permission matrix

Intake can insert events but cannot approve cases; analysis workers can write versioned findings but cannot change consent; reviewer services can write votes but cannot rewrite incidents; retention workers can delete only eligible expired content; Zyrix alone can execute Discord actions. Database roles and repository APIs must enforce these boundaries independently of the frontend.
