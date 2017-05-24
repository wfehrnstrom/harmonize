import struct
import tuple_to_string as tp

""" Args:
        param1: midi file
        param2: index of row of sys_ex start
    Assumptions: 
        file buf starts at the beginning of a determined sys_ex event (as given by param2)
    Returns:  
        Index of the byte directly after the sys_ex event. 
    """


def get_sys_ex(file_buf, index):
    end_index = index # to be returned at end

    # recurrent function so if condition met, the 7th byte (from the right) gives num of bytes until end of event
    # condition: hex F0 (single complete sys_ex msg) or hex F7 (escape sequence; entered func 2nd time)
    # NOTE: IN UNPACKING, '>B' IS LIKELY COMPLETELY WRONG; DO NOT KNOW SYNTAX, MIRRORED GET_VLV
    first_val = int(struct.unpack('>B', file_buf[index])[0])
    single_id = 240 # dec equivalent of F0
    escape_id = 247 # dec equivalent of F7
    if first_val == escape_id or first_val == single_id:
        len_index = 1 # 7th byte index (see above for purpose)
        length = int(struct.unpack('>B', file_buf[index])[len_index])
        end_index = index + length
        return end_index

    # each sys_ex section ends with F7; if not Cairo, must keep checking to find last F7 (there will be multiple)
    # F7 will be first bit of last byte (of a section or the entire sys_ex msg)

    # find first occurrence of hex F7
    bit_zero_index = 7
    exit_val = escape_id # dec equivalent of hex F7
    bit_zero = int(struct.unpack('>B', file_buf[index])[bit_zero_index])
    while bit_zero != exit_val:
        end_index += 1
        bit_zero = int(struct.unpack('>B', file_buf[end_index])[bit_zero_index])

    # if next byte a midi, meta or sys_ex event, exit out; otherwise, feed in get_sys_ex again with updated index
    next_byte_str = tp.tuple_to_string(struct.unpack('>B', file_buf[end_index]))
    next_byte_int = int(next_byte_str)
    if is_event(next_byte_int):
        return end_index
    else:
        return get_sys_ex(file_buf, end_index)














