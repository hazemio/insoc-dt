"""Safety guards for automated response: allowlist and block expiry."""

import ipaddress
import time

# Default lifetime of a temporary block, in seconds.
DEFAULT_BLOCK_TTL = 900


def is_allowlisted(ip: str, allowlist: list[str]) -> bool:
    """Return True if the IP belongs to any allowlisted network."""
    addr = ipaddress.ip_address(ip)
    return any(addr in ipaddress.ip_network(n, strict=False) for n in allowlist)


def block_expiry(now: float | None = None, ttl: int = DEFAULT_BLOCK_TTL) -> float:
    """Return the timestamp at which a block must be rolled back."""
    start = now if now is not None else time.time()
    return start + ttl
