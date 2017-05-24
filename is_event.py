"""Args:
        param1 (int): byte as int value in binary
    Returns:
        True if input is a status byte, False if otherwise.
"""


def is_event(n):
    if is_midi(n) or is_meta(n) or is_sys_ex(n):
        return True
    else:
        return False
