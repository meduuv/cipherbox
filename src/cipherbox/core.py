from __future__ import annotations
import base64, hashlib, hmac, secrets

# CipherBox intentionally exposes primitives only until the authenticated
# encryption container is implemented and tested with a vetted crypto library.
def derive_key(password: str, salt: bytes, rounds: int = 200_000) -> bytes:
    if not password: raise ValueError("password is required")
    if len(salt) < 16: raise ValueError("salt must be at least 16 bytes")
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, rounds, 32)

def make_salt() -> bytes:
    return secrets.token_bytes(16)

def encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode()
