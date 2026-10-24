from insoc.response.safety import block_expiry, is_allowlisted


def test_allowlist_cidr():
    assert is_allowlisted("10.10.10.5", ["10.10.10.0/24"])
    assert not is_allowlisted("10.10.20.5", ["10.10.10.0/24"])


def test_block_expires_in_future():
    assert block_expiry(now=1000.0, ttl=60) == 1060.0
