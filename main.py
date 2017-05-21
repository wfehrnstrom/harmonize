import struct
import tuple_to_string as tp
import get_bit as gb
import get_vlr as gv

f = open('data/bach_846.mid', 'rb')
filedata = f.read()
filetype = struct.unpack("BBBB", filedata[0:4])
str = tp.tuple_to_string(filetype)
print str
header_length = struct.unpack('>I', filedata[4:8])
format = int(struct.unpack('>h', filedata[8:10])[0])
num_chunks = struct.unpack('>h', filedata[10:12])
tick_data = struct.unpack('>h', filedata[12:14])
tick_format = gb.get_bit(int(tick_data[0]), 15)
#Negative SMPTE Format, hours, mins,secs
if(tick_format):
    print 'Unsupported'
#ticks per quarter-note
else:
    bitmask = 0x7FFF
    result = bitmask & int(tick_data[0])
    print result
track_chunk_ver = struct.unpack('BBBB', filedata[14:18])
track_chunk_ver_str = tp.tuple_to_string(track_chunk_ver)
print track_chunk_ver_str
track_chunk_length = struct.unpack('>I', filedata[18:22])
print track_chunk_length[0]
#multiple data chunks each specifying a channel
if(format == 1):
    print 'Hi'
elif(format == 2):
    print 'Hello'
else:
    print 'no'
print header_length
print format
print num_chunks
print tick_format
[vlv, end_index] = gv.get_vlr(filedata[22:], 22)

print 'end index'
print end_index






