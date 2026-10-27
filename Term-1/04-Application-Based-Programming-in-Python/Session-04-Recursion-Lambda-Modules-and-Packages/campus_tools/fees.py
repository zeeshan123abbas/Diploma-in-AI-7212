# campus_tools/fees.py
# Another module inside the campus_tools package

def fee_after_discount(fee, percent=10):
    """Return the fee after a percentage discount."""
    return fee - fee * percent / 100
