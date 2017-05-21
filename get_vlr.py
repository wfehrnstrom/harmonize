import struct

#Get the variable length time that is represented as some fraction of a beat for beat tick format
#Assumptions: file buf starts at the beginning of the vlr
def get_vlr(file_buf, index):
    end_index = index
    vlv = 0
    vlv_accumulator = 0
    evaluation = 128
    count = 0
    while(evaluation >= 128):
        dataout = int(struct.unpack('>B', file_buf[count])[0])
        SEVEN_BIT_SHIFT = 7
        evaluation = dataout
        vlv = dataout & 0x7F
        count += 1
        vlv_accumulator = (vlv_accumulator << SEVEN_BIT_SHIFT) + vlv
    end_index = end_index + count
    print 'end index'
    print end_index
    print vlv_accumulator
    return [vlv_accumulator, end_index]