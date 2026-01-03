import hashlib
from passlib.context import CryptContext

# Prefer Argon2 for new hashes (no 72-byte limit). Keep bcrypt as fallback to verify existing hashes.
pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")

# bcrypt has a 72-byte input limit. To safely handle longer passwords
# we pre-hash them with SHA-256 (hex digest) which produces a 64-char
# string well below the 72-byte limit. This preserves full entropy
# without silently truncating the password.
MAX_BCRYPT_BYTES = 72

def _normalize_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    if len(password_bytes) > MAX_BCRYPT_BYTES:
        return hashlib.sha256(password_bytes).hexdigest()
    return password


def hash_password(password: str) -> str:
    normalized = _normalize_password(password)
    return pwd_context.hash(normalized)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    normalized = _normalize_password(plain_password)
    return pwd_context.verify(normalized, hashed_password)