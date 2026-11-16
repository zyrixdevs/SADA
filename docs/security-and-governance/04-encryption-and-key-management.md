# 04 — Encryption and key management

TLS in transit; encrypted DB volume/backups; envelope encryption for restricted evidence. Keys in managed KMS/secret manager, not repo/database. Record key version, define rotation/rewrap/revocation/restore and deletion. Separate environments; test key rotation and restore. Provider, residency, algorithms and custodians open.
## Key lifecycle controls

Assign a key owner and recovery custodian distinct from routine evidence reviewers. Rotation must support old-key decrypt during controlled rewrap, then prove no live object depends on retired key before revocation. Backup recovery drills use isolated credentials and record key access. Lost key means evidence becomes unavailable and is reported; it must not trigger a fallback to plaintext.
