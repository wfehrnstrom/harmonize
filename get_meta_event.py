import struct
import get_vlv as gv

def get_meta_event(file_buf, index):
    #KNOWN SIGNATURES

    count = index
    signature = int(struct.unpack('>B', file_buf[count])[0])
    print signature
    if(signature != 255):
        print 'Not a meta event.'
    else:
        print 'Meta event.'
        idArr = [0, 0];
        print 'ID ARRAY'
        for i in range(1, len(idArr)):
            count += 1
            idNum = int(struct.unpack('>B', file_buf[count])[0])
            print idNum
            idArr[i] = idNum
        [data, end_index] = gv.get_vlv(file_buf[index + count:], count)
        print 'DATA:'
        print data
        count += end_index
    return count