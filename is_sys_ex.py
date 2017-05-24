"""Args:
        param1 (int): byte as int value in binary

    Returns:
        True if input indicates a sys_ex event, False if otherwise.
"""


def is_sys_ex(n):
    # hex status bytes 0xF0 and 0xF7
    # dec values between 240 and 247
    dec_val = int(n, 2)
    if dec_val >= 240 or dec_val <= 247:
        return True
    else:
        return False
