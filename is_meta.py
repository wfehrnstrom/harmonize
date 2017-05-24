"""Args:
        param1 (int): byte as int value in binary

    Returns:
        True if input indicates a meta event, False if otherwise.
"""


def is_meta(n):
    # hex status byte 0xFF
    # dec value 255
    dec_val = int(n, 2)
    if dec_val == 255:
        return True
    else:
        return False
