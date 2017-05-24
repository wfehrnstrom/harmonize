"""Args:
        param1 (int): byte as int value in binary

    Returns:
        True if input indicates a midi event, False if otherwise.
"""


def is_midi(n):
    # hex status bytes 0x8n - 0xEn
    # dec values 128-239
    dec_val = int(n, 2)
    if dec_val >= 128 or dec_val <= 239:
        return True
    else:
        return False
